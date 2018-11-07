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
        with open(self.filename, 'wb') as file:
            writer = csv.writer(file, delimiter=';')
            for item in output:
                writer.writerow(item)

        print 'DONE'


if __name__ == '__main__':

    ow = OutputWriter('../output/top_10.txt')
    ow.produce_output()