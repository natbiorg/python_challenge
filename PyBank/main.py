#Module 3 
import os
import csv

#create a path to CSV file
# csvpath = os.path.join('Resources', 'budget_data.csv')
## @GRADER: I kept getting errors using a relative path so I switched to using an abolute file path
csvpath = "C:\\Users\\nwf91\\OneDrive\\Desktop\\VandyDataCourse\\Modules\\python-challenge\\python_challenge\\PyBank\\Resources\\budget_data.csv"

#list to store data 
dates = []
prof_loss = []
change_profloss = []

#open the csv file and create reader that understands ' as delimiter 
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
        
# Initialize variables for change calculation

total_change = 0

#use len to find number of months 
total_months = len(dates)

print(total_months)
previous_profit_loss = prof_loss[0]



# Calculate the changes in Profit/Losses
for profit_loss in prof_loss[1:]:  # Start from the second month
    change = profit_loss - previous_profit_loss
    total_change += change
    previous_profit_loss = profit_loss

# Calculate the average change
average_change = total_change / (total_months - 1)  
print(f"Average Change is {average_change}. Total months is {total_months}. Total Change is {total_change}")
#Greatest Increase in Profits 

# Greatest Decrease in Profits 

# ## The Net Total Amount of Profit/Losses over the entire period 
# net_profloss = 0
# net_profloss += sum(prof_loss)
# print(net_profloss)

## Average Change 
avg_change = net_profloss/total_num_months
print(avg_change)

# for element in prof_loss: 
#         change_profloss = element =+ element -1 
    
# this is where i got lost and ran out of time. I will be resubmitting with finished version of homework asap 






