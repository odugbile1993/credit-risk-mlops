"""
Central configuration for the Credit Risk MLOps project.
"""

from pathlib import Path

# -----------------------------------------------------
# Project Root
# -----------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# -----------------------------------------------------
# Data
# -----------------------------------------------------

DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

TRAIN_DATA_PATH = RAW_DATA_DIR / "project_train_data.csv"

# -----------------------------------------------------
# Models
# -----------------------------------------------------

MODELS_DIR = PROJECT_ROOT / "models"
MODEL_PATH = MODELS_DIR / "credit_risk_gradient_boosting_model.pkl"

# -----------------------------------------------------
# Other Directories
# -----------------------------------------------------

NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"
DOCS_DIR = PROJECT_ROOT / "docs"
TESTS_DIR = PROJECT_ROOT / "tests"