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

class DataGatherer(object):
    """
        The DataGatherer class focuses primarily on data manipulation
    """

    def __init__(self):
        self.headers = None

    def get_raw_data(self, filename):
        """Read in CSV data into python list"""

        data_raw = []
        with open(filename, 'r') as file:
            reader = csv.reader(file, delimiter=';')
            self.headers = reader.next()
            data_raw.append(self.headers)
            for row in reader:
                data_raw.append(row)

        return data_raw

    def find_index(self, header_row, title):
        """Given the header row and field name, the index of the filed
        name is found and returned.
        """
        tag_list = [tag for tag in header_row if title in tag]
        title_index = header_row.index(tag_list[0])
        return title_index


    def get_status_data(self, filename, status_title='CERTIFIED'):
        """A file will get read, and records associated with status are
         collected"""
        data_raw = []
        with open(filename, 'r') as file:
            reader = csv.reader(file, delimiter=';')
            self.headers = reader.next()
            data_raw.append(self.headers)
            status_index = self.find_index(self.headers, 'STATUS')
            count = 0
            for row in reader:
                if status_title in row[status_index]:
                    data_raw.append(row)
                else:
                    count += 1

        return data_raw

    def get_raw_data_by_status(self, data_raw, status='STATUS'):
        """
        Goes over raw data and removes the records with

        :param data_raw: Raw Data that has been read in from CSV into a 2D list
        :param status: Specifies to
        :return: Returned to clean, raw data with
        """
        status_index = self.find_index(data_raw[0], status)
        # count  = 1
        for item in data_raw[1:]:
            if 'CERTIFIED' not in item[status_index]:
                data_raw.remove(item)

        return data_raw

