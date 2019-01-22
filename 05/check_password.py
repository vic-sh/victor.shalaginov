# -*- coding: utf-8 -*-

username = input('Please enter username: ')
password = input('Please enter password: ')

if len(password) < 8:
 print('Password too short')
elif username in password:
 print('Password consist username')
else:
 print('Password for username {} set'.format(username))

