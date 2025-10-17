file = []
with open('input.txt') as inputfile:
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
#         antwoord.append(str(id))

# for i in range(1, len(file), 2):
#     # print(file[i])
#     for j in range(int(file[i])):
#         antwoord.append(str1)



for i in range(0, len(file), 1):
    if i % 2 == 0:
        id += 1
        # print(file[i], i, id)
        for j in range(int(file[i])):
            antwoord.append(id)
    else:
        # print(file[i])
        for k in range(int(file[i])):
            antwoord.append(str1)
print(antwoord)


def eersteVrije(lst):
    for f,v in enumerate(lst):
        if v == '.':
            break 
    if f == len(lst)-1:
        return -1 # er is geen vrije plek
    return f

def checksum(lst):
    c = 0
    for k,v in enumerate(lst):
        if v != '.':
            c += (k*v)
    return c 
eerste = eersteVrije(antwoord)

for p in range(len(antwoord)):
    checkpos = len(antwoord) - p -1
    checkval = antwoord[checkpos]
    if checkval != '.':
        antwoord[eerste] = checkval
        antwoord[checkpos] = '.'
        eerste = eersteVrije(antwoord)
    if eerste == checkpos:
        break

print(antwoord)
print(checksum(antwoord))
