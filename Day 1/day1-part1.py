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


left_sorted = sorted(left_list)
right_sorted = sorted(right_list)


total_distance = 0
for i in range(len(left_sorted)):
    if right_sorted[i] > left_sorted[i]:
        distance = right_sorted[i] - left_sorted[i]
        total_distance += distance
    elif left_sorted[i] > right_sorted[i]:
        distance = left_sorted[i] - right_sorted[i]
        total_distance += distance
   

print(total_distance)
