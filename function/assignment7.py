# group8.py
def mrs_bridget_remaining_budget():
    budget = 30000 * 0.85
    pawpaw_cost = 300 * 50
    ginger_cost = 600 * 5
    groundnut_cost = 50 * 10
    stationery_cost = 550 * 10
    bread_cost = 10 * 50
    total_cost = pawpaw_cost + ginger_cost + groundnut_cost + stationery_cost + bread_cost
    remaining_money = budget - total_cost
    print("Mrs. Bridget's remaining budget is:", remaining_money)

mrs_bridget_remaining_budget()