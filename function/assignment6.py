#group7.py
def mr_thomas_account_balance():
    properties_value = 100000 * 4
    father_gift = 50000
    mum_gift = 150000
    car_cost = 200000
    wife_gift = 30000
    initial_balance = 300000
    final_balance = initial_balance + properties_value + father_gift + mum_gift - (car_cost + wife_gift)
    print("Mr. Thomas's account balance is:", final_balance)

mr_thomas_account_balance()