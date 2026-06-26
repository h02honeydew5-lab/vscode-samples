
#Get details of loan
money_owed =float(input('How much money do you owe?\n')) 
apr = float(input('What is the annual \n'))
payment - float(input('How much will you pay off each month\n'))
months = int(input('How many months\n'))

monthly_rate = apr/100/12
# Calculate interest to pay
interest_paid = money_owned* monthly_rate

money_owed = money_owed + interest_paid

money_owed = money_owed - payment
pring('Paid',payment, 'of which', interest_paid, 'was interst'  )
print('Now I owe', money_owed)