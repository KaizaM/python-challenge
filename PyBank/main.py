import csv
import os

#make empty arrays to input the csv data into
dates = []
money = []


csvpath = os.path.join("Resources","budget_data.csv")
with open(csvpath,newline ='') as csvfile:
    budget = csv.reader(csvfile)
    header = next(budget)

    #go through each row of csv to calculate the number of months, total profit, average change, and greatest increase/decrease month
    for row in budget:
        #make an array of dates and profits/losses
        dates.append(row[0])
        money.append(int(row[1]))

#count for indexing of array
profit = sum(money)
count = 0
greatestI = 0
greatestD = 0
difference = 0
month_count = len(dates)

#loop through the created array of profits/losses
for num in range(month_count-1):
    #conditionals to determine whether this row has a higher/lower change
    if (money[count+1]-money[num]) > greatestI:
        greatestI = (money[count+1]-money[num])
        increase = dates[count+1]
    if (money[count+1]-money[num]) < greatestD:
        greatestD = (money[count+1]-money[num])
        decrease = dates[count+1]

    #sum up the differences per month for avg difference
    difference = difference + (money[count+1]-money[num])
    count += 1

#calculate average difference. Subtract 1 from month count since one month will not have a difference
avg_change = difference/(month_count-1)

#format average change to dollars
avg_change = "${:,.2f}".format(avg_change)

#Formatted Outputs
print("\nFinancial Analysis \n ----------------------------")
print(f' Total Months: {month_count}')
print(f' Total: ${profit}')
print(f' Average Change: {avg_change}')
print(f' Greatest Increase in Profits: {increase} (${greatestI})')
print(f' Greatest Decrease in Profits: {decrease} (${greatestD})\n')

#Output to Text File in Analysis Folder
txt_file = open("analysis\Result.txt","w")
txt_file.write("Financial Analysis \n ----------------------------\n")
txt_file.write(f' Total Months: {month_count}\n')
txt_file.write(f' Average Change: {avg_change}\n')
txt_file.write(f' Greatest Increase in Profits: {increase} (${greatestI})\n')
txt_file.write(f' Greatest Decrease in Profits: {decrease} (${greatestD})\n')
txt_file.close()