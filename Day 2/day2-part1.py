import os

# Get the folder where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Build the full path to input.txt
file_path = os.path.join(script_dir, 'inputtest.txt')

list = []

# Open and read the file
with open(file_path, 'r') as file:
    for line in file:
        numbers = line.strip().split()
        list.append(numbers)

safe_reports = 0
for i in range(len(list)):
    puzzlelist = list[i]
    if (int(puzzlelist[0]) - int(puzzlelist[1])) <= 3 and (int(puzzlelist[0]) - int(puzzlelist[1])) >= -3 and (int(puzzlelist[0]) - int(puzzlelist[1])) != 0:
        if (int(puzzlelist[1]) - int(puzzlelist[2])) <= 3 and (int(puzzlelist[1]) - int(puzzlelist[2])) >= -3 and (int(puzzlelist[1]) - int(puzzlelist[2])) != 0:
            if (int(puzzlelist[2]) - int(puzzlelist[3])) <= 3 and (int(puzzlelist[2]) - int(puzzlelist[3])) >= -3 and (int(puzzlelist[2]) - int(puzzlelist[3])) != 0:
                if (int(puzzlelist[3]) - int(puzzlelist[4])) <= 3 and (int(puzzlelist[3]) - int(puzzlelist[4])) >= -3 and (int(puzzlelist[3]) - int(puzzlelist[4])) != 0:
                    if puzzlelist[0] > puzzlelist[1] > puzzlelist[2] > puzzlelist[3] > puzzlelist[4] or puzzlelist[0] < puzzlelist[1] < puzzlelist[2] < puzzlelist[3] < puzzlelist[4]:
                        safe_reports += 1

# heb geen flauw idee hoe ik dit nu niet 'hardcoded' moet doen zodat het werkt op de puzzel input                   


print(safe_reports)



    
                    
                        
        
                    


