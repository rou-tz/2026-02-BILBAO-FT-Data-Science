# main.py
from clases import Tablero
import funciones as func

""" 
Esta es la funcion principal que llama a todas las funciones
"""
def main():
    func.imprimir_instrucciones()
    
    while True:
        print("Introduce una moneda de 1€ para jugar")
        empezar = int(input("Escribe '1' para jugar o '0' para salir: "))
        if empezar == 1:
            break
        elif empezar == 0:
            print("¡Hasta pronto!")
            return
        else:
            print("Opción no válida. Escribe 1 o 0.")
   
    #Inicializamos los dos tableros
    tablero_jugador = Tablero("Jugador 1")
    tablero_jugador.inicializar_tablero()

    tablero_maquina = Tablero("Maquina")
    tablero_maquina.inicializar_tablero()

    turno_jugador = True

    #El bucle comienza siempre que el turno sea True
    while True:

        #Comprobamos las vidas que son el numero total que ocupan los barcos, 20 en total
        if tablero_jugador.vidas == 0:
            print("\n😢 Todos tus barcos se han hundido. ¡HAS PERDIDO!")
            break
        elif tablero_maquina.vidas == 0:
            print("\n🎉 ¡Has hundido toda la flota enemiga! ¡HAS GANADO!")
            break
        
        #Empezamos con el turno del jugador 1
        elif turno_jugador:
            print("\n" + "=" * 50)
            print("              ¡TU TURNO!")
            print("=" * 50)
            func.imprimir_tablero(tablero_jugador.tablero, "Tus posiciones")
            func.imprimir_tablero(tablero_maquina.tablero_disparos, "Tablero de disparo")

            #Devuelve un true si acierta y puede seguir tirando en ese caso.
            turno_jugador = func.turno_jugador(tablero_maquina)

        else:
            print("\n" + "=" * 50)
            print("       TURNO DE LA MÁQUINA")
            print("=" * 50)

            #Al añadir el not nos aseguramos que si acierta, devuelve un False y puede volver a tirar
            turno_jugador = not func.turno_maquina(tablero_jugador)

    # Al acabar, mostramos los tableros finales
    print()
    func.imprimir_tablero(tablero_jugador.tablero, "Tu tablero final")
    func.imprimir_tablero(tablero_maquina.tablero, "Tablero de la máquina")


#Esto ejecuta el juego directamente
if __name__ == "__main__":
    main()
