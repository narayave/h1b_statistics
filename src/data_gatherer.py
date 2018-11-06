'''
CSV Data Gatherer

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
    '''
        The DataGatherer class focuses primarily on data manipulation
    '''

    def __init__(self):
        self.headers = None

    def get_data(self, filename):

        data_raw = []
        print 'Getting data from ', filename

        print csv.field_size_limit()
        with open(filename, 'r') as file:
            reader = csv.reader(file, delimiter=';')
            self.headers = reader.next()
            print self.headers
            for row in reader:
                data_raw.append(row)

        print len(data_raw)
        return data_raw

    def get_column_data(self, data_raw):

        pprint(data_raw[1:3])
        # print len(data_raw), self.headers

    # def split_by_status(self, data_raw):



