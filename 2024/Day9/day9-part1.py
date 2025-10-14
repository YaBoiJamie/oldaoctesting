file = []
with open('inputtest.txt') as inputfile:
    for line in inputfile:
        for char in line:
            file.append(char)
# print(file)
id = -1
antwoord = []
str1 = '.'


# for i in range(0, len(file), 2):
#     id += 1
#     # print(file[i], i, id)
#     for j in range(int(file[i])):
#         antwoord.append(id)

# for i in range(1, len(file), 2):
#     # print(file[i])
#     for j in range(int(file[i])):
#         antwoord.append(str1)
#     antwoord.append('-')


for i in range(0, len(file), 1):
    if i % 2 or i == 0:
        id += 1
        # print(file[i], i, id)
        for j in range(int(file[i])):
            antwoord.append(id)
    else:
        # print(file[i])
        for j in range(int(file[i])):
            antwoord.append(str1)

print(antwoord)
