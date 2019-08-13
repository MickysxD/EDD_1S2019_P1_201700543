class ListaCircular():

    def __init__ (self):
        self.primero = None
        self.contador = 0
        
    def agregar (self, nodo):
        nuevo = nodo
        if (self.primero == None):
            self.primero = nuevo
            self.primero.siguiente = self.primero
            self.primero.anterior = self.primero
            self.contador += 1
        else:
            temp = self.primero.anterior
            temp.siguiente = nuevo
            nuevo.anterior = temp
            self.primero.anterior = nuevo
            nuevo.siguiente = self.primero
            self.primero = nuevo
            self.contador += 1