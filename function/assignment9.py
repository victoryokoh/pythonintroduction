# group11.py
def mrs_banjo_transactions():
    balance = 100000
    transactions = []
    while balance > 5000:
        transactions.append(balance)
        balance -= 2000
    print("Transaction details for Mrs. Banjo:", transactions)

mrs_banjo_transactions()