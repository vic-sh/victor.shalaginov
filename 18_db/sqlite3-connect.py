import sqlite3

connection = sqlite3.connect('sw_inventory.db')

cursor = connection.cursor()

cursor.execute("create table switch (mac text not NULL primary key, hostname text, model text, location text)")

data = [('0030.A3AA.C1CC', 'sw3', 'Cisco 3750', 'London, Green Str'),
        ('0040.A4AA.C2CC', 'sw4', 'Cisco 3850', 'London, Green Str'),
        ('0050.A5AA.C3CC', 'sw5', 'Cisco 3850', 'London, Green Str'),
        ('0060.A6AA.C4CC', 'sw6', 'C3750', 'London, Green Str')]

query = "INSERT into switch values (?, ?, ?, ?)"


for row in data:
    cursor.execute(query, row)

connection.commit()