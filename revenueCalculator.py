import csv
from datetime import date
import sys
from calendar import monthrange

CAPACITY_INDEX = 0
MONTHLY_PRICE_INDEX = 1
START_DAY_INDEX = 2
END_DAY_INDEX = 3


def calculate(file, yearAndMonth):
     '''
     print the expected revenue and expected total capacity of the unreserved offices according to the given file,
     year and month
     :param file: path to the csv file
     :param yearAndMonth: a month and a year in the following format: YYYY-MM
     '''
     expectedRevenue = 0
     unreservedCapacity = 0
     split = yearAndMonth.split('-')
     year = int(split[0])
     month = int(split[1])
     with open(file, 'rt') as csvfile:
          reader = csv.reader(csvfile)
          next(reader)  # skip header line
          for row in reader:
               startDate, endDate = createDates(row)
               startMonth = date(year, month, 1)
               _, monthDays = monthrange(year, month)
               endMonth = date(year, month, monthDays)
               if is_reserved(startMonth, endMonth, startDate, endDate):
                    expectedRevenue += compute_revenue(startMonth, endMonth, monthDays, startDate, endDate, row[MONTHLY_PRICE_INDEX])
               else:
                    unreservedCapacity += int(row[CAPACITY_INDEX])
     print ('expected revenue: $' + '{:,}'.format(expectedRevenue) + ', expected total capacity of the unreserved offices: ' + str(unreservedCapacity))


def is_reserved(startMonth, endMonth, startDate, endDate):
     '''
     check if the office is reserved in the given dates
     :param startMonth: full date of the first day of the month of the given month and year
     :param endMonth: full date of the last day of the month of the given month and year
     :param startDate: the start date of the current row
     :param endDate: the end date of the current row
     :return: true if the office is reserved, false if not
     '''
     # if the given month and year are before the start date
     if endMonth < startDate:
          return False
     if endDate == '':
          return True
     # if the given month and year are after the end date
     if startMonth > endDate:
          return False
     return True


def createDates(row):
     '''
     parse the start and end day from the row and return as dates
     :param row: row from the csv file
     :return: start date and end date as dates
     '''
     splitStart = row[START_DAY_INDEX].split('-')
     startDate = date(int(splitStart[0]), int(splitStart[1]), int(splitStart[2]))
     if row[END_DAY_INDEX] != '':
          splitEnd = row[END_DAY_INDEX].split('-')
          endDate = date(int(splitEnd[0]), int(splitEnd[1]), int(splitEnd[2]))
     else:
          endDate = ''
     return startDate, endDate


def compute_revenue(startMonth, endMonth, monthDays, startDate, endDate, monthlyPrice):
     '''
     Return the revenue for the month
     :param startMonth: full date of the first day of the month of the given month and year
     :param endMonth: full date of the last day of the month of the given month and year
     :param monthDays: number of days in the month
     :param startDate: the start date of the current row
     :param endDate: the end date of the current row
     :param monthlyPrice: the monthly price of the office of the current row
     :return:the revenue for the month
     '''
     #  from the begining to the month
     if startDate <= startMonth:
          #  the whole month
          if endDate == '' or endMonth <= endDate:
               return float(monthlyPrice)
          #  until the end date
          return (float(endDate.day) / monthDays) * float(monthlyPrice)
     #  not from the begining to the month
     if endDate == '' or endDate >= endMonth:
          partFromTheMonth = float((monthDays - startDate.day + 1)) / monthDays
          return partFromTheMonth * float(monthlyPrice)
     partFromTheMonth = float((endDate.day - startDate.day + 1)) / monthDays
     return partFromTheMonth * float(monthlyPrice)


if __name__ == '__main__':
     calculate(sys.argv[1], sys.argv[2])
