from app.utils.time import (
    get_periods,
    get_hours_day,
    get_days,
    get_week_days,
    get_month_days
)

def test_get_periods():
    assert ['2022-10-10 00:00:00',
            '2022-10-11 00:00:00',
            '2022-10-12 00:00:00',
            '2022-10-13 00:00:00',
            '2022-10-14 00:00:00',
            '2022-10-15 00:00:00',
            '2022-10-16 00:00:00'] == get_periods("2022-10-12", "weekly") 


def test_get_hours_day():
    assert ['2022-10-12 00:00:00', 
            '2022-10-12 01:00:00', 
            '2022-10-12 02:00:00', 
            '2022-10-12 03:00:00'] == get_hours_day("2022-10-12")[:4]


def test_get_days():
    assert '2022-10-12 00:00:00' == get_days("2022-10-12", 5)[0]
    


def test_get_week_days():
    assert '2022-10-24 00:00:00' == get_week_days("2022-10-26")[0]
    


def test_get_month_day():
    assert '2022-03-01 00:00:00' == get_month_days("2022-03-12")[0]

