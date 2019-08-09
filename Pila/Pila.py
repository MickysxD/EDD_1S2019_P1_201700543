class Pila():

    def __init__ (self):
        self.cima = None

    def push(self, comida):
        snack = comida
        if (self.cima == None):
            self.cima = snack
        else:
            snack.abajo = self.cima
            self.cima = snack

    def pop(self):
        if (self.cima == None):

        else:
            temp = self.cima
            nuevo = self.cima.abajo
            self.cima = nuevo
            temp.abajo = None
            return temp

    def peek(self):
        return self.cima
