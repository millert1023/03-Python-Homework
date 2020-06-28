#import csv
import os
import csv

# Path to collect data from the Resources folder
budget_data_csv= os.path.join("..", "PyPoll", "Resources","election_data.csv")

#Default Variables
total_votes = 0
candidates = {}
can_perc = {}
winner_count = 0

#Open and Read csv
with open(budget_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    row = next(csvreader,None)

    for row in csvreader:
        #Calculate the total numbers of votes cast
        total_votes = total_votes + 1

        #Count Complete list of candidates who received votes and their vote counts
        if row [2] in candidates.keys():
            candidates[row[2]] = candidates[row[2]] + 1

        else:
            candidates[row[2]] = 1

        

        #Calculate the percentage of votes each candidate won
        for key, value in candidates.items():
            can_perc[key] = round((value/total_votes)*100, 4)

        #Determine the winner of the election
        for key in candidates.keys():
            if candidates[key] > winner_count:
                winner = key
                winner_count = candidates[key]

#print
print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------")
for key, value in candidates.items():
    print(f"{key} {can_perc[key]}% ({value})")
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")

#write output
output_file = os.path.join ("..","PyPoll", "output.txt")

with open(output_file,'w', newline='') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("----------------------------\n")
    for key, value in candidates.items():
        txtfile.write(f"{key} {can_perc[key]}% ({value})\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("----------------------------\n")
