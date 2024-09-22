# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("./Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("./Analysis", "election_analysis.txt")  # Output file path
os.chdir("/Users/wayne.mitchell/Documents/NU/python-challenge/PyPoll")
print(f"cwd: {os.getcwd()}")
print()

# Initialize variables to track the election data
total_votes = 0  

# Define lists and dictionaries to track candidate names and vote counts
total_votes = 0
candidate_votes = 0
this_candidate_percent_vote = 0.0
best_candidate_vote = 0
winner = ""
this_candidate_total_vote = 0
candidates = []

# Winning Candidate and Winning Count Tracker
election_tracker = {
    "Charles Casper Stockham" : [this_candidate_total_vote, this_candidate_percent_vote],
    "Diana DeGette" : [this_candidate_total_vote, this_candidate_percent_vote],
    "Raymon Anthony Doane" : [this_candidate_total_vote, this_candidate_percent_vote]
}

# function: calculate percentage of vote 
def calculate_vote_percent(total_votes, candidate_votes):
    percent_vote = round((candidate_votes/ total_votes)*100, 3)
    return percent_vote

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate_name = row[2]

        # If the candidate is not already in the candidate list, add them
        if not candidate_name in candidates:
            candidates.append(candidate_name)

        # If candidate is not in 'election_tracker', add 
        if not candidate_name in election_tracker.keys():
            votes_percent_by_candidate[candidate_name] = 0.0

        # Add a vote to the candidate's count
        election_tracker[candidate_name][0] += 1

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    print(f"\nTotal votes cast: {total_votes}")
    print()

    # Write the total vote count to the text file
    print(f"\nSUMMARY\n --- Election Results ---\n\n{'-'*25}\n", file = txt_file)
    print(f"Total Votes: {total_votes}\n", file = txt_file)
    print(f"{'-'*25}\n", file = txt_file)
    # Loop through the candidates to determine vote percentages and 
    # identify the winner
    for candidate in candidates:

        # Get the vote count and calculate the percentage
        this_candidate_vote_total = election_tracker[candidate][0]
        this_candidate_percent_vote = calculate_vote_percent\
                                      (total_votes, this_candidate_vote_total)
        
        election_tracker[candidate][1] = this_candidate_percent_vote

        # Update the winning candidate if this one has more votes
        if this_candidate_vote_total > best_candidate_vote:
            winner = candidate
            best_candidate_vote = this_candidate_vote_total

        # Print to screen and save each candidate's vote count and percentage
        print(f"{candidate}: {this_candidate_percent_vote}% ({this_candidate_vote_total})\n")

    # Generate and print the winning candidate summary
    print(f"\n\n\n\n\nSUMMARY\n   --- Election Results ---\n\n{'-'*25}\n")
    print(f"Total Votes: {total_votes}\n")

    for candidate in candidates:
        this_candidate_vote_total = election_tracker[candidate][0]
        this_candidate_percent_vote = election_tracker[candidate][1]
        print(f"{candidate}: {this_candidate_percent_vote}% ({this_candidate_vote_total})\n")
    
    print(f"{'-'*25}\n\nWinner: {winner}\n\n{'-'*25}\n")

    # Save the winning candidate summary to the text file
    for candidate in candidates:
        this_candidate_vote_total = election_tracker[candidate][0]
        this_candidate_percent_vote = election_tracker[candidate][1]
        print(f"{candidate}: {this_candidate_percent_vote}% ({this_candidate_vote_total})\n",file = txt_file)

    print(f"{'-'*25}\n\nWinner: {winner}\n\n{'-'*25}\n", file = txt_file)
 
  
