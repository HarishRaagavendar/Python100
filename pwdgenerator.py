import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to pwd Generator")
letr=int(input(f"How many letter would you want in password\n"))
sym=int(input(f"How many number of symbols?\n"))
num=int(input(f"How many numbers?\n"))

password = []

for char in range(1, letr + 1):
  password += random.choice(letters)

for char in range(1, sym + 1):
  password += random.choice(symbols)

for char in range(1, num + 1):
  password += random.choice(numbers)
print(password)
random.shuffle(password)
print(password)