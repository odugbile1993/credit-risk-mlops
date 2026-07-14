# OpenFraudLabs Credit Decision Engine

## System Architecture

```text
Borrower
    │
    ▼
Evaluation Service
    │
 ┌──┼───────────────┐
 │  │               │
 ▼  ▼               ▼
Predictor   Business Rules   Explainability
 │              │                 │
 └──────────────┼─────────────────┘
                ▼
         Decision Engine
                ▼
         Decision Report
```

## Components

### Borrower

Represents the input schema required to evaluate a borrower.

### Evaluation Service

Acts as the orchestration layer responsible for coordinating the complete evaluation workflow.

### Predictor

Loads the trained machine learning model and generates predictions.

### Business Rules

Applies deterministic lending policies and generates alerts.

### Explainability Engine

Uses SHAP to identify the most influential features contributing to a prediction.

### Decision Engine

Combines predictions, business rules, and explanations to generate a final recommendation.

### Decision Report

Provides a single object containing:

- Prediction
- Probability
- Risk Band
- Alerts
- Explanations
- Recommendation
- Approval Status

## Design Principles

- Modular Architecture
- Explainable AI
- Testability
- Separation of Concerns
- Enterprise Readiness
- Extensibility

## Current Version

v0.3.0