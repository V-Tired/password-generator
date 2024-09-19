import random

input_letters = input("How many letters would you like in your password?\n")
input_numbers = input("How many numbers?\n")
input_symbols = input("How many symbols?\n")

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
           "w", "x", "y", "z"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

let = 0
num = 0
sym = 0
password = ""

while let != int(input_letters) or num != int(input_numbers) or sym != int(input_symbols):

    if let != int(input_letters):
        random.choice(letters)
        password += random.choice(letters)
        let += 1
    if num != int(input_numbers):
        random.choice(numbers)
        password += random.choice(numbers)
        num += 1
    if sym != int(input_symbols):
        random.choice(symbols)
        sym += 1
        password += random.choice(symbols)

print(f"The password is {password}.")
