'''
TOP 10 States for H1-Bs

Author:
	Vedanth Narayanan
File:
	Anomaly Detector class
Date:
	7 Nov, 2018

'''


import sys
from data_gatherer import DataGatherer
from output_writer import OutputWriter

STATE_INDEX = None
STATE_FIELD_NAMES = ["WORKSITE_STATE", "LCA_CASE_WORKLOC1_STATE"]
REQUIRED_TOP_VALUES = 10


def __helper_state_index_finder(datagatherer, header_row):
    """
        Different years have different field names for the worksite field.
        The field name was "LCA_CASE_WORKLOC1_STATE" before 2015 and after it is
        "WORKSITE_STATE." This helper function

    :param datagatherer: The DataGatherer object
    :param header_row: Holds the field names for the gathered data
    :return: Column index for said field name
    """

    for field_name in STATE_FIELD_NAMES:
        if field_name in header_row:
            state_index = datagatherer.find_index(header_row, field_name)

    return state_index


def collect_states(data):
    """
        This function produces a dictionary with all reported occupations and
        the count for each occupation.

    :param data: Certified data in a 2d array
    :return: Dictionary with all states and their counts
    """
    count_states = {}
    for item in data:
        state_title = item[STATE_INDEX]
        if state_title in count_states:
            count_states[state_title] += 1
        else:
            count_states[state_title] = 1

    return count_states


def sort_top_states(all_states, req_number=REQUIRED_TOP_VALUES):
    """
        This function sorts the dictonary by state counts to get the top states.
        The top values are converted to a list, and further sorted
        alphabetically, in the case of equal counts.

    :param all_states: Dictionary with count for all occupatons
    :param req_number: The required number of top values, default is set to 10,
        globally
    :return: Sorted list of top states and the total number
    """
    top_states = dict(sorted(all_states.items(),
                             key=lambda item: (item[1], item[0]),
                             reverse=True)[:req_number])
    top_states_list = [(key, value) for key, value in top_states.iteritems()]
    top_states_list = sorted(top_states_list,
                             key=lambda item: (-item[1], item[0]))

    return top_states_list


def get_states_percentage(top_states_list, total_certified_count):
    """
        From the states list, the percentage values are calculated. The
        same 2d list is then updated to also hold the percentage value.

    :param top_states_list: The sorted list with the top states and counts
    :param total_certified_count: A count of all certified H1-B cases
    :return: 2D list with state names, count, and percenage of total certified
        cases
    """
    for i in xrange(len(top_states_list)):

        percentage = ((top_states_list[i][1] * 100.0) / total_certified_count)
        percentage = "{0:0.1f}".format(percentage)

        top_states_list[i] = [top_states_list[i][0],
                              top_states_list[i][1],
                              str(percentage)+'%']

    output_header = [['TOP_STATES', 'NUMBER_CERTIFIED_APPLICATIONS',
                      'PERCENTAGE']]
    top_states_list = output_header + top_states_list

    return top_states_list


def generate_output_data(all_states, total_certified_cases):
    """
        There are 2 part involved. First, the top occupations are sorted.
        Second, a call is made to get the percentages data, and ultimately the
        output.

    :param all_states: Dictionary with all states and counts
    :param total_certified_cases: Count of total number of certified cases
    :return: The approriate output to be outputted to the output file
    """
    sorted_top_states = sort_top_states(all_states)
    states_output = get_states_percentage(sorted_top_states,
                                          total_certified_cases)
    return states_output


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

    input_file_name = sys.argv[1]
    output_file_name = sys.argv[2]

    datagatherer = DataGatherer(input_file_name)
    certified_cases = datagatherer.get_status_data()
    STATE_INDEX = __helper_state_index_finder(datagatherer, certified_cases[0])

    all_states = collect_states(certified_cases[1:])
    script_output = generate_output_data(all_states, len(certified_cases)-1)

    generate_output_file(output_file_name, script_output)
