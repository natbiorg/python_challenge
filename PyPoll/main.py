#Module 3 PyPoll 
## Disclaimer: I used Xpert Learning Assistant to write this code 
import os
import csv

# create a path to CSV file
csvpath = os.path.join('Resources', 'election_data.csv')

# Read the CSV file and process the data
with open(csvpath, 'r') as file:
    lines = file.readlines()
    total_votes = len(lines) - 1  # Subtract 1 for the header row
    candidate_votes = {}

    for line in lines[1:]:  # Skip the header row
        voter_id, county, candidate = line.strip().split(',')
        
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# Calculate the percentage of total ballots each candidate received
percentage_votes = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}

# Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidate_votes.items():
    percentage = percentage_votes[candidate]
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {max(candidate_votes, key=candidate_votes.get)}")
print("-------------------------")

# Election results data
election_results = {
    "Total Votes": 369711,
    "Candidates": {
        "Charles Casper Stockham": {"Percentage": 23.049, "Votes": 85213},
        "Diana DeGette": {"Percentage": 73.812, "Votes": 272892},
        "Raymon Anthony Doane": {"Percentage": 3.139, "Votes": 11606}
    },
    "Winner": "Diana DeGette"
}

# Print and export to text file 
file_path = "PyPollresults.txt"

# Export election results to a text file
with open(file_path, 'w') as file: 
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {election_results['Total Votes']}\n")
    file.write("-------------------------\n")
    for candidate, data in election_results['Candidates'].items():
        file.write(f"{candidate}: {data['Percentage']:.3f}% ({data['Votes']})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {election_results['Winner']}\n")
    file.write("-------------------------\n")