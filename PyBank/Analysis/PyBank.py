#import modules
import os 
import csv


#set path for csv file
csvpath = os.path.join("Desktop", "GitHub", "python_challenge", "PyBank", "Resources", "budget_data.csv")


#open csv 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    print(csvreader)
    
    #creates lists for data
    csv_header = next(csvreader)
    total_months = []
    total = []
    monthly_changes = []
    popped_list = []
    increase = []
    decrease = []

    # set variables as integers
    total_profit = 0 
    profit_change = 0
    greatest_increase = 0
    greatest_decrease = 0

    print(f"CSV Header: {csv_header}")
    
    #reads each row of data
    for row in csvreader:
        #append makes row 0 into list
        total_months.append(row[0])
        
        #append makes row 1 into list
        total.append(row[1])
        #sum of values in row 1
        total_profit = total_profit + int(row[1])

        #for change in profits/losses
    for i in range(len(total) -1):
        #set variable to equal difference between values row to row
        profit_change = int(total[i+1]) - int(total[i])
        #append variable to a list named monthly_changes
        monthly_changes.append(profit_change)
        
        #ran check on list by printing monthly_changes and comparing list elements to manually determined values from excel file, 
        #saw that the first value in list was counted twice so used pop method 
            
        #set variable to equal to sum of values in list
        sum_list = sum(monthly_changes)
        #set variable to equal sum_list divided by number of values in list
        average_change = sum_list / len(monthly_changes)
            
        #greatest increase
        greatest_increase = max(monthly_changes)
        #look for corresponding row number
        month_index = monthly_changes.index(greatest_increase)
        #set variable for readout of corresponding row information, +1 for next row 
        increase_month = total_months[month_index+1]
        
        #greatest decrease
        greatest_decrease = min(monthly_changes)
        #look for corresponding row number
        month_index2 = monthly_changes.index(greatest_decrease)
        #set variable for readout of corresponding row information, +1 for next row 
        decrease_month = total_months[month_index2+1]
        
        
   
    print(monthly_changes)
    print(average_change)
    print(str(total_profit))
    print(len(total_months))
    print(greatest_increase)
    print(month_index)
    print(increase_month)

    print(greatest_decrease)
    print(month_index2)
    print(decrease_month)

    
    
        