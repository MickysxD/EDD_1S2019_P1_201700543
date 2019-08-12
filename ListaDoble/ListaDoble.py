class ListaDoble():

    def __init__ (self):
        self.primero = None
        self.ultimo = None
        self.contador = 0

    def insertar_f (self, cuerpo):
        nuevo = cuerpo
        if(self.contador == 0):
            nuevo.anterior = nuevo
            nuevo.siguiente = nuevo
            self.primero = nuevo
            self.ultimo = nuevo
            self.contador += 1
        else:
            temp = self.ultimo
            temp.siguiente = nuevo
            nuevo.anterior = temp
            self.primero.anterior = nuevo
            nuevo.siguiente = self.primero
            self.ultimo = nuevo
            self.contador += 1
    
    def eliminar_f (self):
        if (self.contador == 0):
            contador = 0
        else:
            temp = self.ultimo
            temp.anterior.siguiente = self.ultimo.siguiente
            temp.siguiente.anterior = self.ultimo.anterior
            self.contador -= 1
