import os
import csv
budget_data = os.path.join("Resources", "budget_data.csv") 
with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    Total_months=[]
    Net_amount=[]
    Average_change=[]
# The total number of months and total profile/loss included in the dataset  
    for row in csvreader:
        Total_months.append(row)
        Net_amount.append(int(row[1]))
# Loop monthly change of average "Profit/Losses" over the entire period
    for i in range(len(Net_amount)-1):
        Average_change.append(Net_amount[i + 1]- Net_amount[i]) 
print ("----------------------")       
print("Financial Analysis :")
print ("----------------------")
print("Total Month:$" + str(len(Total_months)))
print("Total:$"+ str(sum(Net_amount)))
print("Average Change :$"+ str(int(sum(Average_change) /len(Average_change))))
# The greatest increase /decrease in profits over the entire period
print("Greatest Increase in Profits:$" +     str(max(Average_change)))
print("Greatest Decrease in Profits:$" +     str(min(Average_change)))
print ("----------------------------------------------------------")