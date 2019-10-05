import csv

# Open data file
with open("budget_data.csv") as file:
    read_file = csv.reader(file)
    budget_data = list(read_file)
    budget_data_header = budget_data[0] # Headers for data file
    budget_data = budget_data[1:] # Data file list

# Variable creation
month_count = 0
net_total = 0
greatest_increase = 0
greatest_decrease = 0

for row in budget_data:    
    month_count += 1 # Total number of months
    net_total += int(row[1])
    if int(row[1]) > greatest_increase:
        greatest_increase = int(row[1])
    if int(row[1]) < greatest_decrease:
        greatest_decrease = int(row[1])
    
print(month_count)
print(net_total)
print(net_total / month_count) # Print average
print(greatest_increase)
print(greatest_decrease)
