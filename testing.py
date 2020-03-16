from tkinter import *
import time
import rubiks_cube_3d as cube_3d


    

def main():
    cube=[['blue','blue','orange','yellow','blue','blue','white','orange','white'], ['orange','green','orange','white','white','white','red','yellow','red'], ['green','white','blue','green','red','white','blue','red','orange'], ['yellow','red','white','red','yellow','yellow','green','blue','red'], ['red','red','blue','blue','orange','orange','yellow','yellow','white'], ['green','orange','yellow','green','green','green','green','orange','yellow'],1]
    #input_cube =  [['r', 'b', 'o', 'y', 'b', 'b', 'w', 'o', 'b'], ['b', 'w', 'o', 'y', 'w', 'g', 'w', 'w', 'o'], ['w', 'w', 'b', 'o', 'r', 'w', 'w', 'r', 'o'], ['y', 'r','g', 'r', 'y', 'g', 'g', 'b', 'b'], ['y', 'b', 'r', 'y', 'o', 'r', 'y', 'o', 'g'], ['r', 'g', 'g', 'y', 'g', 'g', 'r', 'o', 'y']], ['l', 'u', 'b', 'b', 'd, 'g'], ['r', 'g', 'g', 'y', 'g', 'g', 'r', 'o', 'y']], ['l', 'u', 'b', 'b'u', 'l', 'u', "l'", 'u', "l'", "u'", 'l', 'u', 'r', "u'", "r'", "u'", "f'", 'u', 'd', 'd', 'r', 'd', 'd', 'u', 'u', 'l', 'l', 'u', 'u', 'r', 'u', "r'", 'u', 'f', "u'", "f'", 'b', "u'", "b'", "u'", "r'", 'u', 'r', "u'", "u'", "b'", 'u', 'u', 'l', 'u', "l'", 'u', "l'", "u'", 'l', 'u', 'r', "u'", "r'", "u'", "', 'u', 'r', "d'", "r'", 'u', 'u', "r'", 'u', 'u', 'f', 'f', 'u', 'l', "r'", 'ff'", 'u', 'f', 'u', 'l', "u'", "l'", "u'", "b'", 'u', 'b', "u'", "l'", 'u', 'l', 'u', 'f', "u'", "f'", 'b', "u'", "b'", "u'", "r'", 'u', 'r', "u'", "u'", "b'", 'u', 'b', 'u', 'l', "u'", "l'", 'r', 'b', 'u', "b'", "u'", 'r', 'd', "r'", 'u', 'u', 'r', "d'", "r'", 'u', 'u', "r'", 'u', 'u', 'f', 'f', 'l', "r'", 'f', 'f', "l'", 'r', 'u', 'f', 'f']]
    
    curr_cubee = [['r', 'b', 'o', 'y', 'b', 'b', 'w', 'o', 'b'], ['b', 'w', 'o', 'y', 'w', 'g', 'w', 'w', 'o'], ['w', 'w', 'b', 'o', 'r', 'w', 'w', 'r', 'o'], ['y', 'r','g', 'r', 'y', 'g', 'g', 'b', 'b'], ['y', 'b', 'r', 'y', 'o', 'r', 'y', 'o', 'g'], ['r', 'g', 'g', 'y', 'g', 'g', 'r', 'o', 'y']]
    
    sol = Tk()
    c = Canvas(sol, width = 400, height = 400)
    c.grid(row = 0, column = 2)

    rubiks_cube = cube_3d.rubiks_cube
    cube_3d.colourCube(rubiks_cube,curr_cubee)
   
    cube2d = cube_3d.convert(rubiks_cube)
    cube_loc = cube_3d.draw_part_of_cube(cube2d[:3],c)
    sol.mainloop()

if __name__ =='__main__':
    main()
