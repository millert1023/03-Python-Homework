#import csv
import os
import csv

# Path to collect data from the Resources folder
budget_data_csv= os.path.join("..", "PyBank", "Resources","budget_data.csv")

#Default Variables
total_months = 0
net_amount = 0
monthly_change = []
month_count = []
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month = 0

#Open and Read csv
with open(budget_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csvheader = next(csvreader)
    row = next(csvreader)

    previous_row = int(row[1])
    total_months = total_months + 1
    net_amount = net_amount + int(row[1])
    greatest_increase = int(row[1])
    greatest_increase_month = row[0]

    for row in csvreader:
        #Count in total of months
        total_months = total_months + 1
        
        #Calculate the total revenue over the entire period
        net_amount = net_amount + int(row[1])
        
        #Calculate the change in revenue between month over the entire period
        rev_change = int(row[1]) - previous_row
        monthly_change.append(rev_change)
        previous_row = int(row[1])
        month_count.append(row[0])
        
        #The greatest increase in revenue (date and amount) over the entire period
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]

        #The greatest decrease in revenue (date and amount) over the entire period
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row [0]

        #Calculate the average
        average_change = round(sum(monthly_change)/len(monthly_change),2)

        High = max(monthly_change)
        Low = min(monthly_change)
        
#print
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total:  ${net_amount}")
print(f"Average Change: ${average_change}")
print(f"Greatest increase in Profits:  {greatest_increase_month},(${High})")
print(f"Greatest decrease in Profits:  {greatest_decrease_month},(${Low})")

#write output
output_file = os.path.join ("..","Pybank", "output.txt")

with open(output_file,'w', newline='') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total:  ${net_amount}\n")
    txtfile.write(f"Average Change: ${average_change}\n")
    txtfile.write(f"Greatest increase in Profits:  {greatest_increase_month},(${High})\n")
    txtfile.write(f"Greatest decrease in Profits:  {greatest_decrease_month},(${Low})\n")
    

