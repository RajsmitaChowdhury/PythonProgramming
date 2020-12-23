#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
letter = ''
number = ''
symbol = ''
total = nr_letters + nr_symbols
+ nr_numbers
for i in range(nr_letters):
  letter = letter + random.choice(letters)
for i in range(nr_symbols):
  symbol = symbol + random.choice(symbols)
for i in range(nr_numbers):
  number = number + str(random.choice(numbers))
print("Your easy random password is: " + letter + symbol + number)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
temp_list = list(letter + symbol + number)
random.shuffle(temp_list)
hard_pswd = ''.join(temp_list)
print(f"Your complex random password is: {hard_pswd}")
