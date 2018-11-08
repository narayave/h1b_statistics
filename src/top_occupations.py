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
from threading import Thread
import time

OCCUPATION_INDEX = None


def collect_occupations(data):
    """
        This function produces a dictionary with all reported occupations and
        the count for each occupation.

        TODO: Occupation field might have duplicates (result of typos or more
        specific titles), and those will not be consolidated. Can be taken into
        account at a later date.

    :param data: Certified data in a 2d array
    :return: Dictionary with all reported occupations and their counts
    """

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

def generate_output_data(all_occupations, total_certified_cases):
    """
        There are 2 part involved. First, the top occupations are sorted.
        Second, a call is made to get the percentages data, and ultimately the
        output.

    :param all_occupations: Dictionary with
    :param total_certified_cases: Count of total number of certified cases
    :return: Returns the approriate output for the occupations script
    """
    sorted_top_occupations = sort_top_occupations(all_occupations)
    occupations_output = get_occupations_percentage(sorted_top_occupations,
                                                    total_certified_cases)
    return occupations_output

def get_occupations_percentage(top_occupations_list, total_certified_count):
    """

    :param top_occupations_list:
    :param total_certified_count:
    :return:
    """
    for i in xrange(len(top_occupations_list)):

        percentage = ((top_occupations_list[i][1] * 100.0) / total_certified_count)
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
    """
        The output data is passed to the OutputWriter to produce output file.

    :param output_file: Specifies the path and name of the output file
    :param output_data: Output data that will need to be outputted to the said
        file. This needs to be a 2d array.
    :return: Returns nothing
    """
    writer = OutputWriter(output_file)
    writer.produce_output(output_data)


if __name__ == '__main__':

    start = time.time()

    input_file_name = sys.argv[1]
    output_file_name = sys.argv[2]

    datagatherer = DataGatherer()
    certified_cases = datagatherer.get_status_data(input_file_name)
    OCCUPATION_INDEX = datagatherer.find_index(certified_cases[0], 'SOC_NAME')

    all_occupations = collect_occupations(certified_cases[1:])
    script_output = generate_output_data(all_occupations, len(certified_cases))

    generate_output_file(output_file_name, script_output)

    print 'Time taken - ', time.time() - start