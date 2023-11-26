from datetime import datetime, timedelta


def calculate_expected_return_date(borrow_days: int) -> datetime:
    """Calculates the date on which the book has to be returned without any penalties."""
    current_date = datetime.now()
    return datetime.now() + timedelta(days=borrow_days)
