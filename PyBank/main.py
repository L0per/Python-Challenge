import csv

# Open data file
with open("budget_data.csv") as file:
    read_file = csv.reader(file)
    budget_data = list(read_file)
    budget_data_header = budget_data[0] # Headers for data file
    budget_data = budget_data[1:] # Data file list

# Casting
month_count = 0
net_total = 0
greatest_increase = 0
greatest_decrease = 0
previous_row_value = 0
average_change_list = []

# Calculations
for row in budget_data:    
    month_count += 1 # Total number of months
    net_total += int(row[1])
    profit_change = int(row[1])-previous_row_value
    if profit_change > greatest_increase: # Greatest increase in profits
        greatest_increase = profit_change
        greatest_increase_date = row[0]
    if profit_change < greatest_decrease: # Greatest decrease in profits
        greatest_decrease = profit_change
        greatest_decrease_date = row[0]
    average_change_list.append(profit_change)
    previous_row_value = int(row[1])

average_change_list.pop(0) # Removing first value since it is not a change
average_change = round(sum(average_change_list)/len(average_change_list), 2) # Average change in profits, rounded to 2 decimals

# Print results to terminal
print(f'''
Financial Analysis
------------------------------
Total Months: {month_count}
Total: ${net_total}
Average Change: ${average_change}
Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})
Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})
''')

# Print results to CSV
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


