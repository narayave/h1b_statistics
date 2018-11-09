'''
Find Trends

Author:
	Vedanth Narayanan
File:
	find_trends.py
Date:
	9 Nov, 2018

'''


from output_writer import OutputWriter


class FindTrends(object):

    def __init__(self, possible_field_names, output_header, top_values_count=10):
        self.field_names = possible_field_names
        self.output_header = output_header
        self.required_top_values = top_values_count
        self.field_index = None


    def fieldname_index_finder(self, datagatherer, header_row):
        """
            Different datasets have different field names for the worksite
            field.This helper function that checks all known versions of the
            field name to find an index.
            For example, the field name for work state was
            "LCA_CASE_WORKLOC1_STATE" before 2015 and after it is
            "WORKSITE_STATE."

        :param datagatherer: The DataGatherer object
        :param header_row: Holds the field names for the gathered data
        :return: The index of the field name is returned, if it exists
        """
        index = None
        for field_name in self.field_names:
            if any(field_name in item for item in header_row):
                index = datagatherer.find_index(header_row, field_name)

        if index is None:
            print 'Error: Could not find index'
            return

        self.field_index = index
        return self.field_index


    def collect_trend(self, data):
        """
            This function produces a dictionary with all reported occupations
            and the count for each occupation.

        :param data: Certified data in a 2d list
        :return: Dictionary with all trend fields and their counts
        """
        count_trend_fields = {}
        for item in data:
            trend_title = item[self.field_index]
            if trend_title in count_trend_fields:
                count_trend_fields[trend_title] += 1
            else:
                count_trend_fields[trend_title] = 1

        return count_trend_fields


    def sort_top_values(self, all_values):
        """
            This function sorts the dictionary by trend counts to get the top
            results. The top values are converted to a list, and further sorted
            alphabetically, in the case of equal counts.

        :param all_values: Dictionary with counts for all values in the trend
        :return: Sorted list of top values and the total number
        """
        top_values = dict(sorted(all_values.items(),
                                 key=lambda item: (item[1], item[0]),
                                 reverse=True)[:self.required_top_values])
        top_values_list = [(key, value) for key, value in
                           top_values.iteritems()]
        top_values_list = sorted(top_values_list,
                                 key=lambda item: (-item[1], item[0]))

        return top_values_list


    def get_values_percentage(self, top_values_list, total_certified_count):
        """
            From the trends list, the percentage values are calculated. The
            same 2d list is then updated to also hold the percentage value.

        :param top_values_list: The sorted list with the top trend values and
            their counts
        :param total_certified_count: A count of all certified H1-B cases
        :return: 2D list with value names, count, and percenage of total
            certified cases
        """
        for i in xrange(len(top_values_list)):
            percentage = (
                        (top_values_list[i][1] * 100.0) / total_certified_count)
            percentage = "{0:0.1f}".format(percentage)

            top_values_list[i] = [top_values_list[i][0],
                                  top_values_list[i][1],
                                  str(percentage) + '%']

        top_values_list = self.output_header + top_values_list

        return top_values_list


    def generate_output_data(self, all_trend_values, total_certified_cases):
        """
            There are 2 part involved. First, the top occupations are sorted.
            Second, a call is made to get the percentages data, and ultimately the
            output.

        :param all_trend_values: Dictionary with all trend values and counts
        :param total_certified_cases: Count of total number of certified cases
        :return: The approriate output (formed as a 2d list) to be outputted to
            the output file
        """
        sorted_top_values = self.sort_top_values(all_trend_values)
        trends_output = self.get_values_percentage(sorted_top_values,
                                              total_certified_cases)
        return trends_output


    def generate_output_file(self, output_file, output_data):
        """
            The output data is passed to the OutputWriter to produce output file.

        :param output_file: Specifies the path and name of the output file
        :param output_data: Output data that will need to be outputted to the said
            file. This needs to be a 2d array.
        :return: None
        """
        writer = OutputWriter(output_file)
        writer.produce_output(output_data)
