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

# Calculations
for row in budget_data:    
    month_count += 1 # Total number of months
    net_total += int(row[1])
    if int(row[1]) > greatest_increase: # Greatest increase in profits
        greatest_increase = int(row[1])
        greatest_increase_date = row[0]
    if int(row[1]) < greatest_decrease: # Greatest decrease in profits
        greatest_decrease = int(row[1])
        greatest_decrease_date = row[0]

average_change = round((net_total / month_count), 2) # Average change in profits, rounded to 2 decimals

# Printing results to terminal
print(f'''
Financial Analysis
------------------------------
Total Months: {month_count}
Total: ${net_total}
Average Change: ${average_change}
Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})
Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})
''')

# Printing results to CSV
# Create CSV file
with open("budget_data_summary.csv", 'w', newline='') as newfile:
    newfilewriter = csv.writer(newfile)
    newfilewriter.writerows([
        ["Financial Analysis"],
        ["------------------------------"],
        [f'Total Months: {month_count}'],
        [f'Total: ${net_total}'],
        [f'Average Change: ${average_change}'],
        [f'Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})'],
        [f'Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})']])

    #newfilewriter.writerow(["------------------------------"])
    #newfilewriter.writerow([f'Average Change: ${average_change}'])

