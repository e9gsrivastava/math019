'''this is find the num of Sundays'''

from datetime import date
from datetime import datetime


def solver(start, end):
    """
    Counts the number of Sundays that fall on the first of the month from start to end
    """

    start_year = start.year
    start_month = start.month
    start_day = start.day
    end_year = end.year
    end_month = end.month
    end_day = end.day

    weekday_dict = {
        "Sunday": 0,
        "Monday": 1,
        "Tuesday": 2,
        "Wednesday": 3,
        "Thursday": 4,
        "Friday": 5,
        "Saturday": 6,
    }
    sunday_count = 0
    current_day = weekday_dict[
        datetime(start_year, start_month, start_day).strftime("%A")
    ]

    for year in range(1900, end_year + 1):
        is_leap_year = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

        for month in range(1, 13):
            days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

            if month == 2 and is_leap_year:
                days_in_month[2] = 29

            days = days_in_month[month]
            if year > start_year or (year == start_year and month >= start_month):

                for day in range(1, days + 1):
                    if year < end_year or (
                        year == end_year and month <= end_month and day <= end_day
                    ):
                        if day == 1 and current_day == 0:
                            sunday_count += 1

                        current_day = (current_day + 1) % 7
    return sunday_count


if __name__ == "__main__":
    print(solver(date(2001, 1, 1), date(2023, 12, 31)))
