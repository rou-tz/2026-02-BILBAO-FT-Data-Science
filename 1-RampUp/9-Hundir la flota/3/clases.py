# clases.py
import variables as var

class Tablero:
    def __init__(self, jugador):
        self.jugador = jugador
        self.tamaño = var.tamaño
        self.barcos = var.barcos
        self.vidas = sum(self.barcos.values())
        
        self.tablero = [[var.agua for i in range(self.tamaño)] for i in range(self.tamaño)]
        self.tablero_disparos = [[var.agua for i in range(self.tamaño)] for i in range(self.tamaño)]

    def inicializar_tablero(self):
        t = self.tablero

        if self.jugador == "Jugador 1":
            # mini_1
            t[0][0] = var.barco
            # mini_2
            t[0][2] = var.barco
            # mini_3
            t[0][4] = var.barco
            # mini_4
            t[0][6] = var.barco

            # semi_1
            t[2][0] = var.barco
            t[2][1] = var.barco
            # semi_2
            t[2][4] = var.barco
            t[2][5] = var.barco
            # semi_3
            t[2][7] = var.barco
            t[2][8] = var.barco

            # grande_1
            t[4][0] = var.barco
            t[4][1] = var.barco
            t[4][2] = var.barco
            # grande_2
            t[4][5] = var.barco
            t[4][6] = var.barco
            t[4][7] = var.barco

            # gigante
            t[6][0] = var.barco
            t[6][1] = var.barco
            t[6][2] = var.barco
            t[6][3] = var.barco

        else:  # Máquina
            # mini_1
            t[0][1] = var.barco
            # mini_2
            t[0][3] = var.barco
            # mini_3
            t[0][5] = var.barco
            # mini_4
            t[0][7] = var.barco

            # semi_1
            t[2][0] = var.barco
            t[2][1] = var.barco
            # semi_2
            t[2][4] = var.barco
            t[2][5] = var.barco
            # semi_3
            t[2][7] = var.barco
            t[2][8] = var.barco

            # grande_1
            t[5][0] = var.barco
            t[5][1] = var.barco
            t[5][2] = var.barco
            # grande_2
            t[5][5] = var.barco
            t[5][6] = var.barco
            t[5][7] = var.barco

            # gigante
            t[8][3] = var.barco
            t[8][4] = var.barco
            t[8][5] = var.barco
            t[8][6] = var.barco

    def disparar(self, fila, col):
        casilla = self.tablero[fila][col]
        
        if casilla in (var.tocado, var.fallo):
            return None
        elif casilla == var.barco:
            self.tablero[fila][col] = var.tocado
            self.tablero_disparos[fila][col] = var.tocado
            self.vidas -= 1
            return True
        else:
            self.tablero[fila][col] = var.fallo
            self.tablero_disparos[fila][col] = var.fallo
            return False