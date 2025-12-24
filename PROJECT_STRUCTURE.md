
# Vehicle Insurance Data Pipeline - MLOps Project

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8+-green.svg)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](Dockerfile)

This document provides a comprehensive overview of the **Vehicle-Insurance-DataPipeline-MLops-** project, an end-to-end MLOps solution for building, deploying, and monitoring machine learning models for vehicle insurance prediction.

---

## 📋 Table of Contents

- [Project Overview](#-project-overview)
- [Architecture](#-architecture)
- [Prerequisites & Dependencies](#-prerequisites--dependencies)
- [Installation & Setup](#-installation--setup)
- [Project Structure](#-project-structure)
- [Pipeline Flow](#-pipeline-flow)
- [Stage-wise Pipeline Details](#-stage-wise-pipeline-details)
- [Code Structure](#-code-structure)
- [Usage](#-usage)
- [Testing](#-testing)
- [Deployment](#-deployment)
- [Monitoring & Logging](#-monitoring--logging)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 Project Overview

### Purpose
The Vehicle Insurance Data Pipeline is a production-ready MLOps framework designed to automate the machine learning lifecycle for predicting vehicle insurance claims. It implements best practices in data engineering, model training, evaluation, and deployment using cloud-native technologies.

### Key Features
- **Modular Pipeline**: Each stage is independent and testable.
- **Cloud Integration**: Seamless integration with AWS S3 for storage and deployment.
- **Data Validation**: Automated schema validation and data quality checks.
- **Model Versioning**: Version control for models and artifacts.
- **Scalable Architecture**: Designed for production workloads.
- **Monitoring**: Comprehensive logging and error handling.

### Use Case
This project predicts vehicle insurance claim probabilities based on historical data, enabling insurers to assess risk and set premiums more accurately.

### Technologies Used
- **Programming Language**: Python 3.8+
- **ML Framework**: Scikit-learn, Pandas, NumPy
- **Cloud Storage**: AWS S3
- **Database**: MongoDB
- **Containerization**: Docker
- **Version Control**: Git
- **CI/CD**: (Optional) GitHub Actions

---

## 🏗️ Architecture

The project follows a layered architecture:

```
┌─────────────────┐
│   Application   │  (app.py, demo.py)
├─────────────────┤
│   Pipeline      │  (training_pipeline.py, prediction_pipeline.py)
├─────────────────┤
│   Components    │  (data_ingestion, validation, etc.)
├─────────────────┤
│   Services      │  (cloud_storage, data_access, etc.)
├─────────────────┤
│   Utilities     │  (logger, exception, utils)
├─────────────────┤
│   Configuration │  (config/, constants/)
└─────────────────┘
```

### Data Flow
1. Raw data → MongoDB
2. Ingestion → Validation → Transformation
3. Training → Evaluation → Deployment
4. Artifacts → S3 Storage

---

## 📦 Prerequisites & Dependencies

### System Requirements
- Python 3.8 or higher
- Docker (for containerized deployment)
- AWS CLI configured with appropriate permissions
- MongoDB instance (local or cloud)

### Python Dependencies
See `requirements.txt` for full list. Key packages:
- `pandas`, `numpy`, `scikit-learn`
- `boto3` (AWS SDK)
- `pymongo` (MongoDB driver)
- `imbalanced-learn` (SMOTEENN)
- `pyyaml` (Configuration)

---

## 🚀 Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd Vehicle-Insurance-DataPipeline-MLops-
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment**
   - Copy `.env.example` to `.env`
   - Set AWS credentials and MongoDB URI
   - Update `config/model.yaml` and `config/schema.yaml`

5. **Run Setup**
   ```bash
   python setup.py install
   ```

---

## 📁 Root Files

| File                    | Description                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| **app.py**              | Main application entry point; orchestrates the ML pipeline.                 |
| **check_s3_bucket.py**  | Checks the status or existence of an S3 bucket.                             |
| **check_s3_versions.py**| Checks versions of objects in an S3 bucket.                                 |
| **crashcourse.txt**     | Notes or crash course summary.                                              |
| **demo.py**             | Demo script for running/testing the pipeline.                               |
| **Dockerfile**          | Docker image build instructions.                                            |
| **LICENSE**             | Project license.                                                            |
| **project_flow.txt**    | Describes the project workflow.                                             |
| **pyproject.toml**      | Python packaging and dependency configuration.                              |
| **README.md**           | Main project documentation and usage instructions.                          |
| **requirements.txt**    | List of Python dependencies.                                                |
| **setup.py**            | Script for installing the project as a package.                             |
| **template.py**         | Template for new modules/scripts.                                           |
| **test_aws_connection.py** | Tests AWS connection and credentials.                                    |
| **workflow.txt**        | Workflow steps in text format.                                              |

---

## 📂 Key Folders

| Folder         | Description                                                                                  |
|----------------|---------------------------------------------------------------------------------------------|
| **artifact/**  | Stores output artifacts from pipeline runs, organized by timestamp and stage.                |
| **build/**     | Build artifacts, including compiled files and source distributions.                          |
| **config/**    | Configuration files (e.g., model.yaml, schema.yaml).                                         |
| **logs/**      | Log files generated by the application.                                                      |
| **notebook/**  | Jupyter notebooks and data files for experimentation and analysis.                           |
| **src/**       | Main source code, organized into submodules (see below for details).                         |
| **src.egg-info/** | Metadata for the installed package.                                                      |

---

## 📦 Source Code Structure (`src/`)

- **cloud_storage/**: Utilities for interacting with cloud storage (e.g., AWS S3).
- **components/**: Core pipeline components:
  - `data_ingestion.py`: Loads data from MongoDB to feature store.
  - `data_validation.py`: Validates data schema and integrity.
  - `data_transformation.py`: Transforms and preprocesses data.
  - `model_trainer.py`: Trains machine learning models.
  - `model_evaluation.py`: Evaluates trained models.
  - `model_pusher.py`: Pushes models to deployment targets.
- **configuration/**: Configuration management (e.g., MongoDB connection).
- **constants/**: Project-wide constants (e.g., file paths, column names).
- **data_access/**: Data access layer for reading/writing data.
- **entity/**: Entity definitions for configuration and artifacts.
- **exception/**: Custom exception classes.
- **logger/**: Logging utilities.
- **pipline/**: Pipeline orchestration (training and prediction).
- **utils/**: Utility functions (e.g., file I/O, helpers).

---


## 🗺️ Pipeline Flow (Mermaid Diagram)

```mermaid
flowchart TD
    A[Start: app.py/demo.py] --> B[data_ingestion.py\n(Data Ingestion)]
    B --> C[data_validation.py\n(Data Validation)]
    C --> D[data_transformation.py\n(Data Transformation)]
    D --> E[model_trainer.py\n(Model Training)]
    E --> F[model_evaluation.py\n(Model Evaluation)]
    F --> G[model_pusher.py\n(Model Pushing)]
    G --> H[Artifacts Saved to S3]
    H --> I[End]
```

---


## 🔎 Stage-wise Pipeline Details

### 0. Configuration & Initialization
- **Purpose:** Sets up all configuration, constants, and logging for the pipeline.
- **Key Steps:**
  - Loads configuration files (YAML, TOML, etc.).
  - Sets up logging and exception handling.
  - Defines constants and environment variables.
- **Artifacts Produced:**
  - Configuration objects
  - Log files

### 1. Data Ingestion (`data_ingestion.py`)
- **Purpose:** Loads raw data from MongoDB (or other sources) and saves it to a feature store (CSV or DataFrame).
- **Key Steps:**
  - Connects to MongoDB using configuration.
  - Exports the specified collection as a DataFrame.
  - Saves the raw data to a local feature store directory.
  - Splits the data into train and test sets.
- **Artifacts Produced:**
  - Raw data file
  - Train and test data files
  - DataIngestionArtifact (metadata about the ingestion)
- **Technical Details:** Uses `Proj1Data` class for MongoDB interaction, supports configurable collection names.

### 2. Data Validation (`data_validation.py`)
- **Purpose:** Ensures the ingested data meets schema and quality requirements.
- **Key Steps:**
  - Loads the schema definition (from YAML).
  - Checks number and names of columns.
  - Validates data types and missing values.
  - Optionally, checks for data drift or anomalies.
- **Artifacts Produced:**
  - Validation report (JSON/YAML)
  - DataValidationArtifact (validation results and paths)
- **Technical Details:** Schema validation against predefined YAML config, raises exceptions on failure.

### 3. Data Transformation (`data_transformation.py`)
- **Purpose:** Prepares data for modeling by applying feature engineering and preprocessing.
- **Key Steps:**
  - Loads train and test data.
  - Applies transformations (e.g., scaling, encoding, imputation).
  - Handles class imbalance (e.g., SMOTEENN).
  - Saves transformed arrays and transformation objects (e.g., pipeline, scaler).
- **Artifacts Produced:**
  - Transformed train and test arrays
  - Preprocessing pipeline object
  - DataTransformationArtifact (metadata and paths)
- **Technical Details:** Uses Scikit-learn pipelines for reproducibility, supports numerical and categorical features.

### 4. Model Training (`model_trainer.py`)
- **Purpose:** Trains a machine learning model using the transformed data.
- **Key Steps:**
  - Loads transformed data and pipeline.
  - Trains a classifier (e.g., RandomForest).
  - Evaluates on validation/test set (accuracy, F1, etc.).
  - Saves the trained model and metrics.
- **Artifacts Produced:**
  - Trained model file
  - Training metrics report
  - ModelTrainerArtifact (model path, metrics)
- **Technical Details:** Configurable hyperparameters, supports multiple algorithms via estimator classes.

### 5. Model Evaluation (`model_evaluation.py`)
- **Purpose:** Compares the newly trained model with the best/production model.
- **Key Steps:**
  - Loads the new and best (previous) models.
  - Evaluates both on a holdout/test set.
  - Compares metrics (e.g., F1 score).
  - Decides if the new model should be promoted.
- **Artifacts Produced:**
  - Evaluation report (comparison)
  - ModelEvaluationArtifact (accept/reject decision)
- **Technical Details:** Uses S3Estimator for loading production models, threshold-based acceptance.

### 6. Model Pushing (`model_pusher.py`)
- **Purpose:** Deploys/promotes the accepted model to a production location (e.g., S3 bucket).
- **Key Steps:**
  - Uploads the model and related artifacts to cloud storage (S3).
  - Updates model registry or deployment pointer.
- **Artifacts Produced:**
  - ModelPusherArtifact (deployment metadata)
  - Model and pipeline objects in S3/production
- **Technical Details:** Integrates with SimpleStorageService for S3 operations, supports versioning.

### 7. Monitoring & Logging (Optional, via `logger/`, `logs/`)
- **Purpose:** Tracks pipeline execution, errors, and performance for debugging and auditing.
- **Key Steps:**
  - Logs each stage's start, end, and errors.
  - Stores logs in the `logs/` directory.
  - Optionally, sends alerts or metrics to monitoring tools.
- **Artifacts Produced:**
  - Log files
  - Monitoring reports (if implemented)

### 8. Artifact Management (via `artifact/`)
- **Purpose:** Stores all intermediate and final outputs for reproducibility and traceability.
- **Key Steps:**
  - Organizes artifacts by timestamp and stage.
  - Stores raw, processed, and model files.
  - Maintains metadata for each run.
- **Artifacts Produced:**
  - All pipeline artifacts (data, models, reports)

### 9. Utilities & Helpers (via `utils/`, `constants/`, etc.)
- **Purpose:** Provides reusable functions, constants, and helpers for all pipeline stages.
- **Key Steps:**
  - File I/O, YAML/JSON reading, saving/loading models.
  - Common error handling and utility functions.
- **Artifacts Produced:**
  - Utility modules
  - Helper scripts

---

## 🏗️ Code Structure Example

```plaintext
src/
├── cloud_storage/
│   └── aws_storage.py          # AWS S3 utilities
├── components/
│   ├── data_ingestion.py       # Data loading from MongoDB
│   ├── data_validation.py      # Schema and quality validation
│   ├── data_transformation.py  # Feature engineering
│   ├── model_trainer.py        # ML model training
│   ├── model_evaluation.py     # Model comparison
│   └── model_pusher.py         # Model deployment
├── configuration/
│   └── mongo_db_connection.py  # DB connection setup
├── constants/
│   └── __init__.py             # Project constants
├── data_access/
│   └── proj1_data.py           # Data access layer
├── entity/
│   ├── artifact_entity.py      # Artifact definitions
│   ├── config_entity.py        # Config entities
│   ├── estimator.py            # Model estimators
│   └── s3_estimator.py         # S3-based estimators
├── exception/
│   └── __init__.py             # Custom exceptions
├── logger/
│   └── __init__.py             # Logging setup
├── pipline/
│   ├── training_pipeline.py    # Training orchestration
│   └── prediction_pipeline.py  # Prediction pipeline
└── utils/
    └── main_utils.py           # Utility functions
```

---

## � Usage

### Running the Pipeline
```bash
# Run training pipeline
python demo.py

# Check S3 bucket
python check_s3_bucket.py

# Test AWS connection
python test_aws_connection.py
```

### API Usage
```python
from src.pipline.training_pipeline import TrainPipeline

pipeline = TrainPipeline()
pipeline.run_pipeline()
```

---

## 🧪 Testing

- Unit tests for each component in `tests/` (if available).
- Integration tests for end-to-end pipeline.
- Run tests: `python -m pytest`

---

## 🚀 Deployment

### Docker
```bash
docker build -t vehicle-insurance-mlops .
docker run vehicle-insurance-mlops
```

### Cloud Deployment
- Deploy to AWS ECS/Fargate
- Use S3 for artifact storage
- Integrate with CI/CD pipelines

---

## 📊 Monitoring & Logging

- Logs stored in `logs/` directory
- Structured logging with timestamps
- Error tracking and alerting (optional)

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make changes and add tests
4. Submit a pull request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

*For more information, contact the development team or refer to the README.md.*