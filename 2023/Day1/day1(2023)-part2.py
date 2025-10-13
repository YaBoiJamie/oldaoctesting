import os

# Get the folder where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Build the full path to input.txt
file_path = os.path.join(script_dir, 'input.txt')

# Open and read the file
with open(file_path, 'r') as file:
    content = file.read()

list = []
for line in content.strip().split('\n'):
    list.append(line)

words = {
    'zero' : 0,
    'one' : 1,
    'two' : 2,
    'three' : 3,
    'four' : 4,
    'five' : 5,
    'six' : 6,
    'seven' : 7,
    'eight' : 8,
    'nine' : 9
}

singlechars = []

for line in list:
    charlist = []
    for char in line:
        charlist.append(char)
    singlechars.append(charlist)

numbers = 0

for i in range(len(singlechars)):
    first_digit = 0
    last_digit = 0
    input_chars = singlechars[i]
    for j in range(len(input_chars)):
        if input_chars[j].isdigit(): 
            first_digit = input_chars[j]
            # print(f'first digit = {first_digit}')
            break
    for k in range(1,len(input_chars)+1):
        if input_chars[-k].isdigit():
            last_digit = input_chars[-k]
            # print(f'last digit = {last_digit}')
            break
    number = (str(first_digit) + str(last_digit))
    numbers += int(number)
    
print(numbers)
