# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("./Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("./Analysis", "budget_analysis.txt")  # Output file path
os.chdir("/Users/wayne.mitchell/Documents/NU/python-challenge/PyBank")
print(f"cwd: {os.getcwd()}")
print()
# Define variables to track the financial data
total_months = 0
net_total_profit_and_loss = 0 # sum of prot _ loss for aall months
net_total_change = 0 # sum of change in P/L from one month to the next

monthly_net_profit_loss = 0
previous_profit_loss = 0
this_profit_loss = 0

monthToMonthChange = 0
monthToMonthProfit = 0
monthToMonthLoss = 0

greatest_profit_loss = {
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
# to track and count months, set  'currentMonth' at first row, set monthCount
# to 1.  For each additional row, inspect month and capture as 'nextMonth'. If 
# 'nextMonth != currentMonth, increment monthCount by 1, set currentMonth to 
# nextMonth. In this data, the number of non-header rows equals months, but, that
# might not alwys be true. This method will coorectly count months even if two
# reports are made in a single month
month_count = 0
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
    print(f"day_month: {day_month}")
    previous_month = day_month[0]
    print(f"previous_month : {previous_month }")
    total_months += 1
    print(f"month_count {month_count}")

    # Track the total and net change
    previous_profit_loss = int(first_row[1])
    #previous_profit_loss = int(previous_profit_loss)

    print(f">>>>> previous_profit_loss type {type(previous_profit_loss)}")

    # takes care of edge case where the first profit or loss happens to be
    # the greatest
    if previous_profit_loss > 0:
        greatest_profit_loss["profit"]["date"] = date
        greatest_profit_loss["profit"]["amount"] = previous_profit_loss
    elif previous_profit_loss < 0:
        greatest_profit_loss["loss"]["date"] = date
        greatest_profit_loss["loss"]["amount"] = previous_profit_loss
    else:
        greatest_profit_loss["profit"]["date"] = date
        greatest_profit_loss["profit"]["amount"] = 0
        greatest_profit_loss["loss"]["date"] = date
        greatest_profit_loss["loss"]["amount"] = 0

    total_change = previous_profit_loss
    #net_total_change = previous_profit_loss
    #net_total_amount = previous_profit_loss
    # Process each row of data
    for row in reader:
        date = row[0]
        day_month = date.split('-')
        this_month = day_month[0]
        print(f"this_month {this_month} previous_month {previous_month}")

        if this_month != previous_month: # type: ignore
            print(f">>>>this_month {this_month} current_month {previous_month}")
            total_months += 1
            print(f"total_months {total_months}")
            previous_month = this_month

        # Track the net change QUESTION -- change from month to month? 
        # or change from begining to current report which could be net + or -
        # ? 
        this_profit_loss = int(row[1])
        #this_profit_loss = int(this_profit_loss)
        
        #adjust 'net_total_profit_and_loss'
        net_total_profit_and_loss += this_profit_loss
        
        # calculate 'monthly_net_profit_loss'
        monthly_net_profit_loss = this_profit_loss - previous_profit_loss
        
        # adjust 'net_total_change'
        net_total_change += monthly_net_profit_loss
        
        # update greatest increase/ decrease
        #if monthly_net_profit_loss < 0 :
        #    print(f"NEGATIVE!")
        #print(f"monthly_net_profit_loss:  {monthly_net_profit_loss}")

        # adjust net_total_amount
        #print(f"old net_total_amount:  { net_total_amount}")
        #net_total_amount += monthly_net_profit_loss
        #print(f"new net_total_amount:  { net_total_amount}")

        #### update greatest increase/ decrease
        # Calculate the greatest increase in profits (month and amount) and
        #  the greatest decrease in losses (month and amount)
        # adjust 'greatestMonthToMonthProfit' or 'greatestMonthToMonthLoss'
        #if ( (monthly_net_profit_loss > 0) & (monthly_net_profit_loss > \
                             # greatest_profit_loss["profit"]["amount"]) ):
            #greatest_profit_loss["profit"]["date"] = date
            #greatest_profit_loss["profit"]["amount"] = monthly_net_profit_loss
       # elif ( (monthly_net_profit_loss) < 0 & (monthly_net_profit_loss < \
            #                    greatest_profit_loss["loss"]["amount"]) ):
            #greatest_profit_loss["loss"]["date"] = date
            #greatest_profit_loss["loss"]["amount"] = monthly_net_profit_loss


        if monthly_net_profit_loss > greatest_profit_loss["profit"]["amount"]:
            greatest_profit_loss["profit"]["date"] = date
            greatest_profit_loss["profit"]["amount"] = monthly_net_profit_loss
        elif monthly_net_profit_loss < greatest_profit_loss["loss"]["amount"]:
            greatest_profit_loss["loss"]["date"] = date
            greatest_profit_loss["loss"]["amount"] = monthly_net_profit_loss
        # up date 'previous_profit_loss'
        previous_profit_loss = this_profit_loss

    # print the total months
    print(f"final total_months {total_months}")

# Calculate the average net change across the months
# total change  / number of months
print(f"net_total_profit_and_loss: {net_total_profit_and_loss}")
#print(f"net_total_amount{net_total_amount}")
print(f"total months {total_months}")

## ! NO ????  need to accumulate monthly changes in a list then take the average
average_profit_loss_change = round(int(net_total_change) / (total_months-1), 2)
print(f"Average profit loss change: {average_profit_loss_change}")

gpa = greatest_profit_loss["profit"]["amount"]
gpd = greatest_profit_loss["profit"]["date"]

gla = greatest_profit_loss["loss"]["amount"]
gld = greatest_profit_loss["loss"]["date"]

print(f"greatest profit date: {gpd} and amount {gpa}")
print(f"greatest loss date: {gld} and amount {gla}")
# Generate the output summary


# Print the output


# Write the results to a text file
#with open(file_to_output, "w", encoding='utf-8') as txt_file:
#   txt_file.write(output)
