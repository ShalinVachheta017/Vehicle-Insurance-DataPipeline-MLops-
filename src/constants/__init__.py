"""
Initializes the constants package for the Vehicle Insurance Data Pipeline MLOps project.

This file centralizes all project-wide constants + environment-driven config
(MongoDB, AWS, app host/port, artifact paths, etc.).
"""

# src/constants/__init__.py

import os
from datetime import date
from dotenv import load_dotenv

# -----------------------------------------------------------------------------
# 1) Load environment variables
# -----------------------------------------------------------------------------
# Reads key=value pairs from a local ".env" file (if present) and merges them
# into the process environment. In Docker/EC2, env vars can also come from
# `docker run -e ...` or GitHub Actions.
load_dotenv()

# -----------------------------------------------------------------------------
# 2) Database (MongoDB) constants
# -----------------------------------------------------------------------------
# MongoDB DB + collection names used throughout ingestion/training/prediction.
DATABASE_NAME = "Vehicle-Insurance"
COLLECTION_NAME = "Vehicle-Insurance-Data"

# IMPORTANT:
# Previously you used `MONGODB_URL_KEY`. Keep it for backward compatibility,
# but also expose `MONGODB_URL` because code often expects that exact name.
MONGODB_URL = os.getenv("MONGODB_URL", "")
MONGODB_URL_KEY = MONGODB_URL  # backward compatible alias

# -----------------------------------------------------------------------------
# 3) Artifact / pipeline constants
# -----------------------------------------------------------------------------
PIPELINE_NAME: str = ""                 # optional pipeline name if you use one
ARTIFACT_DIR: str = "artifact"          # root folder where pipeline artifacts are stored

MODEL_FILE_NAME = "model.pkl"           # final trained model filename
TARGET_COLUMN = "Response"              # target label column in dataset
CURRENT_YEAR = date.today().year

PREPROCSSING_OBJECT_FILE_NAME = "preprocessing.pkl"  # saved preprocessing pipeline

FILE_NAME: str = "data.csv"
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"
SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml")
# -----------------------------------------------------------------------------
# 4) AWS credentials (IMPORTANT: keep *_ENV_KEY as the ENV VAR NAME, not value)
# -----------------------------------------------------------------------------

# These are the environment variable NAMES (keys)
AWS_ACCESS_KEY_ID_ENV_KEY = "AWS_ACCESS_KEY_ID"
AWS_SECRET_ACCESS_KEY_ENV_KEY = "AWS_SECRET_ACCESS_KEY"
AWS_DEFAULT_REGION_ENV_KEY = "AWS_DEFAULT_REGION"

# These are the actual values read from environment at runtime
AWS_ACCESS_KEY_ID = os.getenv(AWS_ACCESS_KEY_ID_ENV_KEY, "")
AWS_SECRET_ACCESS_KEY = os.getenv(AWS_SECRET_ACCESS_KEY_ENV_KEY, "")
AWS_DEFAULT_REGION = os.getenv(AWS_DEFAULT_REGION_ENV_KEY, "us-east-1")

# Backward compatible aliases (if your old code uses REGION_NAME)
REGION_NAME = AWS_DEFAULT_REGION


# -----------------------------------------------------------------------------
# 5) Data ingestion constants
# -----------------------------------------------------------------------------
# Data Ingestion related constant start with DATA_INGESTION VAR NAME
DATA_INGESTION_COLLECTION_NAME: str = "Vehicle-Insurance-Data"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.25

# -----------------------------------------------------------------------------
# 6) Data validation constants
# -----------------------------------------------------------------------------
# Data Validation related constant start with DATA_VALIDATION VAR NAME
DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_REPORT_FILE_NAME: str = "report.yaml"

# -----------------------------------------------------------------------------
# 7) Data transformation constants
# -----------------------------------------------------------------------------
# Data Transformation related constant start with DATA_TRANSFORMATION VAR NAME
DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR: str = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR: str = "transformed_object"

# -----------------------------------------------------------------------------
# 8) Model trainer constants
# -----------------------------------------------------------------------------
# MODEL TRAINER related constant start with MODEL_TRAINER var name
MODEL_TRAINER_DIR_NAME: str = "model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR: str = "trained_model"
MODEL_TRAINER_TRAINED_MODEL_NAME: str = "model.pkl"
MODEL_TRAINER_EXPECTED_SCORE: float = 0.6
MODEL_TRAINER_MODEL_CONFIG_FILE_PATH: str = os.path.join("config", "model.yaml")

# Model hyperparameters
MODEL_TRAINER_N_ESTIMATORS = 300
MODEL_TRAINER_MIN_SAMPLES_SPLIT: int = 7
MODEL_TRAINER_MIN_SAMPLES_LEAF: int = 6
MIN_SAMPLES_SPLIT_MAX_DEPTH: int = 10
MIN_SAMPLES_SPLIT_CRITERION: str = "entropy"
MIN_SAMPLES_SPLIT_RANDOM_STATE: int = 101

# -----------------------------------------------------------------------------
# 9) Model evaluation + model registry constants
# -----------------------------------------------------------------------------
MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE: float = 0.02

# S3 bucket + key where you push/load models (model registry)
MODEL_BUCKET_NAME = "vehicle-insurance-mlops-ytproject"
MODEL_PUSHER_S3_KEY = "model-registry"

# -----------------------------------------------------------------------------
# 10) App constants (host/port)
# -----------------------------------------------------------------------------
# Keep these as defaults, but ALSO allow override from env so Docker/EC2 can control it.
APP_HOST = os.getenv("APP_HOST", "0.0.0.0")
APP_PORT = int(os.getenv("APP_PORT", "5000"))
