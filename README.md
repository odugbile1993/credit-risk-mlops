# 🚀 OpenFraudLabs Credit Decision Intelligence Platform

> **An Explainable AI-powered Credit Risk Decision Engine built with Machine Learning, MLOps, and Business Decision Intelligence.**

![Python](https://img.shields.io/badge/Python-3.12-blue)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange)
![CatBoost](https://img.shields.io/badge/CatBoost-Supported-green)
![Gradient%20Boosting](https://img.shields.io/badge/GradientBoosting-Champion-success)
![SHAP](https://img.shields.io/badge/Explainability-SHAP-red)
![MLOps](https://img.shields.io/badge/MLOps-Production-black)
![Status](https://img.shields.io/badge/Status-Beta-yellow)

---

## 📖 Overview

OpenFraudLabs Credit Decision Intelligence Platform is an end-to-end Machine Learning system designed to support smarter credit decisions through explainable AI, business rule automation, and risk analytics.

Unlike traditional credit scoring systems that focus solely on prediction, this platform combines:

- Machine Learning
- Explainable AI (SHAP)
- Business Rules
- Decision Intelligence
- Model Benchmarking
- Threshold Optimization
- Feature Engineering

to provide transparent, business-driven lending recommendations.

The project is being developed as the foundation of the OpenFraudLabs AI platform.

# ✨ Current Capabilities

## 🤖 Machine Learning

- Gradient Boosting Model
- Random Forest
- Logistic Regression
- CatBoost
- Model Registry
- Model Benchmarking

---

## 🧠 Explainable AI

- SHAP Explanations
- Human-readable predictions
- Feature contribution analysis

---

## 📈 Business Intelligence

- Credit Risk Bands
- Decision Engine
- Policy Alerts
- Threshold Optimization
- Manual Review Recommendation

---

## ⚙️ MLOps

- Modular Architecture
- Reusable Components
- Configuration Management
- Testing Framework
- Production-ready Project Structure

---

## 📊 Feature Engineering

- Income per Dependent
- Estimated Monthly Debt
- Disposable Income
- Delinquency Score
- Utilization Band
- Age Band

# 💼 Business Impact

This platform focuses on improving lending decisions rather than simply improving model accuracy.

Recent experimentation demonstrated that:

- Recall improved from **20.32% → 51.36%**
- High-risk borrower detection increased by **153%**
- Achieved without retraining the underlying model
- Implemented using Threshold Optimization
  
This demonstrates how decision policy optimization can generate significant business value while reducing potential loan losses.

# 🏗️ System Architecture

```text
                        +----------------------+
                        |   Borrower Input     |
                        +----------+-----------+
                                   |
                                   v
                    +----------------------------+
                    | Feature Engineering Layer  |
                    +-------------+--------------+
                                  |
                                  v
                     +---------------------------+
                     | Machine Learning Model    |
                     | (Gradient Boosting)       |
                     +-------------+-------------+
                                   |
                                   v
                    +----------------------------+
                    | Prediction Service         |
                    +-------------+--------------+
                                  |
                    +-------------+--------------+
                    |                            |
                    v                            v
        +----------------------+      +----------------------+
        | Business Rule Engine |      | SHAP Explainability  |
        +----------+-----------+      +----------+-----------+
                   |                             |
                   +-------------+---------------+
                                 |
                                 v
                   +-----------------------------+
                   | Decision Intelligence Layer |
                   +-------------+---------------+
                                 |
                                 v
                     +--------------------------+
                     | Final Lending Decision   |
                     | Approve                 |
                     | Manual Review           |
                     | Reject                  |
                     +--------------------------+

```

# 📂 Project Structure

```text
credit-risk-mlops/
│
├── app/                        # Future web application
│
├── data/
│   ├── raw/
│   └── processed/
│
├── docs/
│
├── models/
│   └── credit_risk_gradient_boosting_model.pkl
│
├── notebooks/
│
├── src/
│   ├── benchmark.py
│   ├── benchmark_runner.py
│   ├── business_rules.py
│   ├── config.py
│   ├── decision_engine.py
│   ├── evaluation_service.py
│   ├── explainer_service.py
│   ├── feature_engineering.py
│   ├── feature_mapper.py
│   ├── metrics.py
│   ├── model_loader.py
│   ├── model_registry.py
│   ├── predictor.py
│   ├── schemas.py
│   ├── threshold_optimizer.py
│   └── train.py
│
├── tests/
│
├── requirements.txt
│
└── README.md
```

# 📈 Current Model Performance

## Champion Model

| Metric | Value |
|---------|------:|
| Model | Gradient Boosting |
| ROC-AUC | **86.64%** |
| Precision | **38.64%** |
| Recall | **51.36%*** |

> *Recall achieved after Threshold Optimization using a 0.20 decision threshold.*

---

### Benchmark Results

| Model | Recall | ROC-AUC |
|---------|------:|------:|
| Logistic Regression | 4.15% | 70.68% |
| Random Forest | 19.18% | 84.07% |
| Gradient Boosting | **20.32%** | **86.64%** |
| CatBoost | 19.71% | 86.40% |

```

🚀 Core Features

✅ Machine Learning Credit Risk Prediction

✅ Explainable AI using SHAP

✅ Business Rule Engine

✅ Decision Intelligence Layer

✅ Human-readable Explanations

✅ Model Benchmarking

✅ Threshold Optimization

✅ Feature Engineering

✅ Policy Alerts

✅ Risk Band Classification

✅ Evaluation Service

✅ Modular MLOps Architecture

✅ Production-ready Codebase
```

# 🗺️ Development Roadmap

## ✅ Version 1.0 — Core Platform (Completed)

- [x] Credit Risk Prediction Engine
- [x] Gradient Boosting Model
- [x] Model Registry
- [x] Model Benchmarking Framework
- [x] Feature Engineering Pipeline
- [x] SHAP Explainability
- [x] Business Rule Engine
- [x] Decision Intelligence Layer
- [x] Threshold Optimization
- [x] Evaluation Service
- [x] Modular Project Architecture
- [x] Comprehensive Unit Tests

---

## 🚧 Version 1.1 — Model Improvement (In Progress)

- [ ] Hyperparameter Optimization
- [ ] Cross-Validation Pipeline
- [ ] Feature Selection
- [ ] Probability Calibration
- [ ] Cost-sensitive Learning
- [ ] Business Cost Simulation
- [ ] Automated Model Comparison Report

---

## 🚀 Version 2.0 — Production MLOps

- [ ] FastAPI REST API
- [ ] Docker Support
- [ ] CI/CD Pipeline
- [ ] Model Versioning
- [ ] MLflow Integration
- [ ] Model Monitoring
- [ ] Logging & Observability
- [ ] Configuration Profiles
- [ ] Automated Retraining Pipeline

---

## 🌐 Version 3.0 — OpenFraudLabs Platform

- [ ] Interactive Streamlit Dashboard
- [ ] Loan Portfolio Risk Dashboard
- [ ] Real-time Credit Decision API
- [ ] Explainable AI Dashboard
- [ ] User Authentication
- [ ] Admin Console
- [ ] Multi-model Deployment
- [ ] Cloud Deployment
- [ ] Public Documentation Portal

---

## 🔬 Long-Term Research

- [ ] Explainable AI Benchmarking
- [ ] Fairness & Bias Evaluation
- [ ] Drift Detection
- [ ] Graph-based Fraud Detection
- [ ] Generative AI Decision Assistant
- [ ] Large Language Model Integration
```
 📸 Example Workflow

Borrower Information

```
Age: 45
Monthly Income: $5,000
Debt Ratio: 0.42
Credit Utilization: 0.87
30–59 Day Late Payments: 2
Dependents: 3
```

↓

Feature Engineering

```
Income per Dependent
Estimated Monthly Debt
Disposable Income
Delinquency Score
Utilization Band
Age Band
```

↓

Machine Learning Prediction

```
Default Probability: 24%
```

↓

Business Rules

```
✓ Medium Risk

✓ Manual Review Required
```

↓

Explainable AI

```
Top Risk Drivers

• High Credit Utilization

• Previous Late Payments

• High Debt Burden
```

↓

Final Recommendation
```

Manual Review
```


 🤝 Contributing

Contributions are welcome.

Whether you're interested in:

- Machine Learning
- Credit Risk Analytics
- MLOps
- Explainable AI
- Python Development
- Testing
- Documentation

feel free to open an issue or submit a pull request.

OpenFraudLabs aims to become a collaborative space for building practical AI systems that solve real business problems.
```
# 👨‍💻 About the Author

## Ayodele Odugbile

**Machine Learning Engineer | AI Researcher | Founder, OpenFraudLabs**

I build explainable AI systems and decision intelligence solutions focused on **Credit Risk, Fraud Detection, Explainable AI (XAI), MLOps, and Trustworthy AI**. My work bridges the gap between machine learning research and production-ready systems that deliver measurable business value.

As the founder of **OpenFraudLabs**, I'm building open, practical AI solutions for decision intelligence, AI data operations, and trustworthy machine learning. The long-term vision is to develop production-grade AI products while contributing research and open-source tools that advance responsible AI.

---
## 🌐 Connect with Me

<p align="left">
  <a href="https://www.openfraudlabs.com" target="_blank">
    <img src="https://img.shields.io/badge/OpenFraudLabs-Website-blue?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Website"/>
  </a>

  <a href="https://github.com/odugbile1993" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-Ayodele-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/>
  </a>

  <a href="https://www.linkedin.com/in/ayodele-odugbile-939b97185/" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-Ayodele_Odugbile-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/>
  </a>

  <a href="https://scholar.google.com/citations?user=xQu8Qf0AAAAJ&hl=en&authuser=1" target="_blank">
    <img src="https://img.shields.io/badge/Google-Scholar-4285F4?style=for-the-badge&logo=googlescholar&logoColor=white" alt="Google Scholar"/>
  </a>
</p>


