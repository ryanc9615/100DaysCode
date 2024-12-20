import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to password generator!")

num_letters = int(input("How many letters would you like?"))
num_numbers = int(input("How many numbers?"))
num_symbols = int(input("How many symbols?"))

password_list = []

for char in range(0,num_letters):
    password_list += random.choice(letters)
for char in range(0,num_numbers):
    password_list += random.choice(letters)
for char in range(0,num_symbols):
    password_list += random.choice(letters)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""

for char in password_list:
    password += char

print(f"Your password is: {password}")

