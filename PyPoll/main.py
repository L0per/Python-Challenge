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
-------------------------''')
for i in range(0,len(vote_dict)):
    print(f'{list(vote_dict.keys())[i]}: {round((vote_dict[list(vote_dict.keys())[i]]/total_votes)*100,2)}% ({vote_dict[list(vote_dict.keys())[i]]})')
print(f'''
-------------------------
Winner: {winner}
-------------------------
''')

# Print results to CSV
with open("election_data_summary.csv", 'w', newline='') as newfile:
    newfilewriter = csv.writer(newfile)
    newfilewriter.writerows([
        ["Election Results"],
        ["-------------------------"],
        [f'Total Votes: {total_votes}'],
        ["-------------------------"]
    ])
    for i in range(0,len(vote_dict)):
        newfilewriter.writerows([
        [f'{list(vote_dict.keys())[i]}: {round((vote_dict[list(vote_dict.keys())[i]]/total_votes)*100,2)}% ({vote_dict[list(vote_dict.keys())[i]]})']
    ])
    newfilewriter.writerows([
        ["-------------------------"],
        [f'Winner: {winner}'],
        ["-------------------------"]
    ])