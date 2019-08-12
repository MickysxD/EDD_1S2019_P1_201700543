from Fila.Fila import Fila
from Fila.Puntos import Puntos
from ListaCircularDoble.LiscaCircular import ListaCircular
from ListaCircularDoble.Usuarios import Usuario
from ListaDoble.ListaDoble import ListaDoble
from ListaDoble.Cuerpo import Cuerpo
from Pila.Pila import Pila
from Pila.Comida import Snack1
from Pila.Comida import Snack2

import curses #import the curses library
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN, KEY_ENTER #import special KEYS from the curses library
import csv
from random import randint

height = 30
width = 100
usuarios = ListaCircular()
puntajes = Fila()

def juego(win):
    window = win

    punteot = 0
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
    bueno = Snack1(40,12)
    malo = Snack2(50,3)
    comida = Pila()

    while key != 27:                #run program while [ESC] key is not pressed
        if punteo > 14:
            ts = snake.primero
            for i in range(snake.contador):
                window.addch(ts.y, ts.x, ' ')
                ts = ts.siguiente
            punteot += punteo
            punteo = 0
            nivel += 1
            pausa -= 5
            snake = ListaDoble()
            snake.insertar_f(Cuerpo(5,14))
            snake.insertar_f(Cuerpo(4,14))
            snake.insertar_f(Cuerpo(3,14))
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
        
        window.addch(bueno.y,bueno.x,'+')
        window.addch(malo.y,malo.x,'*')

        cuer = snake.ultimo
        px = snake.primero.x
        py = snake.primero.y
        for i in range(snake.contador):
            window.addch(cuer.y,cuer.x,' ')
            cuer.x = cuer.anterior.x
            cuer.y = cuer.anterior.y
            cuer = cuer.anterior

        cuer = snake.primero
        cuer.x = px
        cuer.y = py
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
        
        cuer = snake.primero
        for i in range(snake.contador):
            window.addch(cuer.y,cuer.x,"#")
            cuer = cuer.siguiente

        if bueno.x == snake.primero.x and bueno.y == snake.primero.y:
            comida.push(bueno)
            bueno = None
            punteo += 1
            while bueno == None:
                bueno = Snack1(randint(2,width-2),randint(2,height-2))
                cuer = snake.primero
                for i in range(snake.contador):
                    if bueno.x == cuer.x and bueno.y == cuer.y:
                        bueno = None
                    cuer = cuer.siguiente

            cuer = snake.primero
            nx = cuer.x
            ny = cuer.y

            if key == KEY_RIGHT:                #right direction
                nx = cuer.x + 1               #pos_x increase
                if   nx > width-2:
                    nx = 1
            elif key == KEY_LEFT:               #left direction
                nx = cuer.x - 1               #pos_x decrease
                if   nx < 1:
                    nx = width-2
            elif key == KEY_UP:                 #up direction
                ny = cuer.y - 1               #pos_y decrease
                if   nx < 1:
                    nx= height-2
            elif key == KEY_DOWN:               #down direction
                nx = cuer.y + 1               #pos_y increase
                if   nx > height-2:
                    nx = 1
            ct = Cuerpo(nx,ny)
            snake.insertar_i(ct)
        
        if malo.x == snake.primero.x and malo.y == snake.primero.y:
            comida.pop()
            malo = None
            if snake.contador > 3:
                snake.eliminar_f()
                punteo -= 1
            while malo == None:
                malo = Snack1(randint(2,width-2),randint(2,height-2))
                cuer = snake.primero
                for i in range(snake.contador):
                    if malo.x == cuer.x and malo.y == cuer.y:
                        malo = None
                    cuer = cuer.siguiente


        

        
    window.addch(bueno.y,bueno.x,' ')
    window.addch(malo.y,malo.x,' ')
    cuer = snake.primero
    for i in range(snake.contador):
        window.addch(cuer.y,cuer.x,' ')   #print initial dot
        cuer = cuer.siguiente
    curses.endwin() #return terminal to previous state
    return punteot


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
                    p = juego(window)
                    pun = Puntos(p, jugador)
                    if (puntajes.contador == 10):
                        puntajes.dequeue()
                    puntajes.enqueue(pun)
                elif usuarios.primero == None:
                    key = -1
                else:
                    jugador = jugadores(window)
            elif key == 50:               #left direction
                tablap(window)
            elif key == 51:                 #up direction
                if usuarios.primero != None:
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
    window.addstr(0, 47, ' cambio ')
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

def tablap(win):
    window = win
    key = -1
    window.border(0)
    window.addstr(0, 47, ' SNAKE ')
    window.addstr(5, 43, "Top 10 puntajes")

    pt = puntajes.primero
    for i in range(puntajes.contador):
        window.addstr(9+i, 45, pt.nombre + ": " + str(pt.puntos))
        pt = pt.siguiente
    
    while key != 27:
        key = -1
        keystroke = window.getch()
        if keystroke is not  -1:            #key is pressed
            key = keystroke                 #key direction changes
    
    window.addstr(5, 38, "                              ")
    pt = puntajes.primero
    for i in range(puntajes.contador):
        window.addstr(9+i, 45, '                                 ')
        pt = pt.siguiente
    curses.endwin()

menu()