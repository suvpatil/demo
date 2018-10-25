import sqlite3
import csv

conn = sqlite3.connect('app.db')
cursor = conn.cursor()


def db_to_csv(table, filename, columns):
    data = cursor.execute('SELECT * FROM "%s"' % table)
    with open('db/%s.csv' % filename, 'w+') as f:
        print("\n%s:" % filename)
        csv_file = csv.writer(f)
        csv_file.writerow(columns)
        for row in data:
            print(row)
            csv_file.writerow(row)


tables = ['User', 'Balance', 'Trade', 'Transfer']
filenames = ['users', 'balances', 'trades', 'transfers']
columns = [['id', 'first_name', 'last_name', 'username', 'password_hash', 
            'balances', 'trades', 'transfers'],
           ['id', 'balance_btc', 'balance_usd', 'user_id'],
           ['id', 'timestamp', 'tx_type', 'amount', 'price', 'total',
            'user_id'],
           ['id', 'timestamp', 'tx_type', 'amount', 'currency', 'tx_id', 
            'user_id']]

for table, filename, column in zip(tables, filenames, columns):
    db_to_csv(table, filename, column)
