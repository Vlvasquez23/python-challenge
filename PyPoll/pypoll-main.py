#Assignment 3: Python Homework - Py Me Up, Charlie (PyPoll)

import os
import csv


csvpath = os.path.join('.','python-challenge', 'PyBank', 'Resources', 'election_data.csv')

with open(csvpath, newline='') as csvfile:
       
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)
    row = next(csvreader)

    