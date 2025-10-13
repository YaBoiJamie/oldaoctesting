import os

# Get the folder where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Build the full path to input.txt
file_path = os.path.join(script_dir, 'input.txt')

list = []

# Open and read the file
with open(file_path, 'r') as file:
    for line in file:
        numbers = line.strip().split()
        list.append(numbers)

# safe_reports = 0
# for i in range(len(list)):
#     puzzlelist = list[i]
#     if (int(puzzlelist[0]) - int(puzzlelist[1])) <= 3 and (int(puzzlelist[0]) - int(puzzlelist[1])) >= -3 and (int(puzzlelist[0]) - int(puzzlelist[1])) != 0:
#         if (int(puzzlelist[1]) - int(puzzlelist[2])) <= 3 and (int(puzzlelist[1]) - int(puzzlelist[2])) >= -3 and (int(puzzlelist[1]) - int(puzzlelist[2])) != 0:
#             if (int(puzzlelist[2]) - int(puzzlelist[3])) <= 3 and (int(puzzlelist[2]) - int(puzzlelist[3])) >= -3 and (int(puzzlelist[2]) - int(puzzlelist[3])) != 0:
#                 if (int(puzzlelist[3]) - int(puzzlelist[4])) <= 3 and (int(puzzlelist[3]) - int(puzzlelist[4])) >= -3 and (int(puzzlelist[3]) - int(puzzlelist[4])) != 0:
#                     if puzzlelist[0] > puzzlelist[1] > puzzlelist[2] > puzzlelist[3] > puzzlelist[4] or puzzlelist[0] < puzzlelist[1] < puzzlelist[2] < puzzlelist[3] < puzzlelist[4]:
#                         safe_reports += 1

# # heb geen flauw idee hoe ik dit nu niet 'hardcoded' moet doen zodat het werkt op de puzzel input
# for i in range(len(list)):
#     puzzellist = list[i]
#     var = 0
#     for number in puzzellist:
#         if (int(puzzlelist[int(number)]) - int(puzzlelist[int(number)+1])) <= 3 and (int(puzzlelist[int(number)]) - int(puzzlelist[int(number)+1])) >= -3 and (int(puzzlelist[int(number)]) - int(puzzlelist[int(number)+1])) != 0:
#             var +=1
#     if var == len(puzzellist):
#         print('yes')
#     else:
#         print('no')

# print(safe_reports)


# zo dan?
safe_reports = 0
for valuelist in list:
    # alle 'regels'
    values = [int(x) for x in valuelist]
    # zijn we oplopend of aflopend?
    if values[1] > values[0]:
        dir = "O"
    elif values[1] < values[0]:
        dir = "A"
    else:
        print('Deze is al niet goed')
    a = values[0]
    hoeveel_moeten_er_goed = len(values) - 1
    goed = 0
    for b in values[1:]:
        # vanaf de tweede   
        print(f"moet {a} en {b} checken")     
        if dir == "O":
            if b - a <= 3 and b - a > 0:
                print('safe')
                goed += 1 
        elif dir == "A":
            if a - b <= 3 and a -b > 0:
                print('safe')
                goed += 1
        a = b # nu de tweede met de derde (volgende loop) 
    if goed == hoeveel_moeten_er_goed:
        safe_reports += 1

print(safe_reports)


    
                    
                        
        
                    


