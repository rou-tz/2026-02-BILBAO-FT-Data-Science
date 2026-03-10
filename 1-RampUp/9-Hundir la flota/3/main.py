# main.py
from clases import Tablero
import funciones as func

def main():
    func.imprimir_instrucciones()
    
    while True:
        empezar = int(input("Escribe '1' para jugar o '0' para salir: "))
        if empezar == 1:
            break
        elif empezar == 0:
            print("¡Hasta pronto!")
            return
        else:
            print("Opción no válida. Escribe 1 o 0.")
   
    # Inicialización de tableros
    tablero_jugador = Tablero("Jugador 1")
    tablero_jugador.inicializar_tablero()

    tablero_maquina = Tablero("Máquina")
    tablero_maquina.inicializar_tablero()

    turno_jugador = True

    # Bucle principal del juego — igual que el while del notebook pero con dos jugadores
    while True:

        # Comprobamos si alguien ha ganado antes de cada turno
        if tablero_jugador.vidas == 0:
            print("\n😢 Todos tus barcos se han hundido. ¡HAS PERDIDO!")
            break
        if tablero_maquina.vidas == 0:
            print("\n🎉 ¡Has hundido toda la flota enemiga! ¡HAS GANADO!")
            break

        if turno_jugador:
            print("\n" + "=" * 40)
            print("          ¡TU TURNO!")
            print("=" * 40)
            func.imprimir_tablero(tablero_jugador.tablero, "Tus posiciones")
            func.imprimir_tablero(tablero_maquina.tablero_disparos, "Tablero de disparo")

            # Si acierta (True) sigue siendo su turno, igual que en el notebook
            turno_jugador = func.turno_jugador(tablero_maquina)

        else:
            print("\n" + "=" * 40)
            print("       TURNO DE LA MÁQUINA")
            print("=" * 40)

            # Si la máquina acierta (True) sigue siendo su turno
            turno_jugador = not func.turno_maquina(tablero_jugador)

    # Al acabar, mostramos los tableros finales
    print()
    func.imprimir_tablero(tablero_jugador.tablero, "Tu tablero final")
    func.imprimir_tablero(tablero_maquina.tablero, "Tablero de la máquina")


if __name__ == "__main__":
    main()
