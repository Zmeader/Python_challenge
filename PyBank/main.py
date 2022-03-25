import os
import csv

# pull in the CSV file
pybank_csv = os.path.join("Resources", "budget_data.csv" )

#Lists used for the financials Analysis
total_months = 0
total_net_revenue = 0
current_net_revenue = 0
largest_increase = 0
p_l_changes = []
month_changes = []
prior_month_revenue = 0
current_month_revenue = 0
overall_PL_change = 0

print("Financial Analysis")
print("-----------------------")

#open and read the csv file
with open(pybank_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    
    #define the header line
    csv_header = next(csv_reader)
    
    for row in csv_reader:

        #Calculate the total months and net revenue
        total_months += 1
        current_month_revenue = int(row[1])
        total_net_revenue += current_month_revenue

        #create an if statement to update the total changes per month
        if (total_months == 1):
            prior_month_revenue = current_month_revenue
            

        else:
            overall_PL_change = current_month_revenue - prior_month_revenue

             #add each month to the list
            month_changes.append(row[0])
             #add each monthly change
            p_l_changes.append(overall_PL_change)
             #reset the previous month for the loop
            prior_month_revenue = current_month_revenue

 
    #calculate the sum and average 
    sum_p_l = sum(p_l_changes)
    average_p_l = round(sum_p_l/(total_months - 1), 2)

    #calculate the largest and smallest changes per each month
    largest_change = max(p_l_changes)
    smallest_change = min(p_l_changes)

    #find the largest and smallest via index
    largest_month = p_l_changes.index(largest_change)
    smallest_month = p_l_changes.index(smallest_change)

    #
    best_profit_month = month_changes[largest_month]
    worst_profit_month = month_changes[smallest_month]


print(f"Total Months:  {total_months}")
print(f"Total:  ${total_net_revenue}")
print(f"Average Change:  ${average_p_l}")
print(f"Greatest Increase in Profits:  {best_profit_month} (${largest_change})")
print(f"Greatest Decrease in Losses:  {worst_profit_month} (${smallest_change})")

    
pybank_output = os.path.join("Analysis", "pybank_output.txt")
with open(pybank_output, "w") as output:
    output.write("Financial Analysis")
    output.write('\n')
    output.write("-----------------------")
    output.write('\n')
    output.write(f"Total Months:  {total_months}")
    output.write('\n')
    output.write(f"Total:  ${total_net_revenue}")
    output.write('\n')
    output.write(f"Average Change:  ${average_p_l}")
    output.write('\n')
    output.write(f"Greatest Increase in Profits:  {best_profit_month} (${largest_change})")
    output.write('\n') 
    output.write(f"Greatest Decrease in Losses:  {worst_profit_month} (${smallest_change})")
    output.write('\n')

