'''
Output Writer

Author:
	Vedanth Narayanan
File:
	output_writer.py
Date:
	6 Nov, 2018

'''

import csv

class OutputWriter:
    '''
        This class is used for outputting data to proper files
    '''

    def __init__(self, filename):
        self.filename = filename

    def produce_output(self, output):
        """
           This function takes the incoming data and puts it in a .txt file.

        :param output: A 2d list holding data that needs to be outputted to a
        file.
        :return: None
        """
        with open(self.filename, 'wb') as file:
            writer = csv.writer(file, delimiter=';')
            for item in output:
                writer.writerow(item)

