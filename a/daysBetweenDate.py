def isLeapYear(year):
    if year % 400 == 0:
        return True
    if year % 4 == 0:
        if year % 100 == 0:
            return False
        else:
            return True
        
def daysInMonth(year, month):
    if month == 2:
        if isLeapYear(year):
            return 29
        else:
            return 28
    
    if month < 8:
        if month % 2 != 0:
            return 31
        else:
            return 30
    else:
        if month % 2 == 0:
            return 31
        else:
            return 30
    

def nextDay(year, month, day):
    if day < daysInMonth(year, month):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1

def dateIsBefore(year1, month1, day1, year2, month2, day2):
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""

    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days


# print(daysBetweenDates(2013, 1, 24, 2013, 6, 29))
# print(daysBetweenDates(1912, 12, 12, 2012, 12, 12))
# print(daysBetweenDates(2017, 12, 30, 2018, 1, 1))