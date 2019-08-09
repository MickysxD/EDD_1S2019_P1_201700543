class ListaCircular():

    def __init__ (self):
        self.primero = None
        
    def agregar (self, nodo):
        nuevo = nodo
        if (self.primero == None):
            self.primero = nuevo
            self.primero.siguiente = self.primero
            self.primero.anterior = self.primero
        else:
            temp = self.primero.anterior
            temp.siguiente = nuevo
            nuevo.anterior = temp
            self.primero.anterior = nuevo
            nuevo.siguiente = self.primero
            self.primero = nuevo