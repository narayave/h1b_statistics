'''
H1-B Counting

Author:
	Vedanth Narayanan
File:
	h1b_counting.py
Date:
	9 Nov, 2018

'''


import sys
from find_trends import FindTrends
from data_gatherer import DataGatherer
import time
from threading import Thread

def get_occupations_trend(input_file_name, output_file_name):

    field_names = ["SOC_NAME"]
    output_header = [['TOP_OCCUPATIONS', 'NUMBER_CERTIFIED_APPLICATIONS',
                      'PERCENTAGE']]

    trend = FindTrends(field_names, output_header)

    datagatherer = DataGatherer(input_file_name)
    certified_cases = datagatherer.get_status_data()
    trend.state_index_finder(datagatherer, certified_cases[0])

    all_trend_counts = trend.collect_trend(certified_cases[1:])
    # all_occupations = collect_occupations(certified_cases[1:])
    script_output = trend.generate_output_data(all_trend_counts,
                                         len(certified_cases)-1)

    trend.generate_output_file(output_file_name, script_output)


def get_states_trend(input_file_name, output_file_name):


    field_names = ["WORKSITE_STATE", "LCA_CASE_WORKLOC1_STATE"]
    output_header = [['TOP_STATES', 'NUMBER_CERTIFIED_APPLICATIONS',
                      'PERCENTAGE']]

    trend = FindTrends(field_names, output_header)

    datagatherer = DataGatherer(input_file_name)
    certified_cases = datagatherer.get_status_data()
    trend.state_index_finder(datagatherer, certified_cases[0])

    all_trend_counts = trend.collect_trend(certified_cases[1:])
    # all_occupations = collect_occupations(certified_cases[1:])
    script_output = trend.generate_output_data(all_trend_counts,
                                         len(certified_cases)-1)

    trend.generate_output_file(output_file_name, script_output)


if __name__ == '__main__':

    start = time.time()

    # thread_1 = Thread(target=get_occupations_trend, args=(sys.argv[1],
    #                                                       sys.argv[2]),)
    # thread_1.start()
    #
    # thread_2 = Thread(target=get_states_trend, args=(sys.argv[1],
    #                                                  sys.argv[3]),)
    # thread_2.start()
    #
    # thread_1.join()
    # thread_2.join()

    get_occupations_trend(sys.argv[1], sys.argv[2])
    get_states_trend(sys.argv[1], sys.argv[3])

    print 'Total time - ', time.time() - start
