'''
Created on  April 26, 2022
@author:    Songhan Yu
Pledge:     I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 12 - Date class
'''
DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

class Date(object):
    '''A user-defined data structure that stores and manipulates dates.'''

    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        '''The constructor for objects of type Date.'''
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        '''This method returns a string representation for the
           object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.'''
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    def __repr__(self):
        '''This method also returns a string representation for the object.'''
        return self.__str__()

    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        '''Returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False

    def copy(self):
        '''Returns a new object with the same month, day, year
        as the calling object (self).'''
        dnew = Date(self.month, self.day, self.year)
        return dnew

    def equals(self, d2):
        '''Decides if self and d2 represent the same calendar date,
        whether or not they are the in the same place in memory.'''
        return self.year == d2.year and self.month == d2.month and \
        self.day == d2.day


    def tomorrow(self):
        '''represents one calendar day after the date it originally represented.'''
        daysLeapYear = 28 + self.isLeapYear()
        DAYS_IN_MONTH = (0,31, daysLeapYear,31,30,31,30,31,31,30,31,30,31)
        if self.day == DAYS_IN_MONTH[self.month]:
            if self.month == 12:
                self.day = 1
                self.month = 1
                self.year += 1
            else:
                self.day = 1
                self.month += 1
        else:
            self.day += 1

    def yesterday(self):
        '''represents one calendar day before the date it originally represented.'''
        daysLeapYear = 28 + self.isLeapYear()
        DAYS_IN_MONTH = (0,31, daysLeapYear,31,30,31,30,31,31,30,31,30,31)
        if self.day == 1:
            if self.month == 1:
                self.day = 31
                self.month = 12
                self.year -= 1
            else:
                self.day = DAYS_IN_MONTH[self.month-1]
                self.month -= 1
        else:
            self.day -= 1


    def addNDays (self, N):
        '''represents N calendar days after the date it originally represented'''
        print(self)
        for day in range (N):
            self.tomorrow()
            print(self)

    def subNDays (self, N):
        '''represents N calendar days before the date it originally represented'''
        print(self)
        for day in range (N):
            self.yesterday()
            print(self)

    def isBefore (self, d2):
        '''return True if the calling object is a calendar date before the input named d2 (which will always be an object of type Date)'''
        if self.year > d2.year :
            return False
        elif self.year < d2.year:
            return True
        elif self.month > d2.month:
            return False
        elif self.month < d2.month:
            return True
        elif self.day > d2.day:
            return False
        elif self.day < d2.day:
            return True
        else:
            return False

    def isAfter(self, d2):
        '''return True if the calling object is a calendar date after the input named d2 (which will always be an object of type Date)'''
        if self.isBefore(d2):
            return False
        elif d2.isBefore(self):
            return True
        else:
            return False

    def diff (self, d2):
        '''return an integer representing the number of days between self and d2.  (self - d2)'''
        day1 = self.copy()
        day2 = d2.copy()
        diffDay = 0
        while day1.isBefore(day2):  # If self is before d2, this method should return a negative integer equal to the number of days between the two dates
            diffDay -= 1
            day1.tomorrow()

        while day1.isAfter(day2):  # If self is after d2, this method should return a positive integer equal to the number of days between the two dates.
            diffDay += 1
            day1.yesterday()

        return diffDay


    def dow(self):
        '''return a string that indicates the day of the week (dow) of the object'''
        start_date = Date(12, 7, 1941)
        days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday','Thursday', 'Friday', 'Saturday']
        return days[self.diff(start_date) % 7]   


# test case
if __name__ == "__main__":
    d = Date(1, 1, 2011)
    d2 = d.copy()
    print(d)    # 01/01/2011
    print(d2)   # 01/01/2011
    print(d == d2)         # False
    print(d.equals(d2))    # True
    print(d.equals(Date(1, 1, 2011)))   # True
    print(d == Date(1, 1, 2011))        # False

    d = Date(12, 31, 2010)
    print(d)  # 12/31/2010
    d.tomorrow()
    print(d)  # 01/01/2011

    d = Date(1, 1, 2011)
    print(d)  # 01/01/2011
    d.yesterday()
    print(d)  # 12/31/2010

    d = Date(11, 9, 2011)
    d.addNDays(3)
    print(d)  # 11/12/2011

    d = Date(11, 11, 2011)
    d2 = Date(1, 1, 2012)
    print(d.isBefore(d2))  # True
    print(d2.isBefore(d))  # False
    print(d.isBefore(d))   # False

    d = Date(11,9,2011)
    d2 = Date(12,16,2011)
    print(d2.diff(d))   # 37
    print(d.diff(d2))   # -37
    print(d)    # 11/09/2011
    print(d2)   # 12/16/2011

    d = Date(11,9,2011)
    d3 = Date(5, 18, 2012)
    print(d3.diff(d))  # 191

    d = Date(12, 7, 1941)
    print(d.dow())
    print(Date(10, 28, 1929).dow())
    print(Date(10, 19, 1987).dow())

    d = Date(1, 1, 2100)
    print(d.dow())