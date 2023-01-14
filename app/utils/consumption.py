from itertools import groupby
from datetime import datetime

def sample_hour(sample):
    return sample.meter_date.replace(minute=0, second=0)


def sample_day(sample):
    return sample.meter_date.replace(hour=0, minute=0, second=0)


def max_dif(l):
    values = [v.active_energy for v in l]
    return max(values) - min(values)


def group_usages_by_hour(meters):
    grouped_usages =  {hour: list(sample) for hour, sample in groupby(meters, sample_hour)}
    return {key: max_dif(value) for key, value in grouped_usages.items()} 


def group_usages_by_day(meters):
    grouped_usages =  {hour: list(sample) for hour, sample in groupby(meters, sample_day)}
    return {key: max_dif(value) for key, value in grouped_usages.items()} 


def get_usages(meters, period):
    if period == "daily":
        usages = group_usages_by_hour(meters)
    else:
        usages = group_usages_by_day(meters)
    return usages
