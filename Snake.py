from Fila.Fila import Fila
from Fila.Puntos import Puntos
from ListaCircularDoble.LiscaCircular import ListaCircular
from ListaCircularDoble.Usuarios import Usuario

import curses #import the curses library
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN, KEY_ENTER #import special KEYS from the curses library
import csv

height = 30
width = 100
usuarios = ListaCircular()
usuario = None

def juego(win):
    window = win

    punteo = 0
    nivel = 1
    pausa = 100
    key = KEY_RIGHT         #key defaulted to KEY_RIGHT
    pos_x = 1               #initial x position
    pos_y = 1               #initial y position
    window.addch(pos_y,pos_x,'*')   #print initial dot

    while key != 27:                #run program while [ESC] key is not pressed
        if punteo > 14:
            punteo = 0
            nivel += 1
            pausa -= 5
        window.border(0)
        window.addstr(0, 47, ' SNAKE ')
        window.timeout(pausa)               #delay of 100 milliseconds
        window.addstr(0, 1, ' Puntos: ' + str(punteo) + ' ')                # Printing 'Score' and
        window.addstr(0, 89, ' Nivel: ' + str(nivel) + ' ') 
        keystroke = window.getch()          #get current key being pressed
        if keystroke is not  -1:            #key is pressed
            key = keystroke                 #key direction changes
        
        window.addch(pos_y, pos_x, ' ')       #erase last dot
        if key == KEY_RIGHT:                #right direction
            pos_x = pos_x + 1               #pos_x increase
            if   pos_x > width-2:
                pos_x = 1
        elif key == KEY_LEFT:               #left direction
            pos_x = pos_x - 1               #pos_x decrease
            if   pos_x < 1:
                pos_x = width-2
        elif key == KEY_UP:                 #up direction
            pos_y = pos_y - 1               #pos_y decrease
            if   pos_y < 1:
                pos_y = height-2
        elif key == KEY_DOWN:               #down direction
            pos_y = pos_y + 1               #pos_y increase
            if   pos_y > height-2:
                pos_y = 1
        window.addch(pos_y,pos_x,'#')       #draw new dot
    
    window.addch(pos_y, pos_x, ' ')
    curses.endwin() #return terminal to previous state


def menu():
    stdscr = curses.initscr() #initialize console
    pos_y = 0
    pos_x = 0
    window = curses.newwin(height,width,pos_y,pos_x) #create a new curses window
    window.keypad(True)     #enable Keypad mode
    curses.noecho()         #prevent input from displaying in the screen
    curses.curs_set(0)      #cursor invisible (0)
            #default border for our window
    window.nodelay(True)    #return -1 when no key is pressed

    key = -1         #key defaulted to KEY_RIGHT

    while key != 27:                #run program while [ESC] key is not pressed
        window.border(0)
        stdscr.clear()
        key = -1
        window.addstr(0, 47, ' SNAKE ')
        window.addstr(10, 41, ' 1.Jugar ')
        window.addstr(11, 41, ' 2.Puntajes ') 
        window.addstr(12, 41, ' 3.Usuarios ') 
        window.addstr(13, 41, ' 4.Reportes ') 
        window.addstr(14, 41, ' 5.Carga(usuario.CSV) ') 
        keystroke = window.getch()          #get current key being pressed
        if keystroke is not  -1:            #key is pressed
            key = keystroke                 #key direction changes
        
        window.addch(pos_y, pos_x, ' ')       #erase last dot
        if key == 49 or key == 50 or key == 51 or key == 52 or key == 53:                #right direction
            fila = 10
            for i in range(5):
                window.addstr(fila, 41, '                      ')
                fila += 1
            if   key == 49:
                juego(window)
            elif key == 50:               #left direction
                print("2")
            elif key == 51:                 #up direction
                print("3")
            elif key == 52:               #down direction
                print("4")
            elif key == 53:               #down direction
                carga()

    curses.endwin() #return terminal to previous state    

def carga():
    try:
        with open("usuarios.CSV", newline='') as File:  
            reader = csv.reader(File)
            for line in reader:
                if line != "Usuario":
                    us = Usuario(line)
                    usuarios.agregar(us)
        
    except FileNotFoundError:
        print("")
            
menu()