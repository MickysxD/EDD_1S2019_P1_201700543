from Fila.Fila import Fila
from Fila.Puntos import Puntos

fila = Fila()
temp = Puntos(15, "Miguel")
fila.enqueue(temp)
temp = Puntos(16, "Angel")
fila.enqueue(temp)
temp = Puntos(18, "Solis")
fila.enqueue(temp)

tempo = fila.primero
for i in range(fila.contador):
    print (str(tempo.puntos) + " " + tempo.nombre)
    tempo = tempo.siguiente