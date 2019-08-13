
class Fila():

    def __init__ (self):
        self.primero = None
        self.ultimo = None
        self.contador = 0

    def enqueue (self, puntos):
        nuevo = puntos
        if (self.primero == None):
            self.primero = nuevo
            self.ultimo = nuevo
            self.contador += 1
        else:
            nuevo.siguiente = self.primero
            self.primero = nuevo
            self.contador += 1

    def dequeue (self):
        if (self.primero == None):
            self.contador = self.contador
        elif (self.primero == self.ultimo):
            self.primero = None
            self.ultimo = None
            self.contador -= 1
        else:
            temp = self.primero
            for i in range(self.contador-1):
                temp = temp.siguiente
            temp.siguiente = None
            self.contador -= 1
  
