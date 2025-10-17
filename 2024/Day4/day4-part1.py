with open('inputtest.txt', 'r') as inputfile:
    file = inputfile.read().splitlines()


map = {}

for y,line in enumerate(file):
    print('regel', y, line)
    for x,char in enumerate(line):
        if x not in map:
            map[x] = {}
        map[x][y] = char
        print('map nu', map)

def getPos(x,y,map):
    """Geef waarde op positie x,y

    Args:
        x (int): Xpos (character)
        y (int): Ypos (regel)
        map (dict): de x/y map

    Returns:
        str: Waarde op x,y
    """
    if x not in map:
        return False
    if y not in map[x]:
        return False
    r = map[x][y]
    return r





print(getPos(4,0,map))

