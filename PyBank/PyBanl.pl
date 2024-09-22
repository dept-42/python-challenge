# -*- coding: UTF-8 -*-
"""PyBank.py"""

# Dependencies
import csv
import os

# Files to load and output
file_to_load = os.path.join("./Resources", "budget_data.csv") 
file_to_output = os.path.join("./Analysis", "budget_analysis.txt") 
os.chdir("/Users/wayne.mitchell/Documents/NU/python-challenge/PyBank")
print(f"cwd: {os.getcwd()}")
print()

# Define variables to track the financial data
total_months = 0
total_profit_and_loss = 0 # sum of profit and loss for all months
total_net_pl_change = 0 # sum of changes in P/L from one month to the next
monthly_net_PL_change = 0 # one month to month PL change

greatest_profit_and_loss_tracker = {
    "profit" : {
        "date" : "",
        "amount" : 0
    },
    "loss" : {
        "date" : "",
        "amount" : 0
    }
}
day_month = ''

previous_month = ''
this_month = ''
date = ''

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    date = first_row[0]
    day_month = date.split('-')
    previous_month = day_month[0]
    total_months += 1

    # Track 'total_profit_and_loss' (no 'total_net_pl_change' in first month)
    previous_monthly_profit_or_loss = int(first_row[1])
    total_profit_and_loss = int(first_row[1])

    # Process each row of data
    for row in reader:
        date = row[0]
        day_month = date.split('-')
        this_month = day_month[0]

        # to track and count months, set  'currentMonth' at first row, set \
        # monthCount = 1.  For each additional row, inspect month and capture \
        # as 'nextMonth'. If 'nextMonth != currentMonth, increment monthCount \
        # by 1, set currentMonth to nextMonth. In this data, the number of \
        # non-header rows equals the number of months months, but, that might 
        # not alwys be true; a four week period would occur twice in some months\
        # The method here will correctly count NUMBER OF MONTHS even if two \
        # reports are made in a single month

        if this_month != previous_month: 
            total_months += 1
            previous_month = this_month

        # Track the individual net PL change last month to this month
        this_monthly_profit_or_loss = int(row[1])
      
        #adjust 'total_net_profit_and_loss'
        total_profit_and_loss += this_monthly_profit_or_loss
        
        # calculate 'monthly_net_PL_change'
        monthly_net_PL_change = this_monthly_profit_or_loss - \
            previous_monthly_profit_or_loss
        
        # adjust 'total_net_pl_change'
        total_net_pl_change += monthly_net_PL_change
        
        if monthly_net_PL_change > greatest_profit_and_loss_tracker["profit"]["amount"]:
            greatest_profit_and_loss_tracker["profit"]["date"] = date
            greatest_profit_and_loss_tracker["profit"]["amount"] = monthly_net_PL_change 
        elif monthly_net_PL_change < greatest_profit_and_loss_tracker["loss"]["amount"]:
            greatest_profit_and_loss_tracker["loss"]["date"] = date
            greatest_profit_and_loss_tracker["loss"]["amount"] = monthly_net_PL_change 

        # up date 'previous_profit_loss'
        previous_monthly_profit_or_loss = this_monthly_profit_or_loss

    # print the total months
    print(f"final total_months {total_months}")

# calculate 'average_profit_loss_change'
average_profit_loss_change = round(int(total_net_pl_change) / (total_months-1), 2)
print(f"Average profit loss change: {average_profit_loss_change}")

# Generate the output summary

gpa = greatest_profit_and_loss_tracker["profit"]["amount"]
gpd = greatest_profit_and_loss_tracker["profit"]["date"]

gla = greatest_profit_and_loss_tracker["loss"]["amount"]
gld = greatest_profit_and_loss_tracker["loss"]["date"]

print(f"greatest profit date: {gpd} and amount {gpa}")
print(f"greatest loss date: {gld} and amount {gla}")

# Print the output
print("--- FINANCIAL ANALYSIS SUMMARY ---\n")
print(f"{'-'*25}\n")
print(f"Total Months: {total_months}\n")
print(f"Total Net Profit/Loss: ${total_profit_and_loss}\n")
print(f"Total Net Profit/Loss change : ${total_net_pl_change}\n")
print(f"Average Change: ${average_profit_loss_change}\n")
print(f"Greatest Increase in Profits: {gpd} (${gpa})\n")
print(f"Greatest Decrease in Profits: {gld} (${gla})\n")

# Write the results to a text file
with open(file_to_output, "w", encoding='utf-8') as txt_file:
    print(f"\nSUMMARY\n --- Financial Report ---\n\n{'-'*25}\n", file = txt_file)
    print(f"Total Months: {total_months}\n", file = txt_file)
    print(f"Total: ${total_profit_and_loss}\n", file = txt_file)
    print(f"Average Change: ${average_profit_loss_change}\n", file = txt_file)
    print(f"Greatest Increase in Profits: {gpd} (${gpa})\n", file = txt_file)
    print(f"Greatest Decrease in Profits: {gld} (${gla})\n", file = txt_file)