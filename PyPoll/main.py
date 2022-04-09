import csv
import os

#create empty array for candidates
candidates = []

#import csv and input content into array
csvpath = os.path.join('Resources','election_data.csv')
with open(csvpath, newline ='') as csvfile:
    election = csv.reader(csvfile)
    header = next(election)

    #enter each candidate name into array
    for row in election:
        candidates.append(row[2])

#create empty dictionary for list of candidates
votes = {}

#loop through array and enter new names into dictionary. If already exists, add count
for name in candidates:
    if name not in votes:
        votes[name] = 1
    else:
        votes[name] += 1

winner = 0

#formatted outputs
print("\nElection Results\n-------------------------")
print(f"Total Votes: {len(candidates)}\n-------------------------")

for name,count in votes.items():
    percent = count/len(candidates)
    percent = "{:.3%}".format(percent)
    print(f"{name}: {percent} ({count})")

    if count > winner:
        winner_name = name
        winner = count

print("-------------------------")


print(f"Winner: {winner_name}\n-------------------------\n")

#Output to Text File in Analysis Folder
txt_file = open("analysis\Result.txt","w")

txt_file.write("Election Results\n-------------------------\n")
txt_file.write(f"Total Votes: {len(candidates)}\n-------------------------\n")

for name,count in votes.items():
    percent = count/len(candidates)
    percent = "{:.3%}".format(percent)
    txt_file.write(f"{name}: {percent} ({count})\n")

    if count > winner:
        winner_name = name
        winner = count

txt_file.write("-------------------------\n")
txt_file.write(f"Winner: {winner_name}\n-------------------------\n")

txt_file.close()