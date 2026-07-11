# Credit Risk Decision Engine

Production-ready machine learning system for predicting borrower default risk.

## Features

- Gradient Boosting Model
- Explainable AI (SHAP)
- Credit Policy Engine
- Risk Classification
- REST API
- Streamlit Dashboard
- Docker
- MLflow
- CI/CD

## Architecture
                User
                  │
                  ▼
        Streamlit / FastAPI
                  │
                  ▼
        preprocessing.py
                  │
                  ▼
          predictor.py
                  │
          ┌───────┴────────┐
          ▼                ▼
 model_loader.py      explainer.py
          │                │
          ▼                ▼
 Gradient Boosting      SHAP
          │                │
          └───────┬────────┘
                  ▼
        business_rules.py
                  │
                  ▼
          Final Decision
             
## Project Structure

src/
tests/
models/
...

## Installation

...

## Roadmap

...
