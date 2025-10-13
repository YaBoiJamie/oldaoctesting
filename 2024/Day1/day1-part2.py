import os

# Get the folder where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Build the full path to input.txt
file_path = os.path.join(script_dir, 'input.txt')

# Open and read the file
with open(file_path, 'r') as file:
    content = file.read()
left_list = []
right_list = []
for line in content.strip().split('\n'):
    left, right = line.split()
    left_list.append(int(left))
    right_list.append(int(right))

similarity_score = 0
for number in left_list:
    for number2 in right_list:
        if number == number2:
            similarity_score += number
print(similarity_score)