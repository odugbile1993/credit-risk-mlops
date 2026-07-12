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

# ==========================
# Risk Classification Thresholds
# ==========================

LOW_RISK_THRESHOLD = 0.20

MEDIUM_RISK_THRESHOLD = 0.50

# ==================================================
# Business Rule Thresholds
# ==================================================

MIN_MONTHLY_INCOME = 1000

LOW_INCOME_THRESHOLD = 2000

HIGH_DEBT_RATIO = 5

MAX_REVOLVING_UTILIZATION = 1

SEVERE_DELINQUENCY_THRESHOLD = 3

YOUNG_BORROWER_AGE = 21