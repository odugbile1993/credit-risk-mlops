"""
Feature Engineering Module.

Creates derived features to improve
credit risk model performance.
"""


def income_per_dependent(
    monthly_income: float,
    dependents: int,
) -> float:
    """
    Monthly income allocated per household member.

    Adds 1 to include the borrower.
    """

    return monthly_income / (dependents + 1)


def estimated_monthly_debt(
    debt_ratio: float,
    monthly_income: float,
) -> float:
    """
    Estimate the borrower's monthly debt obligations.

    DebtRatio in the dataset is already expressed
    as a proportion of income.
    """

    return debt_ratio * monthly_income


def disposable_income(
    monthly_income: float,
    debt_ratio: float,
) -> float:
    """
    Estimate disposable income after debt payments.
    """

    debt = estimated_monthly_debt(
        debt_ratio,
        monthly_income,
    )

    return monthly_income - debt


def delinquency_score(
    past_due_30_59: int,
    past_due_60_89: int,
    times_90_days_late: int,
) -> int:
    """
    Weighted delinquency score.

    Assigns increasing weights to more severe
    delinquency categories.
    """

    return (
        (1 * past_due_30_59)
        + (2 * past_due_60_89)
        + (3 * times_90_days_late)
    )


def utilization_band(
    revolving_utilization: float,
) -> str:
    """
    Categorize revolving credit utilization.
    """

    if revolving_utilization < 0.30:
        return "Low"

    elif revolving_utilization < 0.70:
        return "Medium"

    return "High"


def age_band(
    age: int,
) -> str:
    """
    Categorize borrower age.
    """

    if age < 25:
        return "Young"

    elif age < 50:
        return "Middle"

    return "Senior"