"""
Project data models.

These schemas define the objects exchanged
between different parts of the application.
"""

from dataclasses import dataclass


@dataclass
class Borrower:
    """
    Borrower information required
    for credit risk prediction.
    """

    revolving_utilization: float
    age: int
    past_due_30_59: int
    debt_ratio: float
    monthly_income: float
    open_credit_lines: int
    times_90_days_late: int
    real_estate_loans: int
    past_due_60_89: int
    dependents: int


@dataclass
class PredictionResult:
    """
    Machine learning prediction output.
    """

    prediction: int
    probability: float
    risk_band: str


@dataclass
class Alert:
    """
    Business policy alert.
    """

    rule_id: str
    category: str
    severity: str
    title: str
    reason: str
    icon: str

@dataclass
class Explanation:
    """
    Represents a single feature explanation.
    """

    feature: str
    contribution: float
    direction: str
    description: str
@dataclass
class DecisionReport:
    """
    Final credit decision report.
    """

    prediction: PredictionResult
    alerts: list[Alert]
    explanations: list[Explanation]
    recommendation: str
    approved: bool