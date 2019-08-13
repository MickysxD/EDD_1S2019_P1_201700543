class ListaDoble():

    def __init__ (self):
        self.primero = None
        self.ultimo = None
        self.contador = 0

    def insertar_f (self, cuerpo):
        nuevo = cuerpo
        if(self.contador == 0):
            self.primero = nuevo
            self.ultimo = nuevo
            self.contador += 1
        else:
            temp = self.ultimo
            temp.siguiente = nuevo
            nuevo.anterior = temp
            self.ultimo = nuevo
            self.contador += 1
    
    def eliminar_f (self):
        temp = self.ultimo
        temp.anterior.siguiente = None
        self.ultimo = temp.anterior
        self.contador -= 1

    def insertar_i (self, cuerpo):
        nuevo = cuerpo
        if(self.contador == 0):
            self.primero = nuevo
            self.ultimo = nuevo
            self.contador += 1
        else:
            temp = self.primero
            temp.anterior = nuevo
            nuevo.siguiente = temp
            self.primero = nuevo
            self.contador += 1
