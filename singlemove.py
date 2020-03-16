def single_move(cube,move):
    #if move == "f":
    #    cube[1][6], cube[1][7], cube[1][8], cube[0][0], cube[0][3], cube[0][6], cube[5][0], cube[5][1], cube[5][2], cube[4][2], cube[4][5], cube[4][8] = cube[4][8], cube[4][5], cube[4][2], cube[1][6], cube[1][7], cube[1][8], cube[0][6], cube[0][3], cube[0][0], cube[5][0], cube[5][1], cube[5][2]
    #    cube[2][0], cube[2][1], cube[2][2], cube[2][3], cube[2][5], cube[2][6], cube[2][7], cube[2][8] = cube[2][6], cube[2][3], cube[2][0], cube[2][7], cube[2][1], cube[2][8], cube[2][5], cube[2][2]  
    if move == "f":
        cube[1][0], cube[1][3], cube[1][6],  cube[5][2], cube[5][1], cube[5][0],cube[4][8], cube[4][5], cube[4][2],cube[2][6], cube[2][7], cube[2][8] = cube[2][6], cube[2][7], cube[2][8],cube[1][0], cube[1][3], cube[1][6],  cube[5][2], cube[5][1], cube[5][0],cube[4][8], cube[4][5], cube[4][2] 
        cube[0][0], cube[0][1], cube[0][2], cube[0][3], cube[0][5], cube[0][6], cube[0][7], cube[0][8] = cube[0][6], cube[0][3], cube[0][0], cube[0][7], cube[0][1], cube[0][8], cube[0][5], cube[0][2]      
    elif move == "f'":
        cube[1][6], cube[1][7], cube[1][8], cube[0][0], cube[0][3], cube[0][6], cube[5][0], cube[5][1], cube[5][2], cube[4][2], cube[4][5], cube[4][8] = cube[0][0], cube[0][3], cube[0][6], cube[5][2], cube[5][1], cube[5][0], cube[4][2], cube[4][5], cube[4][8], cube[1][8], cube[1][7], cube[1][6]
        cube[2][0], cube[2][1], cube[2][2], cube[2][3], cube[2][5], cube[2][6], cube[2][7], cube[2][8] = cube[2][2], cube[2][5], cube[2][8], cube[2][1], cube[2][7], cube[2][0], cube[2][3], cube[2][6]  
    elif move == "r":
        cube[1][2], cube[1][5], cube[1][8], cube[3][0], cube[3][3], cube[3][6], cube[5][2], cube[5][5], cube[5][8], cube[2][2], cube[2][5], cube[2][8] = cube[2][2], cube[2][5], cube[2][8], cube[1][8], cube[1][5], cube[1][2], cube[3][6], cube[3][3], cube[3][0], cube[5][2], cube[5][5], cube[5][8]
        cube[0][0], cube[0][1], cube[0][2], cube[0][3], cube[0][5], cube[0][6], cube[0][7], cube[0][8] = cube[0][6], cube[0][3], cube[0][0], cube[0][7], cube[0][1], cube[0][8], cube[0][5], cube[0][2]  
    elif move == "r'":
        cube[1][2], cube[1][5], cube[1][8], cube[3][0], cube[3][3], cube[3][6], cube[5][2], cube[5][5], cube[5][8], cube[2][2], cube[2][5], cube[2][8] = cube[3][6], cube[3][3], cube[3][0], cube[5][8], cube[5][5], cube[5][2], cube[2][2], cube[2][5], cube[2][8], cube[1][2], cube[1][5], cube[1][8]
        cube[0][0], cube[0][1], cube[0][2], cube[0][3], cube[0][5], cube[0][6], cube[0][7], cube[0][8] = cube[0][2], cube[0][5], cube[0][8], cube[0][1], cube[0][7], cube[0][0], cube[0][3], cube[0][6]  
    elif move == "u":
        cube[2][0], cube[2][1], cube[2][2], cube[0][0], cube[0][1], cube[0][2], cube[3][0], cube[3][1], cube[3][2], cube[4][0], cube[4][1], cube[4][2] = cube[0][0], cube[0][1], cube[0][2], cube[3][0], cube[3][1], cube[3][2], cube[4][0], cube[4][1], cube[4][2], cube[2][0], cube[2][1], cube[2][2]
        cube[1][0], cube[1][1], cube[1][2], cube[1][3], cube[1][5], cube[1][6], cube[1][7], cube[1][8] = cube[1][6], cube[1][3], cube[1][0], cube[1][7], cube[1][1], cube[1][8], cube[1][5], cube[1][2]  
    elif move == "u'":
        cube[2][0], cube[2][1], cube[2][2], cube[0][0], cube[0][1], cube[0][2], cube[3][0], cube[3][1], cube[3][2], cube[4][0], cube[4][1], cube[4][2] = cube[4][0], cube[4][1], cube[4][2], cube[2][0], cube[2][1], cube[2][2], cube[0][0], cube[0][1], cube[0][2], cube[3][0], cube[3][1], cube[3][2]
        cube[1][0], cube[1][1], cube[1][2], cube[1][3], cube[1][5], cube[1][6], cube[1][7], cube[1][8] = cube[1][2], cube[1][5], cube[1][8], cube[1][1], cube[1][7], cube[1][0], cube[1][3], cube[1][6]  
    elif move == "b":
        cube[1][0], cube[1][1], cube[1][2], cube[0][2], cube[0][5], cube[0][8], cube[5][6], cube[5][7], cube[5][8], cube[4][0], cube[4][3], cube[4][6] = cube[0][2], cube[0][5], cube[0][8], cube[5][8], cube[5][7], cube[5][6], cube[4][0], cube[4][3], cube[4][6], cube[1][2], cube[1][1], cube[1][0]
        cube[3][0], cube[3][1], cube[3][2], cube[3][3], cube[3][5], cube[3][6], cube[3][7], cube[3][8] = cube[3][6], cube[3][3], cube[3][0], cube[3][7], cube[3][1], cube[3][8], cube[3][5], cube[3][2]  
    elif move == "b'":
        cube[1][0], cube[1][1], cube[1][2], cube[0][2], cube[0][5], cube[0][8], cube[5][6], cube[5][7], cube[5][8], cube[4][0], cube[4][3], cube[4][6] = cube[4][0], cube[4][3], cube[4][6], cube[1][0], cube[1][1], cube[1][2], cube[0][8], cube[0][5], cube[0][2], cube[5][6], cube[5][7], cube[5][8]
        cube[3][0], cube[3][1], cube[3][2], cube[3][3], cube[3][5], cube[3][6], cube[3][7], cube[3][8] = cube[3][2], cube[3][5], cube[3][8], cube[3][1], cube[3][7], cube[3][0], cube[3][3], cube[3][6]  
    elif move == "l":
        cube[1][0], cube[1][3], cube[1][6], cube[3][2], cube[3][5], cube[3][8], cube[5][0], cube[5][3], cube[5][6], cube[2][0], cube[2][3], cube[2][6] = cube[3][8], cube[3][5], cube[3][2], cube[5][6], cube[5][3], cube[5][0], cube[2][0], cube[2][3], cube[2][6], cube[1][0], cube[1][3], cube[1][6]
        cube[4][0], cube[4][1], cube[4][2], cube[4][3], cube[4][5], cube[4][6], cube[4][7], cube[4][8] = cube[4][6], cube[4][3], cube[4][0], cube[4][7], cube[4][1], cube[4][8], cube[4][5], cube[4][2]  
    elif move == "l'":
        cube[1][0], cube[1][3], cube[1][6], cube[3][2], cube[3][5], cube[3][8], cube[5][0], cube[5][3], cube[5][6], cube[2][0], cube[2][3], cube[2][6] = cube[2][0], cube[2][3], cube[2][6], cube[1][6], cube[1][3], cube[1][0], cube[3][8], cube[3][5], cube[3][2], cube[5][0], cube[5][3], cube[5][6]
        cube[4][0], cube[4][1], cube[4][2], cube[4][3], cube[4][5], cube[4][6], cube[4][7], cube[4][8] = cube[4][2], cube[4][5], cube[4][8], cube[4][1], cube[4][7], cube[4][0], cube[4][3], cube[4][6]  
    elif move == "d":
        cube[2][6], cube[2][7], cube[2][8], cube[0][6], cube[0][7], cube[0][8], cube[3][6], cube[3][7], cube[3][8], cube[4][6], cube[4][7], cube[4][8] = cube[4][6], cube[4][7], cube[4][8], cube[2][6], cube[2][7], cube[2][8], cube[0][6], cube[0][7], cube[0][8], cube[3][6], cube[3][7], cube[3][8]
        cube[5][0], cube[5][1], cube[5][2], cube[5][3], cube[5][5], cube[5][6], cube[5][7], cube[5][8] = cube[5][6], cube[5][3], cube[5][0], cube[5][7], cube[5][1], cube[5][8], cube[5][5], cube[5][2]  
    #elif move == "d'":
    #    cube[2][6], cube[2][7], cube[2][8], cube[0][6], cube[0][7], cube[0][8], cube[3][6], cube[3][7], cube[3][8], cube[4][6], cube[4][7], cube[4][8] = cube[0][6], cube[0][7], cube[0][8], cube[3][6], cube[3][7], cube[3][8], cube[4][6], cube[4][7], cube[4][8], cube[2][6], cube[2][7], cube[2][8]
    #    cube[5][0], cube[5][1], cube[5][2], cube[5][3], cube[5][5], cube[5][6], cube[5][7], cube[5][8] = cube[5][2], cube[5][5], cube[5][8], cube[5][1], cube[5][7], cube[5][0], cube[5][3], cube[5][6]  
    #    print(cube)
    elif move == "d'":
        cube[0][6], cube[0][7], cube[0][8], cube[1][6], cube[1][7], cube[1][8], cube[3][6], cube[3][7], cube[3][8], cube[4][6], cube[4][7], cube[4][8] = cube[1][6], cube[1][7], cube[1][8], cube[3][6], cube[3][7], cube[3][8],cube[4][6], cube[4][7], cube[4][8],            cube[0][6], cube[0][7], cube[0][8]
        cube[5][0], cube[5][1], cube[5][2], cube[5][3], cube[5][5], cube[5][6], cube[5][7], cube[5][8] = cube[5][2], cube[5][5], cube[5][8], cube[5][1], cube[5][7], cube[5][0], cube[5][3], cube[5][6]  
        print(cube)

