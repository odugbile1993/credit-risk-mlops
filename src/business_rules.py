"""
Business policy engine.

This module evaluates borrower information against
credit policy rules and returns policy alerts.
"""

from src.schemas import Borrower
from src.config import (
    HIGH_DEBT_RATIO,
    LOW_INCOME_THRESHOLD,
    MAX_REVOLVING_UTILIZATION,
    MIN_MONTHLY_INCOME,
    SEVERE_DELINQUENCY_THRESHOLD,
    YOUNG_BORROWER_AGE,
)


def check_credit_policy(borrower: Borrower) -> list[dict]:
    """
    Evaluate borrower information against
    internal credit policy.

    Parameters
    ----------
    borrower : Borrower
        Borrower information.

    Returns
    -------
    list[dict]
        List of policy alerts.
    """

    alerts = []

    # ==================================================
    # Rule 1 - Zero Income
    # ==================================================
    if borrower.monthly_income <= 0:
        alerts.append(
            {
                "icon": "🚨",
                "severity": "critical",
                "title": "Zero Income Detected",
                "reason": (
                    "Borrower reports no monthly income. "
                    "Manual review is strongly recommended."
                ),
            }
        )

    # ==================================================
    # Rule 2 - Low Income With Dependents
    # ==================================================
    if (
        borrower.monthly_income < MIN_MONTHLY_INCOME
        and borrower.dependents > 0
    ):
        alerts.append(
            {
                "icon": "🚨",
                "severity": "critical",
                "title": "Insufficient Income",
                "reason": (
                    "Borrower income may be inadequate "
                    "to support existing dependents."
                ),
            }
        )

    # ==================================================
    # Rule 3 - Elevated Credit Utilization
    # ==================================================
    if (
        borrower.revolving_utilization
        > MAX_REVOLVING_UTILIZATION
    ):
        alerts.append(
            {
                "icon": "⚠",
                "severity": "warning",
                "title": "Elevated Credit Utilization",
                "reason": (
                    "Credit utilization exceeds 100%, "
                    "indicating potential financial stress."
                ),
            }
        )

    # ==================================================
    # Rule 4 - Severe Delinquencies
    # ==================================================
    if (
        borrower.times_90_days_late
        >= SEVERE_DELINQUENCY_THRESHOLD
    ):
        alerts.append(
            {
                "icon": "⚠",
                "severity": "warning",
                "title": "Severe Delinquency History",
                "reason": (
                    "Repeated 90-day delinquencies "
                    "increase repayment risk."
                ),
            }
        )

    # ==================================================
    # Rule 5 - Income vs Dependents
    # ==================================================
    if (
        borrower.monthly_income < LOW_INCOME_THRESHOLD
        and borrower.dependents > 2
    ):
        alerts.append(
            {
                "icon": "⚠",
                "severity": "warning",
                "title": "Income-to-Dependent Imbalance",
                "reason": (
                    "Monthly income may be insufficient "
                    "for household obligations."
                ),
            }
        )

    # ==================================================
    # Rule 6 - High Debt Ratio
    # ==================================================
    if borrower.debt_ratio > HIGH_DEBT_RATIO:
        alerts.append(
            {
                "icon": "⚠",
                "severity": "warning",
                "title": "High Leverage Exposure",
                "reason": (
                    "Debt obligations are unusually high "
                    "relative to borrower capacity."
                ),
            }
        )

    # ==================================================
    # Rule 7 - Young Borrower
    # ==================================================
    if borrower.age < YOUNG_BORROWER_AGE:
        alerts.append(
            {
                "icon": "ℹ",
                "severity": "info",
                "title": "Additional Assessment Recommended",
                "reason": (
                    "Limited credit history may "
                    "affect risk evaluation."
                ),
            }
        )

    return alerts