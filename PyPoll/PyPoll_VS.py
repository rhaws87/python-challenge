import csv
import os

PyPoll_csv = os.path.join("Resources","election_data.csv")

Number_Voters = []
Number_Votes = []
Candidates = []

count = 0
Votes = 0
Voters = 0

with open(PyPoll_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        Votes = Votes + 1
        
        Candidates = row[2]
        Number_Votes.append(row[0])

        
                
print("----------------------------------------------------------")

print("Election Results")

print("----------------------------------------------------------")

print("Total Votes: " + str(Votes))
print(str(Candidates))
