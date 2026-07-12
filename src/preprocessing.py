"""
Input preprocessing utilities.

This module converts a Borrower object into
the DataFrame format expected by the ML model.
"""

import pandas as pd

from src.schemas import Borrower


def prepare_input(borrower: Borrower) -> pd.DataFrame:
    """
    Convert borrower information into
    a model-ready DataFrame.
    """

    return pd.DataFrame(
        {
            "RevolvingUtilizationOfUnsecuredLines": [
                borrower.revolving_utilization
            ],
            "age": [borrower.age],
            "NumberOfTime30-59DaysPastDueNotWorse": [
                borrower.past_due_30_59
            ],
            "DebtRatio": [borrower.debt_ratio],
            "MonthlyIncome": [borrower.monthly_income],
            "NumberOfOpenCreditLinesAndLoans": [
                borrower.open_credit_lines
            ],
            "NumberOfTimes90DaysLate": [
                borrower.times_90_days_late
            ],
            "NumberRealEstateLoansOrLines": [
                borrower.real_estate_loans
            ],
            "NumberOfTime60-89DaysPastDueNotWorse": [
                borrower.past_due_60_89
            ],
            "NumberOfDependents": [borrower.dependents],
        }
    )