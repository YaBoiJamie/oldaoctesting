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
        if input_chars[j] == '0' or input_chars[j] == '1' or input_chars[j] == '2' or input_chars[j] == '3' or input_chars[j] == '4' or input_chars[j] == '5' or input_chars[j] == '6' or input_chars[j] == '7' or input_chars[j] == '8' or input_chars[j] == '9':
            first_digit = input_chars[j]
            # print(f'first digit = {first_digit}')
            break
    for k in range(1,len(input_chars)+1):
        if input_chars[-k] == '0' or input_chars[-k] == '1' or input_chars[-k] == '2' or input_chars[-k] == '3' or input_chars[-k] == '4' or input_chars[-k] == '5' or input_chars[-k] == '6' or input_chars[-k] == '7' or input_chars[-k] == '8' or input_chars[-k] == '9':
            last_digit = input_chars[-k]
            # print(f'last digit = {last_digit}')
            break
    number = (str(first_digit) + str(last_digit))
    numbers += int(number)
    
print(numbers)
