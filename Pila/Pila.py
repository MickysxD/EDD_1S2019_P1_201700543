class Pila():

    def __init__ (self):
        self.cima = None
        self.contador = 0

    def push(self, comida):
        snack = comida
        if (self.cima == None):
            self.cima = snack
            self.contador += 1
        else:
            snack.abajo = self.cima
            self.cima = snack
            self.contador += 1

    def pop(self):
        if (self.cima == None):
            self.cima = None
        else:
            temp = self.cima
            nuevo = self.cima.abajo
            self.cima = nuevo
            temp.abajo = None
            self.contador -= 1
            return temp

    def peek(self):
        return self.cima
