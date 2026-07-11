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

                Streamlit
                     │
                     ▼
              preprocessing.py
                     │
                     ▼
               predictor.py
                     │
                     ▼
             model_loader.py
                     │
                     ▼
       Gradient Boosting Model
                     │
                     ▼
                 SHAP Engine
                     │
                     ▼
             Business Rules
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
