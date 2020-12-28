import sqlite3

conn = sqlite3.connect('new_db.db')

cursor = conn.cursor()

cursor.executescript('''
    create table switches (
        hostname message_text not null primary key,
        location text
    );
    
    create table dhcp (
        mac message_text not null primary key,
        datetime_interval_precision message_text,
        vlan text
    );
''')