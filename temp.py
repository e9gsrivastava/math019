def count_sundays(start_year, end_year):
    '''
    Counts the number of Sundays that fall on the first of the month
    '''

    sunday_count = 0
    current_day = 0  

    for year in range(start_year, end_year + 1):
        is_leap_year = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
        for month in range(1, 13):
            days= 31
            if month in (4, 6, 9, 11):
                days = 30
            elif month == 2:
                if is_leap_year:
                    days = 29
                else: 
                    days = 29

            current_day = (current_day + days) % 7
            if current_day == 0: 
                sunday_count += 1

    return sunday_count

if __name__=='__main__':
    print(1901, 2000)
