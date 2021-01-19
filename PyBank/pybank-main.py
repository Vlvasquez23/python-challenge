#Assignment 3: Python Homework - Py Me Up, Charlie (PyBank)

import os
import csv

# Variables
tot_mths = 0
net_amt = 0
mth_chg = []
mth_ct = []
greatest_incr = 0
greatest_incr_mth = 0
greatest_decr = 0
greatest_decr_mth = 0

# Set Path For File
csvpath = os.path.join('.', 'python-challenge', 'PyBank', 'Resources', 'budget_data.csv')


with open(csvpath, newline='') as csvfile:
    
    # CSV Reader 
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # To read header
    csv_header = next(csvreader)
    row = next(csvreader)
        
    previous_row = int(row[1])
    tot_mths += 1
    net_amt += int(row[1])
    greatest_incr = int(row[1])
    greatest_incr_mth = row[0]
    
    # For each row after the header
    for row in csvreader:
        
        # Find Total of Months
        tot_mths += 1
        net_amt += int(row[1])

        # Change month to month
        revenue_change = int(row[1]) - previous_row
        mth_chg.append(revenue_change)
        previous_row = int(row[1])
        mth_ct.append(row[0])
               
        # Calculate The Greatest Increase
        if int(row[1]) > greatest_incr:
            greatest_incr = int(row[1])
            greatest_incr_mth = row[0]
            
        # Calculate The Greatest Decrease
        if int(row[1]) < greatest_decr:
            greatest_decr = int(row[1])
            greatest_decr_mth = row[0]  
        
    # Calculate The Average & The Date
    avg_chg = sum(mth_chg)/ len(mth_chg)
    
    highest = max(mth_chg)
    lowest = min(mth_chg)

# Print Analysis
print(f"Financial Analysis")
print(f"---------------------------")
print(f"Total Months: {tot_mths}")
print(f"Total: ${net_amt}")
print(f"Average Change: ${avg_chg:.2f}")
print(f"Greatest Increase in Profits:, {greatest_incr_mth}, (${highest})")
print(f"Greatest Decrease in Profits:, {greatest_decr_mth}, (${lowest})")

# Path to output text file
output_file = os.path.join('.', 'python-challenge', 'PyBank', 'Analysis', 'Pybank.txt')

# Open File Using "Write" Mode. 
with open(output_file, 'w',) as txtfile:

# Text Data
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Months: {tot_mths}\n")
    txtfile.write(f"Total: ${net_amt}\n")
    txtfile.write(f"Average Change: ${avg_chg:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_incr_mth}, (${highest})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decr_mth}, (${lowest})\n")

