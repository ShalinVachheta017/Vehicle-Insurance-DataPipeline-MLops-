"""
Main application entry point for the Vehicle Insurance Data Pipeline MLops project.
Handles orchestration of the pipeline and serves as the primary script to run the project.
"""

import os
import traceback
from typing import Optional

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from uvicorn import run as app_run

from src.pipline.prediction_pipeline import VehicleData, VehicleDataClassifier
from src.pipline.training_pipeline import TrainPipeline

# -----------------------------
# App + Config
# -----------------------------
APP_HOST = os.getenv("APP_HOST", "0.0.0.0")
APP_PORT = int(os.getenv("APP_PORT", "5000"))

app = FastAPI()

# Docker-safe base directory (this file's folder)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Static + Templates (absolute paths => stable in Docker)
app.mount(
    "/static",
    StaticFiles(directory=os.path.join(BASE_DIR, "static")),
    name="static",
)
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Health check
# -----------------------------
@app.get("/health")
def health():
    return {"status": "ok"}


# -----------------------------
# Form parser
# -----------------------------
class DataForm:
    """
    Handles and converts incoming form data to correct numeric types.
    """

    def __init__(self, request: Request):
        self.request: Request = request
        self.Gender: Optional[int] = None
        self.Age: Optional[int] = None
        self.Driving_License: Optional[int] = None
        self.Region_Code: Optional[float] = None
        self.Previously_Insured: Optional[int] = None
        self.Annual_Premium: Optional[float] = None
        self.Policy_Sales_Channel: Optional[float] = None
        self.Vintage: Optional[int] = None
        self.Vehicle_Age_lt_1_Year: Optional[int] = None
        self.Vehicle_Age_gt_2_Years: Optional[int] = None
        self.Vehicle_Damage_Yes: Optional[int] = None

    async def get_vehicle_data(self):
        """
        Fetch form values and convert to correct numeric types.
        NOTE: form.get() returns strings -> conversion avoids ML pipeline errors.
        """
        form = await self.request.form()

        # Convert safely (raise clear error if missing / wrong)
        self.Gender = int(form.get("Gender"))
        self.Age = int(form.get("Age"))
        self.Driving_License = int(form.get("Driving_License"))
        self.Region_Code = float(form.get("Region_Code"))
        self.Previously_Insured = int(form.get("Previously_Insured"))
        self.Annual_Premium = float(form.get("Annual_Premium"))
        self.Policy_Sales_Channel = float(form.get("Policy_Sales_Channel"))
        self.Vintage = int(form.get("Vintage"))
        self.Vehicle_Age_lt_1_Year = int(form.get("Vehicle_Age_lt_1_Year"))
        self.Vehicle_Age_gt_2_Years = int(form.get("Vehicle_Age_gt_2_Years"))
        self.Vehicle_Damage_Yes = int(form.get("Vehicle_Damage_Yes"))


# -----------------------------
# Routes
# -----------------------------
@app.get("/", tags=["authentication"])
async def index(request: Request):
    """
    Renders the main HTML form page.
    """
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "context": "Rendering"},
    )


@app.get("/train")
async def trainRouteClient():
    """
    Trigger model training pipeline.
    """
    try:
        train_pipeline = TrainPipeline()
        train_pipeline.run_pipeline()
        return Response("Training successful!!!")
    except Exception as e:
        traceback.print_exc()
        return Response(f"Error Occurred! {e}", status_code=500)


@app.post("/")
async def predictRouteClient(request: Request):
    """
    Receive form data and return prediction on same page.
    """
    try:
        form = DataForm(request)
        await form.get_vehicle_data()

        vehicle_data = VehicleData(
            Gender=form.Gender,
            Age=form.Age,
            Driving_License=form.Driving_License,
            Region_Code=form.Region_Code,
            Previously_Insured=form.Previously_Insured,
            Annual_Premium=form.Annual_Premium,
            Policy_Sales_Channel=form.Policy_Sales_Channel,
            Vintage=form.Vintage,
            Vehicle_Age_lt_1_Year=form.Vehicle_Age_lt_1_Year,
            Vehicle_Age_gt_2_Years=form.Vehicle_Age_gt_2_Years,
            Vehicle_Damage_Yes=form.Vehicle_Damage_Yes,
        )

        # DataFrame for model
        vehicle_df = vehicle_data.get_vehicle_input_data_frame()

        # Predictor
        model_predictor = VehicleDataClassifier()
        value = model_predictor.predict(dataframe=vehicle_df)[0]

        status = "Response-Yes" if int(value) == 1 else "Response-No"

        return templates.TemplateResponse(
            "index.html",
            {"request": request, "context": status},
        )

    except Exception as e:
        # Full traceback in docker logs
        traceback.print_exc()
        return {"status": False, "error": str(e)}


# -----------------------------
# Run app
# -----------------------------
if __name__ == "__main__":
    app_run(app, host=APP_HOST, port=APP_PORT)

"""
Use test dataset to see our model prediction result on web page is correct or not.

test dataset can be found in:
artifacts/data_ingestion/../test.csv
"""
