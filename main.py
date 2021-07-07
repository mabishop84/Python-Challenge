import csv
import os
#from csv import DictReader
#from typing import List, Dict

csv_path = os.path.join('budget_data.csv')



with open(csv_path, 'r') as csv_file:

    # Split the data on commas
    csv_reader = csv.reader(csv_file, delimiter=',')

    header = next(csv_reader)
    profit_loss_sum = 0
    date_count = 0
    delta_profit_counter = 0
    delta_profit = 0
    previous_profit_loss = 0
    avg_profit = 0
    delta_profit_sum =0
    greatest_inc = 0
    greatest_dec = 0
    
   # profit_index = None
    #table: List[Dict[str,float]]=[]
    for row in csv_reader:
        date=row[0]
        profit_loss=int(row[1])
        date_count +=1
        profit_loss_sum += profit_loss
        if date_count > 1:
            delta_profit_counter =  profit_loss - previous_profit_loss
        delta_profit_sum=delta_profit_sum+delta_profit_counter
        previous_profit_loss = int(row[1])
        if delta_profit_counter > greatest_inc:
            greatest_inc = delta_profit_counter
        if delta_profit_counter < greatest_dec:
            greatest_dec = delta_profit_counter

        #print(delta_profit_counter)
        #print(profit_loss_sum)
        #print(total_delta_profit)       

total_delta_profit = delta_profit_sum/(date_count-1)
#avg_profit = sum(delta_profit_counter)/(date_count-1)
#print(profit_loss_sum)

print(f"Financial Analysis")
print(f"-------------------------------")
print(f"Total Months: {str(date_count)}")
print(f"Total: {str(profit_loss_sum)}")
print(f"Average Change: {str(total_delta_profit)}")
print(f"Greatest Increase in Profits:  {str(greatest_inc)}")
print(f"Greatest Decrease in Profits:  {str(greatest_dec)}")


output= os.path.join('Analysis.txt')
with open(output, 'w') as text:
    text.write(f"Financial Analysis" + '\n')
    text.write(f"-------------------------------"  + '\n')
    text.write(f"Total Months: {str(date_count)}"  + '\n')
    text.write(f"Total: {str(profit_loss_sum)}"  + '\n')
    text.write(f"Average Change: {str(total_delta_profit)}"  + '\n')
    text.write(f"Greatest Increase in Profits:  {str(greatest_inc)}"  + '\n')
    text.write(f"Greatest Decrease in Profits:  {str(greatest_dec)}"  + '\n')
#data = [row for row in csv_reader]
#date = datetime=strptime(row[0],'%m/%d')
#profit_loss=integer(row[1])
#print(f'{budget_data}')


#def print_financial_analysis(budget_csv):
 #   date = str(budget_csv[0])
  #  profit_loss = int(budget_csv[1])