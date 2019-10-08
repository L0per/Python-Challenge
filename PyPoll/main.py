import csv

# Open data file
with open("election_data.csv") as file:
    read_file = csv.reader(file)
    election_data = list(read_file)
    election_data_header = election_data[0] # Headers for data file
    election_data = election_data[1:] # Data file list

# Casting
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

# Calculations
for row in election_data:
    total_votes += 1 # Total number of votes
    # Total votes for each candidate
    if row[2] == "Khan":
        khan_votes += 1
    elif row[2] == "Correy":
        correy_votes += 1
    elif row[2] == "Li":
        li_votes += 1
    elif row[2] == "O'Tooley":
        otooley_votes += 1

# Create dictionary with candidate votes, used for finding winner
max_dict = {"Khan" : khan_votes, "Correy" : correy_votes, "Li" : li_votes, "O'Tooley" : otooley_votes}

# Find max value in dictionary and prints associated key (candidate)
print(max(max_dict, key=max_dict.get))



#  Election Results
#  -------------------------
#  Total Votes: 3521001
#  -------------------------
#  Khan: 63.000% (2218231)
#  Correy: 20.000% (704200)
#  Li: 14.000% (492940)
#  O'Tooley: 3.000% (105630)
#  -------------------------
#  Winner: Khan
#  -------------------------