def moves(cube,moves):
    for move in moves:
        single_move(cube,move)





#if move == "f":
#        cube[1][0], cube[1][3], cube[1][6],  cube[5][2], cube[5][1], cube[5][0],cube[4][8], cube[4][5], cube[4][2],cube[2][6], cube[2][7], cube[2][8] = cube[2][6], cube[2][7], cube[2][8],cube[1][0], cube[1][3], cube[1][6],  cube[5][2], cube[5][1], cube[5][0],cube[4][8], cube[4][5], cube[4][2] 
#        cube[0][0], cube[0][1], cube[0][2], cube[0][3], cube[0][5], cube[0][6], cube[0][7], cube[0][8] = cube[0][6], cube[0][3], cube[0][0], cube[0][7], cube[0][1], cube[0][8], cube[0][5], cube[0][2]   
#    elif move == "f'":
#        cube[2][6], cube[2][7], cube[2][8], cube[4][8], cube[4][5], cube[4][2], cube[5][2], cube[5][1], cube[5][0], cube[1][0], cube[1][3], cube[1][6] = cube[1][0], cube[1][3], cube[1][6], cube[2][6], cube[2][7], cube[2][8], cube[4][8], cube[4][5], cube[4][2], cube[5][2], cube[5][1], cube[5][0]
#        cube[0][0], cube[0][1], cube[0][2], cube[0][3], cube[0][5], cube[0][6], cube[0][7], cube[0][8] = cube[0][2], cube[0][5], cube[0][8], cube[0][1], cube[0][7], cube[0][0], cube[0][3], cube[0][6]   
