from calendar import monthrange
from datetime import datetime, timedelta
from itertools import repeat


def get_periods(date, period):
    if period == "daily":
        periods = get_hours_day(date)
    if period == "weekly":
        periods = get_week_days(date)
    if period == "monthly":
        periods = get_month_days(date)
    return periods


def get_hours_day(period):
    year, month, day = period.split("-") # TODO: this will be changed for regular expression in case that don't use "-" string
    date = datetime(int(year), int(month), int(day))
    return [(date + timedelta(hours=hour)).strftime("%Y-%m-%d %H:%M:%S") if hour != 23 else 
            (date + timedelta(hours=hour, minutes=59)).strftime("%Y-%m-%d %H:%M:%S") 
            for hour, sec in zip(range(0, 24), repeat(1, len(range(0,24))))]


def get_days(period, num_days: int):
    year, month, day = period.split("-") # TODO: this will be changed for regular expression in case that don't use "-" string
    date = datetime(int(year), int(month), int(day))
    return [(date + timedelta(days=d)).strftime("%Y-%m-%d %H:%M:%S") for d in range(0, num_days)]


def get_week_days(period):
    year, month, day = period.split("-") # TODO: this will be changed for regular expression in case that don't use "-" string
    first_day = int(day) - datetime(int(year), int(month), int(day)).weekday()
    week_days = get_days(f"{year}-{month}-{first_day}", 7)
    return week_days

def get_month_days(period):
    year, month, _ = period.split("-") # TODO: this will be changed for regular expression in case that don't use "-" string
    _, month_num_days = monthrange(int(year), int(month))
    month_days = get_days(f"{year}-{month}-01", month_num_days)
    return month_days
