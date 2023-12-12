# Tupla con las coordenadas de las casillas donde hay muro
muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))

# Número de filas y columnas del laberinto
filas = 5
columnas = 5

# Creamos una lista de listas que será nuestro laberinto y todas las casillas empiezan en blanco
laberinto = [[' ' for _ in range (columnas)] for _ in range (filas)]

# Asignamos que en cada coordenada de nuestra lista muro ponga x
for coordenada in muro:
    fila, columna = coordenada
    laberinto[fila][columna] = 'X'

#Imprimimos nuestro laberinto
for fila in laberinto:
    print(' '.join(fila))