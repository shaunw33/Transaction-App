import csv
from os import path
def log_transactions(logger):
    if not path.isfile('transactions.csv'):
        with open('transactions.csv','w') as fp:
            data = csv.writer(fp)
            data.writerow(['Name','Price','Time','Quantity'])

    with open('transactions.csv', 'a') as fp:
        data = csv.writer(fp)
        for i in range(len(logger)):
            data.writerow(logger[i])
            i + 1