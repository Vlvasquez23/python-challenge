#Assignment 3: Python Homework - Py Me Up, Charlie (PyPoll)

import os
import csv

#Variables
voterids= [] 
counties = [] 
candidates = [] 
candidate_names = [] 
total_per_cand = [] 
results_print = [] 
total_perc_cand = [] 
line_count = 1
loop_candidates = 0
loop_vote_ct = 0
runner_up_up_votes = 0
winner_votes = 0
loop_high_low = 0
loop_results = 0
   
csvpath = os.path.join('.','python-challenge', 'PyPoll', 'Resources', 'election_data.csv')

with open(csvpath, newline='') as csvfile:
       
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)
    row = next(csvreader)


    for row in csvreader:
        voterid=row[0] 
        county=row[1] 
        candidate=row[2] 
        voterids.append(voterid) 
        counties.append(county) 
        candidates.append(candidate) 
    
    #Count the total number of votes cast in the "Voter ID" column
    line_count= len(voterids)
    
#Find first candidate name to compare
candidate_names.append(candidates[0]) 

#Loop through the list of candidates to determine candidates voted for 
for loop_candidates in range (line_count-1):
    if candidates[loop_candidates+1] != candidates[loop_candidates] and candidates[loop_candidates+1] not in candidate_names:
        candidate_names.append(candidates[loop_candidates+1])

n=len(candidate_names)

#Range of loop depending on how many candidates were found
for loop_vote_ct in range (n): 
    total_per_cand.append(candidates.count(candidate_names[loop_vote_ct])) 

runner_up_votes=line_count 

for loop_high_low in range(n): 
    #Calculate % per candidate found
    total_perc_cand.append(f'{round((total_per_cand[loop_high_low]/line_count*100), 4)}%') 

    #Find candidate with highest vote count
    if total_per_cand[loop_high_low]>winner_votes: 
        winner=candidate_names[loop_high_low]
        winner_votes=total_per_cand[loop_high_low]

     #Find candidate with lowest vote count   
    if total_per_cand[loop_high_low]<runner_up_votes: 
        runner_up=candidate_names[loop_high_low]
        runner_up_votes=total_per_cand[loop_high_low]

for loop_results in range(n):
    results_print.append(f'{candidate_names[loop_results]}: {total_perc_cand[loop_results]} ({total_per_cand[loop_results]})') 

resultlines='\n'.join(results_print) 

# Print Analysis
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {line_count}")
print(f"-------------------------")
print(f"-------------------------")
print(f"Winner: {winner}")


# Path to output text file
output_file = os.path.join('.', 'python-challenge', 'PyPoll', 'Analysis', 'PyPoll.txt')

# Open File Using "Write" Mode. 
with open(output_file, 'w',) as txtfile:

# Text Data
    txtfile.write(f"Election Results\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Votes: {line_count}\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"{resultlines}\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write(f"---------------------------\n")    