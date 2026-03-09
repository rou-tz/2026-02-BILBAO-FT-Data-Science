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
        self.tablero = [[var.agua for _ in range(self.tamaño)] for _ in range(self.tamaño)]
        
        # Tablero de disparos (lo que ves del enemigo, empieza vacío)
        self.tablero_disparos = [[var.agua for _ in range(self.tamaño)] for _ in range(self.tamaño)]

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
        # Comprueba que el barco no se salga del tablero ni pise otro barco
        for i in range(eslora):
            f, c = fila, col
            if orientacion == 'N': f -= i
            elif orientacion == 'S': f += i
            elif orientacion == 'E': c += i
            elif orientacion == 'O': c -= i

            if f < 0 or f >= self.tamaño or c < 0 or c >= self.tamaño:
                return False
            if self.tablero[f][c] != var.AGUA:
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

    def disparar(self, fila, col):
        # Retorna True si acierta, False si falla, None si ya se había disparado ahí
        if self.tablero[fila][col] == var.barco:
            self.tablero[fila][col] = var.impacto
            self.tablero_disparos[fila][col] = var.impacto
            self.vidas -= 1
            return True
        elif self.tablero[fila][col] == var.agua:
            self.tablero[fila][col] = var.fallo
            self.tablero_disparos[fila][col] = var.fallo
            return False
        else:
            return None