"""
Custom exceptions for the Credit Risk Decision Engine.
"""


class CreditRiskError(Exception):
    """
    Base exception for the application.
    """


class ModelNotFoundError(CreditRiskError):
    """
    Raised when the trained model
    cannot be located.
    """

class InvalidBorrowerError(CreditRiskError):
    """
    Raised when borrower data
    is invalid.
    """


class PredictionError(CreditRiskError):
    """
    Raised when prediction fails.
    """
