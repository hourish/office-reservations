# office-reservations

Given a month and a year, the program reads a CSV file and prints what is the revenue for the month and what is the total capacity of the unreserved offices for the month.

Instructions:
Download the file revenueCalculator.py (Python version 3.7.1)

The required arguments for the program:
First – the name of the csv file, for example reservations.csv, where each line represents a reservation of a unique office. There are four columns in each line: Capacity, Monthly Price, Start Day, and End Day. The fourth column "End Day" could be empty, meaning the office is indefinitely reserved starting from the Start Day.
Second – a month and a year in the following format: YYYY-MM, for example 2000-01
** Assumption - both arguments are valid inputs

Run from the cmd in the directory of the file: python revenueCalculator.py firstArgument secondArgument, for example: python revenueCalculator.py reservations.csv 2014-03

The result will be printed to you

Answers:

1. How much time did you spend? I spent about 4 hours to design and write the code, open repository and write README.
2. What was the most difficult thing for you? Manipulate the dates and think about all the possible cases
3. What technical debt would you pay if you had one more iteration? I would write tests to check different inputs.

* The results for the following inputs:

* 2013-01: expected revenue: $8,100.0, expected total capacity of the unreserved offices: 254

* 2013-06: expected revenue: $15,150.0, expected total capacity of the unreserved offices: 241

* 2014-03: expected revenue: $37,214.516129, expected total capacity of the unreserved offices: 203

* 2014-09: expected revenue: $86,700.0, expected total capacity of the unreserved offices: 120

* 2015-07: expected revenue: $76,225.8064516, expected total capacity of the unreserved offices: 135



