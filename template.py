# Template for Vehicle Insurance Data Pipeline ML Ops
import os
from pathlib import Path


# Author: Shalin Vachheta
# Date:14/12/2025
# Description: This script serves as a template for building a data pipeline and ML workflow for vehicle insurance data.

# Define the main project directory name
project_name ="src"

# List of files and directories to be created for the ML Ops project structure
list_of_files = [
    
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/configuration/mongo_db_connection.py" ,
    f"{project_name}/configuration/aws_connection.py",
    f"{project_name}/cloud_storage/__init__.py",
    f"{project_name}/cloud_storage/aws_storage.py",
    f"{project_name}/data_access/__init__.py",
    f"{project_name}/data_access/proj1_data.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/entity/estimator.py",
    f"{project_name}/entity/s3_estimator.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipline/__init__.py",
    f"{project_name}/pipline/training_pipeline.py",
    f"{project_name}/pipline/prediction_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    "app.py",
    "requirements.txt",
    "Dockerfile",
    "setup.py",
    "demo.py",
    "pyproject.toml",
    "config/model.yaml",
    "config/scema.yaml",
]

# Create the directories and files as specified in the list
for filepath in list_of_files:
    # Convert the filepath string to a Path object for easier manipulation
    filepath = Path(filepath)
    # Split the filepath into directory and filename
    filedir, filename = os.path.split(filepath)
    # If there is a directory part, create it if it doesn't exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        print(f"Creating directory: {filedir} for file: {filename}")
    # If the file doesn't exist or is empty, create it
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        print(f"Creating file: {filepath}")
    else:
        print(f"File already exists: {filepath}")