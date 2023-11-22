import datetime


def calculate_expected_return_date(borrow_days: int) -> datetime:
    """Calculates the date on which book has to be returned without any penalties"""
    current_date = datetime.date.today()
    return current_date + datetime.timedelta(days=borrow_days)
