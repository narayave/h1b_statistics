'''
Data Gatherer

Author:
	Vedanth Narayanan
File:
	data_gatherer.py
Date:
	6 Nov, 2018

'''

import csv
from pprint import pprint   # TODO: Specify pprint is used for clean printing

class DataGatherer(object):
    """
        The DataGatherer class focuses primarily on data manipulation
    """

    def __init__(self):
        self.headers = None

    def get_raw_data(self, filename):
        """Read in CSV data into python list"""

        data_raw = []
        print 'Getting data from ', filename

        # print csv.field_size_limit()
        with open(filename, 'r') as file:
            reader = csv.reader(file, delimiter=';')
            self.headers = reader.next()
            data_raw.append(self.headers)
            # print self.headers
            for row in reader:
                data_raw.append(row)

        print len(data_raw)
        return data_raw

    def find_index(self, header_row, title):
        """Given the header row and field name, the index of the filed
        name is found and returned.
        """

        # STATUS
        # SOC_NAME
        # WORKSITE_STATE or LCA_CASE_WORKLOC1_STATE

        # Working under the assumption that 'STATUS' typically used
        # only for the Case Status
        tag_list = [tag for tag in header_row if title in tag]
        title_index = header_row.index(tag_list[0])
        return title_index

    def get_certified_data(self, data_raw):

        status_index = self.find_index(data_raw[0], 'STATUS')

        for item in data_raw:
            if 'CERTIFIED' not in item[status_index]:
                data_raw.remove(item)

        print len(data_raw)

        return data_raw


    def get_column_data(self, data_raw):

        pprint(data_raw[1:3])
        # print len(data_raw), self.headers

    # def split_by_status(self, data_raw):



