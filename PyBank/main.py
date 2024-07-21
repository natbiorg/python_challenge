#Module 3 
import os
import csv

# create a path to CSV file
# csvpath = os.path.join('Resources', 'budget_data.csv')
# I kept getting errors using a relative path so I switched to using an abolute file path
csvpath = "C:\\Users\\nwf91\\OneDrive\\Desktop\\VandyDataCourse\\Modules\\python-challenge\\python_challenge\\PyBank\\Resources\\budget_data.csv"

# List to store data 
dates = []
prof_loss = []
changes = []

# Open the csv file and create reader that understands ' as delimiter 
with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #skipping header row
    next(csvreader)
    
    #reading the file and adding values to list
    for row in csvreader: 
        # print(row)
        dates.append(row[0])
        prof_loss.append(row[1])
        prof_loss = list((map(int, prof_loss)))
        
# The total number of months included in the dataset
total_months = len(dates)
# print(round(total_months,2))

# The net total amount of "Profit/Losses" over the entire period
total = sum(prof_loss)
# print(round(total,2))

# Average change 
for i in range(1, len(prof_loss)):
    change = prof_loss[i] - prof_loss[i-1]
    changes.append(change)

average_change = sum(changes)/len(changes)
# print(round(average_change, 2))

# Greatest Increase/Decrease in Profits 
max_increase = max(changes)
max_increase_date = dates[changes.index(max_increase) + 1]  # Adding 1 to get the corresponding date

max_decrease = min(changes)
max_decrease_date = dates[changes.index(max_decrease) + 1]  # Adding 1 to get the corresponding date
# print(f'The greatest increase was {max_increase} on {max_increase_date}the greatest decrease was {max_decrease} on {max_decrease_date}')

# Print and export to text file 
file_path = "C:\\Users\\nwf91\\OneDrive\\Desktop\\VandyDataCourse\\Modules\\python-challenge\\python_challenge\\PyBank\\PyBankresults.txt"

with open(file_path, 'w') as file: 
    file.write(
    f"""
    Financial Analysis
    ----------------------------
    Total Months: {total_months}
    Total: ${total}
    Average Change: ${average_change:.2f}
    Greatest Increase in Profits: {max_increase_date} (${max_increase})
    Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})
    """
    )
