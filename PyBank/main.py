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
        greatest_increase_date = row[0]
    if int(row[1]) < greatest_decrease:
        greatest_decrease = int(row[1])
        greatest_decrease_date = row[0]

print(f'''
Financial Analysis
------------------------------
Total Months: {month_count}
Total: ${net_total}
Average Change: ${round((net_total / month_count), 2)}
Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})
Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})
''')

