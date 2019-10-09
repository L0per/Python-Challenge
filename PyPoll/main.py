import csv

# Open data file
with open("election_data.csv") as file:
    read_file = csv.reader(file)
    election_data = list(read_file)
    election_data_header = election_data[0] # Headers for data file
    election_data = election_data[1:] # Data file list

# Casting
total_votes = 0

# Create dictionary for tallying votes
vote_dict = {}
for row in election_data:
    total_votes += 1
    if row[2] not in vote_dict.keys():
        vote_dict[row[2]] = 1
    else:
        vote_dict[row[2]] += 1

# Find max value in dictionary
winner = max(vote_dict, key=vote_dict.get)

# Print results to terminal
print(f'''
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
{list(vote_dict.keys())[0]}: {round((vote_dict[list(vote_dict.keys())[0]]/total_votes)*100,2)}% ({vote_dict[list(vote_dict.keys())[0]]})
{list(vote_dict.keys())[1]}: {round((vote_dict[list(vote_dict.keys())[1]]/total_votes)*100,2)}% ({vote_dict[list(vote_dict.keys())[1]]})
{list(vote_dict.keys())[2]}: {round((vote_dict[list(vote_dict.keys())[2]]/total_votes)*100,2)}% ({vote_dict[list(vote_dict.keys())[2]]})
{list(vote_dict.keys())[3]}: {round((vote_dict[list(vote_dict.keys())[3]]/total_votes)*100,2)}% ({vote_dict[list(vote_dict.keys())[3]]})
-------------------------
Winner: {winner}
-------------------------
''')

# Print to CSV
with open("election_data_summary.csv", 'w', newline='') as newfile:
    newfilewriter = csv.writer(newfile)
    newfilewriter.writerows([
        ["Election Results"],
        ["-------------------------"],
        [f'Total Votes: {total_votes}'],
        ["-------------------------"],
        [f'{list(vote_dict.keys())[0]}: {round((vote_dict[list(vote_dict.keys())[0]]/total_votes)*100,2)}% ({vote_dict[list(vote_dict.keys())[0]]})'],
        [f'{list(vote_dict.keys())[1]}: {round((vote_dict[list(vote_dict.keys())[1]]/total_votes)*100,2)}% ({vote_dict[list(vote_dict.keys())[1]]})'],
        [f'{list(vote_dict.keys())[2]}: {round((vote_dict[list(vote_dict.keys())[2]]/total_votes)*100,2)}% ({vote_dict[list(vote_dict.keys())[2]]})'],
        [f'{list(vote_dict.keys())[3]}: {round((vote_dict[list(vote_dict.keys())[3]]/total_votes)*100,2)}% ({vote_dict[list(vote_dict.keys())[3]]})'],
        ["-------------------------"],
        [f'Winner: {winner}'],
        ["-------------------------"]])