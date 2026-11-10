from datetime import datetime


def time_left(deadline):
    """
    Calculates the number of hours remaining until the deadline.

    Args:
        deadline (datetime): The task's deadline.

    Returns:
        float: The number of hours remaining until the deadline.

    Raises:
        ValueError: If the deadline is in the past or not a valid datetime object.
    """
    if not isinstance(deadline, datetime):
        raise ValueError("Invalid deadline. Must be a datetime object.")

    now = datetime.now()
    if deadline < now:
        raise ValueError("Deadline has already passed.")

    time_remaining = deadline - now
    return time_remaining.total_seconds() / 3600