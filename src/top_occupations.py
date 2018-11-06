'''
Top 10 Occupations for H1-Bs

Author:
	Vedanth Narayanan
File:
	top_occupations.py
Date:
	5 Nov, 2018


Input:


Output:
    top_10_occupations.txt: Top 10 occupations for certified visa applications

    - TOP_OCCUPATIONS: Use the occupation name associated with an application's
        Standard Occupational Classification (SOC) code
    - NUMBER_CERTIFIED_APPLICATIONS: Number of applications that have been
        certified for that occupation. An application is considered certified if
        it has a case status of Certified
    - PERCENTAGE: % of applications that have been certified for that occupation
        compared to total number of certified applications regardless of
        occupation.

'''


import sys
from data_gatherer import DataGatherer


if __name__ == '__main__':

    filename = sys.argv[1]

    datag = DataGatherer()

    data_raw = datag.get_data(filename)
    datag.get_column_data(data_raw)


