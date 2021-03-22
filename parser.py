from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing
See the file script for an example of the file format
"""

def parse_file( fname, points, transform, screen, color ):
    f = open(fname, 'r') #open file
    file = f.read().split('\n') #read's file, split things by new line; put that into a list
    f.close()
    i = 0
    while i < len(file):
        if file[i] == "line":
            coor = file[i+1].split(' ') #read next line, split by space; put that into a list
            add_edge(points, int(coor[0]), int(coor[1]), int(coor[2]), int(coor[3]), int(coor[4]), int(coor[5]))
            i += 2
        elif file[i] == "ident":
            ident(transform)
            i += 1
        elif file[i] == "scale":
            coor = file[i+1].split(' ')
            scale = make_scale(int(coor[0]), int(coor[1]), int(coor[2]))
            matrix_mult(scale, transform)
            i += 2
        elif file[i] == "move":
            coor = file[i+1].split(' ')
            translate = make_translate(int(coor[0]), int(coor[1]), int(coor[2]))
            matrix_mult(translate, transform)
            i += 2
        elif file[i] == "rotate": #could do, rotate = None, and then move matrix_mult to after the conditional statements
            coor = file[i+1].split(' ')
            if coor[0] == 'x':
                rotate = make_rotX(float(coor[1]))
                matrix_mult(rotate, transform)
            elif coor[0] == 'y':
                rotate = make_rotY(float(coor[1]))
                matrix_mult(rotate, transform)
            elif coor[0] == 'z':
                rotate = make_rotZ(float(coor[1]))
                matrix_mult(rotate, transform)
            i += 2
        elif file[i] == "apply":
            matrix_mult(transform, points)
            i += 1
        elif file[i] == "display":
            clear_screen(screen)
            draw_lines(points, screen, color)
            display(screen)
            i += 1
        elif file[i] == "save":
            name = file[i+1].split(' ')[0]
            clear_screen(screen)
            draw_lines(points, screen, color)
            save_extension(screen, name)
            save_ppm(screen, name)
            save_ppm_ascii(screen, name)
            i += 1
        elif file[i] == "quit":
            break
        else:
            break