"""
Business policy engine.

This module evaluates borrower information against
credit policy rules and returns policy alerts.
"""

from src.schemas import Borrower, Alert
from src.config import (
    HIGH_DEBT_RATIO,
    LOW_INCOME_THRESHOLD,
    MAX_REVOLVING_UTILIZATION,
    MIN_MONTHLY_INCOME,
    SEVERE_DELINQUENCY_THRESHOLD,
    YOUNG_BORROWER_AGE,
)


def check_credit_policy(borrower: Borrower) -> list[Alert]:
    """
    Evaluate borrower information against
    internal credit policy.

    Parameters
    ----------
    borrower : Borrower
        Borrower information.

    Returns
    -------
    list[Alert]
        List of policy alerts.
    """

    alerts = []

    # ==================================================
    # BR-001 - Zero Income
    # ==================================================
    if borrower.monthly_income <= 0:
        alerts.append(
            Alert(
                rule_id="BR-001",
                category="Financial Capacity",
                severity="critical",
                title="Zero Income Detected",
                reason=(
                    "Borrower reports no monthly income. "
                    "Manual review is strongly recommended."
                ),
                icon="🚨",
            )
        )

    # ==================================================
    # BR-002 - Low Income With Dependents
    # ==================================================
    if (
        borrower.monthly_income < MIN_MONTHLY_INCOME
        and borrower.dependents > 0
    ):
        alerts.append(
            Alert(
                rule_id="BR-002",
                category="Financial Capacity",
                severity="critical",
                title="Insufficient Income",
                reason=(
                    "Borrower income may be inadequate "
                    "to support existing dependents."
                ),
                icon="🚨",
            )
        )

    # ==================================================
    # BR-003 - Elevated Credit Utilization
    # ==================================================
    if (
        borrower.revolving_utilization
        > MAX_REVOLVING_UTILIZATION
    ):
        alerts.append(
            Alert(
                rule_id="BR-003",
                category="Credit Behaviour",
                severity="warning",
                title="Elevated Credit Utilization",
                reason=(
                    "Credit utilization exceeds 100%, "
                    "indicating potential financial stress."
                ),
                icon="⚠",
            )
        )

    # ==================================================
    # BR-004 - Severe Delinquency History
    # ==================================================
    if (
        borrower.times_90_days_late
        >= SEVERE_DELINQUENCY_THRESHOLD
    ):
        alerts.append(
            Alert(
                rule_id="BR-004",
                category="Credit Behaviour",
                severity="warning",
                title="Severe Delinquency History",
                reason=(
                    "Repeated 90-day delinquencies "
                    "increase repayment risk."
                ),
                icon="⚠",
            )
        )

    # ==================================================
    # BR-005 - Income-to-Dependent Imbalance
    # ==================================================
    if (
        borrower.monthly_income < LOW_INCOME_THRESHOLD
        and borrower.dependents > 2
    ):
        alerts.append(
            Alert(
                rule_id="BR-005",
                category="Financial Capacity",
                severity="warning",
                title="Income-to-Dependent Imbalance",
                reason=(
                    "Monthly income may be insufficient "
                    "for household obligations."
                ),
                icon="⚠",
            )
        )

    # ==================================================
    # BR-006 - High Leverage Exposure
    # ==================================================
    if borrower.debt_ratio > HIGH_DEBT_RATIO:
        alerts.append(
            Alert(
                rule_id="BR-006",
                category="Financial Capacity",
                severity="warning",
                title="High Leverage Exposure",
                reason=(
                    "Debt obligations are unusually high "
                    "relative to borrower capacity."
                ),
                icon="⚠",
            )
        )

    # ==================================================
    # BR-007 - Young Borrower
    # ==================================================
    if borrower.age < YOUNG_BORROWER_AGE:
        alerts.append(
            Alert(
                rule_id="BR-007",
                category="Borrower Profile",
                severity="info",
                title="Additional Assessment Recommended",
                reason=(
                    "Limited credit history may "
                    "affect risk evaluation."
                ),
                icon="ℹ"
            )
        )

    return alerts

