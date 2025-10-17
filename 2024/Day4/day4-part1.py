with open('inputtest.txt', 'r') as inputfile:
    file = inputfile.read().replace('\n', '')

map = {}

for i, char in enumerate(file):
    print(i, char)
    map[i] = char
print(map)
