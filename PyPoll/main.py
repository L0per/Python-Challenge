import csv

# Open data file
with open("election_data.csv") as file:
    read_file = csv.reader(file)
    election_data = list(read_file)
    election_data_header = election_data[0] # Headers for data file
    election_data = election_data[1:] # Data file list

# Casting
total_votes = 0

# Calculations


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
