# clases.py
import random
import variables as var

class Tablero:
    def __init__(self, jugador):
        self.jugador = jugador
        self.tamaño = var.tamaño
        self.barcos = var.barcos
        # Vidas totales = suma de todas las esloras
        self.vidas = sum(self.barcos.values())
        
        # Tablero propio (donde están tus barcos y los impactos que recibes)
        self.tablero = [[var.agua for i in range(self.tamaño)] for i in range(self.tamaño)]
        
        # Tablero de disparos (lo que ves del enemigo, empieza vacío)
        self.tablero_disparos = [[var.agua for i in range(self.tamaño)] for i in range(self.tamaño)]

    def inicializar_tablero(self):
        for nombre, eslora in self.barcos.items():
            colocado = False
            while not colocado:
                fila = random.randint(0, self.tamaño - 1)
                col = random.randint(0, self.tamaño - 1)
                orientacion = random.choice(['N', 'S', 'E', 'O'])
                
                if self._puede_colocar(fila, col, eslora, orientacion):
                    self._colocar_barco(fila, col, eslora, orientacion)
                    colocado = True

    def _puede_colocar(self, fila, col, eslora, orientacion):
        for i in range(eslora):
            f, c = fila, col
            if orientacion == 'N': f -= i
            elif orientacion == 'S': f += i
            elif orientacion == 'E': c += i
            elif orientacion == 'O': c -= i

            if f < 0 or f >= self.tamaño or c < 0 or c >= self.tamaño:
                return False
            if self.tablero[f][c] != var.agua:   # <-- CORREGIDO: var.AGUA → var.agua
                return False
        return True

    def _colocar_barco(self, fila, col, eslora, orientacion):
        for i in range(eslora):
            f, c = fila, col
            if orientacion == 'N': f -= i
            elif orientacion == 'S': f += i
            elif orientacion == 'E': c += i
            elif orientacion == 'O': c -= i
            self.tablero[f][c] = var.barco

    # NUEVO: método disparar que recibe unas coordenadas y actualiza el tablero
    def disparar(self, fila, col):
        casilla = self.tablero[fila][col]
        
        if casilla in (var.tocado, var.fallo):
            return None                          # ya disparado aquí antes
        elif casilla == var.barco:
            self.tablero[fila][col] = var.tocado
            self.tablero_disparos[fila][col] = var.tocado
            self.vidas -= 1
            return True                          # tocado
        else:
            self.tablero[fila][col] = var.fallo
            self.tablero_disparos[fila][col] = var.fallo
            return False                         # agua
