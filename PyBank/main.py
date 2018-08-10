import os
import csv

# Pull in CSV file
budget_data = "Resources/budget_data.csv"

# Variables
total_months = 0
total_rev = 0

prev_rev = 0
rev_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999]

rev_changes = []

# Read Files
with open(budget_data) as rev_data:
    reader = csv.DictReader(rev_data)

    # Loop through all the rows
    for row in reader:

        # Calc totals
        total_months = total_months + 1
        total_rev = total_rev + int(row["Revenue"])
        # print(row)

        # Keep track of changes
        rev_change = int(row["Revenue"]) - prev_rev
        #print(rev_change)

        # Reset the value of prev_rev to be current
        prev_rev = int(row["Revenue"])
        # print(prev_rev)

        # Get the greatest increase - conditional
        if (rev_change > greatest_increase[1]):
            greatest_increase[1] = rev_change
            greatest_increase[0] = row["Date"]
         
        # Get the greatest decrease - conditional 
        if (rev_change < greatest_decrease[1]):
            greatest_decrease[1] = rev_change
            greatest_decrease[0] = row["Date"]

        # Add to the rev_changes list
        rev_changes.append(rev_change)
        #print(rev_changes)

    # Set the Revenue average
    # sum of rev changes minus - the first line / num of rev changes - first line
    rev_avg = (sum(rev_changes) - rev_changes[0]) / (len(rev_changes) -1)
    #print("Average Change: " + str(rev_avg))

    
    
    print()
    print("Financial Analysis")
    print("-----------------------")
    print("Total Months: " + str(total_months))
    print("Total Revenue: " + "$" + str(int(total_rev)))
    print("Average Change: " + "$" + str(rev_avg))
    print("Greatest Increase: " + str(greatest_increase[0]) + " ($" +  str(greatest_increase[1]) + ")") 
    print("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" +  str(greatest_decrease[1]) + ")")


