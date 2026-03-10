
# main.py
import random
from clases import Tablero
import funciones as func
import variables as var

def main():
    func.imprimir_instrucciones()

    # Inicialización de jugadores
    tablero_jugador = Tablero("Jugador 1")
    tablero_jugador.inicializar_tablero()

    tablero_maquina = Tablero("Máquina")
    tablero_maquina.inicializar_tablero()

    turno_jugador = True

    while disparar(tablero):
        print("¡Turno extra! Vuelves a disparar.\n")
        print()
        imprimir_tablero(tablero)
        

if __name__ == "__main__":
    main()