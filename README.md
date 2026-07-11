# 🏦 Credit Risk Decision Engine

A production-oriented **Machine Learning Engineering** project for predicting borrower default risk using a trained **Gradient Boosting Classifier**. This project demonstrates how to transform a traditional data science model into a modular, scalable, and maintainable machine learning system following software engineering and MLOps best practices.

---

## 📖 Project Overview

This project predicts the likelihood that a borrower will default on a loan based on historical financial information.

Unlike a typical machine learning notebook, this repository focuses on building a **production-ready credit risk decision engine** by separating the application into reusable modules for configuration, preprocessing, prediction, testing, and future deployment.

This repository is being developed incrementally to demonstrate the complete journey from **Data Science** to **Machine Learning Engineering** and eventually **MLOps**.

---

## 🚀 Current Features

- ✅ Gradient Boosting Credit Risk Model
- ✅ Modular Project Architecture
- ✅ Model Loading Service
- ✅ Input Preprocessing Module
- ✅ Prediction Service
- ✅ Unit Tests
- ✅ Git Version Control
- ✅ Professional Project Structure

---

## 🚧 Features In Progress

- Risk Classification Engine
- Business Rule Engine
- Explainable AI (SHAP)
- Decision Recommendation Engine
- Exception Handling
- Logging
- Configuration Management

---

## 📅 Planned Features

- FastAPI REST API
- Streamlit Dashboard
- Docker Containerization
- MLflow Experiment Tracking
- GitHub Actions CI/CD
- Model Monitoring
- Data Drift Detection
- Cloud Deployment

---

# 🏗 System Architecture

```text
                   User
                     │
                     ▼
              Streamlit / API
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
             SHAP Explainer
                     │
                     ▼
          Business Rules Engine
                     │
                     ▼
             Final Decision
```

---

# 📂 Project Structure

```text
credit-risk-mlops/
│
├── app/                    # Application entry point
├── data/
│   ├── raw/
│   └── processed/
│
├── docs/
│
├── models/
│
├── notebooks/
│
├── src/
│   ├── config.py
│   ├── model_loader.py
│   ├── preprocessing.py
│   ├── predictor.py
│   └── ...
│
├── tests/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone git@github.com:odugbile1993/credit-risk-mlops.git
```

Navigate into the project

```bash
cd credit-risk-mlops
```

Create a virtual environment

```bash
python3 -m venv venv
```

Activate the environment

macOS / Linux

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running Tests

Configuration Test

```bash
python -m tests.test_config
```

Model Loader Test

```bash
python -m tests.test_model_loader
```

Prediction Pipeline Test

```bash
python -m tests.test_predictor
```

---

# 🧠 Machine Learning Model

Current model:

- Gradient Boosting Classifier

Primary objective:

- Predict borrower default probability

Current output:

- Default Prediction
- Default Probability

Future outputs:

- Risk Band
- Business Decision
- SHAP Explanation
- Lending Recommendation

---

# 🛣 Development Roadmap

## Phase 1 — Foundation ✅

- Project Structure
- Configuration Module
- Model Loader
- Preprocessing
- Prediction Pipeline

---

## Phase 2 — Backend Engineering 🚧

- Risk Engine
- Business Rules
- SHAP Integration
- Utility Functions
- Exception Handling

---

## Phase 3 — API Development

- FastAPI
- Swagger Documentation
- REST Endpoints

---

## Phase 4 — Frontend

- Streamlit Dashboard
- Interactive Prediction Interface
- SHAP Visualizations

---

## Phase 5 — MLOps

- Docker
- MLflow
- GitHub Actions
- Automated Testing
- Monitoring
- Deployment

---

# 🎯 Learning Objectives

This project demonstrates practical skills in:

- Machine Learning Engineering
- Software Engineering
- Python Packaging
- Clean Architecture
- Model Deployment
- Explainable AI
- API Development
- Testing
- Version Control
- MLOps

---

# 🤝 Contributing

Contributions, ideas, and suggestions are welcome.

Feel free to fork the repository, submit issues, or open pull requests.

---

# 👨‍💻 Author

**Ayodele Odugbile**

Machine Learning Engineer | Data Scientist | AI Researcher

GitHub:
https://github.com/odugbile1993

LinkedIn:
(https://www.linkedin.com/in/ayodele-odugbile-939b97185/)

---

# ⭐ Repository Status

**Current Version:** v0.1.0

This repository is actively under development as part of a complete Machine Learning Engineering and MLOps learning journey.
