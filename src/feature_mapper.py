"""
Feature Knowledge Base.

Stores business-friendly names and explanation
templates for each model feature.
"""

FEATURE_INFO = {
    "RevolvingUtilizationOfUnsecuredLines": {
        "name": "Credit Utilization",
        "increase": (
            "High credit utilization increased the predicted default risk "
            "because the borrower is using a large proportion of available revolving credit."
        ),
        "decrease": (
            "Lower credit utilization reduced the predicted default risk, "
            "indicating responsible use of available credit."
        ),
    },

    "age": {
        "name": "Borrower Age",
        "increase": (
            "Borrower age contributed to a higher predicted default risk "
            "based on patterns learned from historical data."
        ),
        "decrease": (
            "Borrower age contributed to a lower predicted default risk "
            "based on historical repayment patterns."
        ),
    },

    "NumberOfTime30-59DaysPastDueNotWorse": {
        "name": "30-59 Day Late Payments",
        "increase": (
            "Recent late payment history increased the predicted default risk."
        ),
        "decrease": (
            "A strong recent repayment history reduced the predicted default risk."
        ),
    },

    "DebtRatio": {
        "name": "Debt Ratio",
        "increase": (
            "High debt obligations increased the predicted default risk."
        ),
        "decrease": (
            "Lower debt obligations reduced the predicted default risk."
        ),
    },

    "MonthlyIncome": {
        "name": "Monthly Income",
        "increase": (
            "Monthly income contributed to a higher predicted default risk."
        ),
        "decrease": (
            "Stable monthly income reduced the predicted default risk."
        ),
    },

    "NumberOfOpenCreditLinesAndLoans": {
        "name": "Open Credit Lines",
        "increase": (
            "The number of open credit accounts increased the predicted default risk."
        ),
        "decrease": (
            "The borrower's credit account profile reduced the predicted default risk."
        ),
    },

    "NumberOfTimes90DaysLate": {
        "name": "90-Day Late Payments",
        "increase": (
            "Repeated serious delinquencies significantly increased the predicted default risk."
        ),
        "decrease": (
            "Limited severe delinquency history reduced the predicted default risk."
        ),
    },

    "NumberRealEstateLoansOrLines": {
        "name": "Real Estate Loans",
        "increase": (
            "Existing real estate loan exposure increased the predicted default risk."
        ),
        "decrease": (
            "Real estate loan exposure reduced the predicted default risk."
        ),
    },

    "NumberOfTime60-89DaysPastDueNotWorse": {
        "name": "60-89 Day Late Payments",
        "increase": (
            "Past payment delays increased the predicted default risk."
        ),
        "decrease": (
            "Consistent repayment behaviour reduced the predicted default risk."
        ),
    },

    "NumberOfDependents": {
        "name": "Number of Dependents",
        "increase": (
            "Household obligations increased the predicted default risk."
        ),
        "decrease": (
            "Household obligations had a limited impact on predicted default risk."
        ),
    },
}


def get_feature_info(feature_name: str) -> dict:
    """
    Return feature metadata.

    Parameters
    ----------
    feature_name : str

    Returns
    -------
    dict
    """

    return FEATURE_INFO.get(
        feature_name,
        {
            "name": feature_name,
            "increase": "Feature increased predicted risk.",
            "decrease": "Feature reduced predicted risk.",
        },
    )