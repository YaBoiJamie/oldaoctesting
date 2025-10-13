import re

with open('input.txt', 'r') as file:
    inputfile = file.read()

def mul(x,y):
    return x * y
check = re.compile(r'mul\([0-9]{1,3},[0-9]{1,3}\)')

matches = check.findall(inputfile)
# print(matches)
totaal = 0
for match in matches:
    #print(match)
    muller = match.strip('mul()')
    # print(muller)
    yes = muller.split(',')
    # print(yes)
    antwoord = mul(int(yes[0]),int(yes[1]))
    totaal += antwoord
print(totaal)

print(inputfile)






    