#Module 3 
import os
import csv

#create a path to CSV file
csvpath = os.path.join("C:/Users/nwf91/anacoda3.1/envs/python_challenge/python_challenge/PyBank/Resources/budget_data.csv")

#list to store data 
dates = []
prof_loss = []
change_profloss = []

#open the csv file and create reader that understands ' as delimiter 
with open(csvpath, encoding='UTF-8') as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #skipping header row
    next(csvreader)
    
    #reading the file and adding values to list
    for row in csvreader: 
        
        dates.append(row[0])
        prof_loss.append(row[1])
        prof_loss = list((map(int, prof_loss)))
        
        
# print(prof_loss)

#use len to find number of months 
total_num_months = len(dates)
# print(total_num_months)

#finding net total amount of profit/losses, first set var to 0, then define it as sum of prof/loss values
#learned that i have to use sum() because prof_loss is a list from Xpert Learning Assistant
net_prof_loss = 0
net_prof_loss += sum(prof_loss)
# print(net_prof_loss)

#finding avg change
# for element in prof_loss: 
#         change_profloss = element =+ element -1 
    
# this is where i got lost and ran out of time. I will be resubmitting with finished version of homework asap 






