from Fila.Fila import Fila
from Fila.Puntos import Puntos
from ListaCircularDoble.LiscaCircular import ListaCircular
from ListaCircularDoble.Usuarios import Usuario
from ListaDoble.ListaDoble import ListaDoble
from ListaDoble.Cuerpo import Cuerpo

import curses #import the curses library
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN, KEY_ENTER #import special KEYS from the curses library
import csv
from random import randint

height = 30
width = 100
usuarios = ListaCircular()

def juego(win):
    window = win

    punteo = 0
    nivel = 1
    pausa = 150
    key = KEY_RIGHT         #key defaulted to KEY_RIGHT
    pos_x = 1               #initial x position
    pos_y = 1               #initial y position

    snake = ListaDoble()
    snake.insertar_f(Cuerpo(5,14))
    snake.insertar_f(Cuerpo(4,14))
    snake.insertar_f(Cuerpo(3,14))

    while key != 27:                #run program while [ESC] key is not pressed
        if punteo > 14:
            punteo = 0
            nivel += 1
            pausa -= 5
        window.border(0)
        window.addstr(0, 47, ' SNAKE ')
        window.timeout(int(pausa - (snake.contador/5 + snake.contador/10)%120))               #delay of 100 milliseconds
        window.addstr(0, 1, ' Puntos: ' + str(punteo) + ' ')                # Printing 'Score' and
        window.addstr(0, 89, ' Nivel: ' + str(nivel) + ' ') 
        keystroke = window.getch()          #get current key being pressed
        if keystroke is not  -1:            #key is pressed
            if keystroke == KEY_LEFT and key == KEY_RIGHT:
                key = key                 #key direction changes
            elif keystroke == KEY_DOWN and key == KEY_UP:
                key = key
            elif keystroke == KEY_RIGHT and key == KEY_LEFT:
                key = key
            elif keystroke == KEY_UP and key == KEY_DOWN:
                key = key
            elif keystroke == 32:
                key = -1
            else:
                key = keystroke
        
        cuer = snake.primero
        for i in range(snake.contador):
            window.addch(cuer.y,cuer.x,' ')   #print initial dot
            if key == KEY_RIGHT:                #right direction
                cuer.x = cuer.x + 1               #pos_x increase
                if   cuer.x > width-2:
                    cuer.x = 1
            elif key == KEY_LEFT:               #left direction
                cuer.x = cuer.x - 1               #pos_x decrease
                if   cuer.x < 1:
                    cuer.x = width-2
            elif key == KEY_UP:                 #up direction
                cuer.y = cuer.y - 1               #pos_y decrease
                if   cuer.y < 1:
                    cuer.y = height-2
            elif key == KEY_DOWN:               #down direction
                cuer.y = cuer.y + 1               #pos_y increase
                if   cuer.y > height-2:
                    cuer.y = 1
            window.addch(cuer.y,cuer.x,str(i))   #print initial dot
            cuer = cuer.siguiente
    
    
    cuer = snake.primero
    for i in range(snake.contador):
        window.addch(cuer.y,cuer.x,' ')   #print initial dot
        cuer = cuer.siguiente
    curses.endwin() #return terminal to previous state


def menu():
    stdscr = curses.initscr() #initialize console
    jugador = ""
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
                if jugador != "":
                    juego(window)
                elif usuarios.primero == None:
                    key = -1
                else:
                    jugador = jugadores(window)
            elif key == 50:               #left direction
                print("2")
            elif key == 51:                 #up direction
                jugador = jugadores(window)
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
                nombre = str(line).replace("['","",1).replace("']","",1)
                if nombre != "Usuario":
                    us = Usuario(nombre)
                    usuarios.agregar(us)
        
    except FileNotFoundError:
        print("")
      
def jugadores(win):
    window = win
    key = -1
    window.border(0)
    window.addstr(0, 47, ' SNAKE ')
    us = usuarios.primero
    while key != 27:
        key = -1
        keystroke = window.getch()
        if keystroke is not  -1:            #key is pressed
            key = keystroke                 #key direction changes
        if key == KEY_LEFT:
            us = us.anterior
        if key == KEY_RIGHT:
            us = us.siguiente
        if key == 32:
            window.addstr(13, 40, '                                 ')
            curses.endwin()
            return us.nombre
        window.addstr(13, 40, '                                 ')
        window.addstr(13, 40,"<------" + str(us.nombre) + "------>")
    
    window.addstr(13, 40, '                                 ')
    curses.endwin()
    return ""


menu()