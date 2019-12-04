import sqlite3

connection = sqlite3.connect('sw_inventory.db')

print(type(connection))
print(connection.in_transaction)

cursor = connection.cursor()

cursor.execute("create table IF NOT EXISTS switch (mac text not NULL primary key, hostname text, model text, location text)")

data = [('0030.A3AA.C1CC', 'sw3', 'Cisco 3750', 'London, Green Str'),
        ('0040.A4AA.C2CC', 'sw4', 'Cisco 3850', 'London, Green Str'),
        ('0050.A5AA.C3CC', 'sw5', 'Cisco 3850', 'London, Green Str'),
        ('0060.A6AA.C4CC', 'sw6', 'C3750', 'London, Green Str')]

data2 = [('0070.A7AA.C5CC', 'sw7', 'Cisco 3650', 'London, Green Str'),
         ('0080.A8AA.C6CC', 'sw8', 'Cisco 3650', 'London, Green Str')]

query = "INSERT into switch values (?, ?, ?, ?)"

for row in data:
    cursor.execute(query, row)

cursor.executemany(query, data2)

connection.commit()

print(connection.in_transaction)

cursor.execute('select * from switch')

print(connection.in_transaction)

print('fetchone')
print(cursor.fetchone())
print('fetchmany')
'''
while True:
    next_row = cursor.fetchone()
    if next_row:
        print(next_row)
    else:
        break
'''

#print(cursor.arraysize)
print(cursor.fetchmany(size=2))
print('fetchall')
print(cursor.fetchall())

print('cursor as iterator')
result = cursor.execute('select * from switch')

for row in result:
    print(row)


print(connection.in_transaction)


