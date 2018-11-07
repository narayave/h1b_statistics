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
import operator
from data_gatherer import DataGatherer
from output_writer import OutputWriter
from pprint import pprint

OCCUPATION_INDEX = None

def collect_occupations(data):
    """Reads occupation titles and keeps count via a dict"""

    count_occupations = {}

    for item in data:
        occupation_title = item[OCCUPATION_INDEX]

        if occupation_title in count_occupations:
            count_occupations[occupation_title] += 1
        else:
            count_occupations[occupation_title] = 1

    return count_occupations


def sort_top_occupations(all_occupations):

    top_occupations = dict(sorted(all_occupations.iteritems(),
                                  key=operator.itemgetter(1),
                                  reverse=True)[:10])

    top_occupations_list = [(key, value) for key, value in top_occupations.iteritems()]

    top_occupations_list = sorted(top_occupations_list,
                                  key=operator.itemgetter(1),
                                  reverse=True)

    return top_occupations_list

def generate_output_list(all_occupations, total_certified_cases):

    top_occupations = sort_top_occupations(all_occupations)

    occupations_output = get_occupations_percentage(top_occupations,
                                                    total_certified_cases)

    return occupations_output

def get_occupations_percentage(top_occupations_list, total_certified_count):

    for i in xrange(len(top_occupations_list)):

        percentage = ((top_occupations_list[i][1] * 1.0) / total_certified_count) * 100.00
        percentage = "{0:0.1f}".format(percentage)

        top_occupations_list[i] = [top_occupations_list[i][0],
                                   top_occupations_list[i][1],
                                   str(percentage)+'%']

    pprint(top_occupations_list)

    output_header = [['TOP_OCCUPATIONS', 'NUMBER_CERTIFIED_APPLICATIONS',
                      'PERCENTAGE']]
    top_occupations_list = output_header + top_occupations_list

    return top_occupations_list


def generate_output_file(output_file, output_data):
    """Should build output and make calls to the OutputWriter class"""

    writer = OutputWriter(output_file)
    writer.produce_output(output_data)


if __name__ == '__main__':

    input_file_name = sys.argv[1]
    output_file_name = sys.argv[2]

    datag = DataGatherer()
    certified_cases = datag.get_status_data(input_file_name)
    OCCUPATION_INDEX = datag.find_index(certified_cases[0], 'SOC_NAME')

    all_occupations = collect_occupations(certified_cases[1:])
    script_output = generate_output_list(all_occupations, len(certified_cases))

    generate_output_file(output_file_name, script_output)