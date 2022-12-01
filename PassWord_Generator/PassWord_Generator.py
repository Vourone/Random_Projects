import random

print ('Welcome to Your PassWord Generator')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`1234567890-=[]\;',./~!@#$%^&*()_+{}|:"<>?'

number = input('Amount of Password: ')
number = int(number)

length = input('Input Your PassWord Length: ')
length = int(length)

print('\n Here are your password: ')

for pwd in range (number):
	password = ''
	for a in range (length):
		password += random.choice(chars)
	print (passwords)
