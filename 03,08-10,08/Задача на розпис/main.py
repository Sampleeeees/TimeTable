import datetime

def timetable(year1, month1, day1, year2, month2, day2, date_work, date_skip):
    date_start = datetime.date(year1, month1, day1)
    date_end = datetime.date(year2, month2, day2)

    dates = []
    date_minus = date_end - date_start

    if(date_work != 0):
        for y in range(date_work-1, date_minus.days, date_skip + date_work):
            dates.append(str(date_start + datetime.timedelta(days=y)))
    else:
        dates = []


    print(dates)



timetable(2022, 5, 14, 2022, 5, 24, 1, 95)