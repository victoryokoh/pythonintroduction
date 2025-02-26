#Mrs Philip account balance in GTB is 200000, the bank decided to be removing 4000
# from her account every day this action should continue while her balance is > 6000.
#Write a python function code that will show the transaction details in
balance = 200000
while balance >6000:
    balance=balance-4000
    print(balance)
    
    