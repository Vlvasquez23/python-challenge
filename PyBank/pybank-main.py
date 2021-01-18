#Assignment 3: Python Homework - Py Me Up, Charlie (PyBank)

import os
import csv

# Variables
#total months
tot_mths = 0
#net amount
net_amt = 0
#Monthly Change
mth_chg = []
#Month Count
mth_ct = []
greatest_incr = 0
greatest_incr_mth = 0
greatest_decr = 0
greatest_decr_mth = 0

csv_path = os.path.join('.', 'PyBank', 'Resources', 'budget_data.csv')

with open(csv_path, newline='') as csvfile:
       
    csv_reader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csv_reader)
    row = next(csv_reader)

#Total of Months
    previous_row = int(row[1])
    tot_mths += 1
    net_amt += int(row[1])
    greatest_incr = int(row[1])
    greatest_incr_mth = row[0]

    for row in csv_reader:
   
     tot_mths += 1
     net_amt += int(row[1])

     revenue_chg = int(row[1])-previous_row
     mth_chg.append(revenue_chg)   
     previous_row = int(row[1])
     mth_ct.append(row[0])

# Find greatest increase
    if int(row[1]) > greatest_incr:
        greatest_incr = int(row[1])
        greatest_incr_mth = row[0]

# Find greatest decrease    
    if int(row[1]) < greatest_decr:
        greatest_decr = int(row[1])
        greatest_decr_mth = row[0]

avg_chg = sum(mth_chg)/ len(mth_chg)

highest = max(mth_chg)
lowest = min(mth_chg)

print(f"Financial Analysis")
print(f"---------------------------")
print(f"Total Months: {tot_mths}")
print(f"Total: ${net_amt}")
print(f"Average Change: ${avg_chg:.2f}")
print(f"Greatest Increase in Profits:, {greatest_incr_mth}, (${highest})")
print(f"Greatest Decrease in Profits:, {greatest_decr_mth}, (${lowest})")