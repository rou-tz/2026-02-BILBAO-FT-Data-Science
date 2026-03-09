
# main.py
import random
import time
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

    while True:
        # Comprobación de victoria
        if tablero_jugador.vidas == 0:
            print("¡Oh no! Todos tus barcos se han hundido. HAS PERDIDO.")
            break
        elif tablero_maquina.vidas == 0:
            print("¡Felicidades! Has hundido toda la flota de la máquina. ¡HAS GANADO!")
            break

        elif turno_jugador:
            print("\n¡TU TURNO!")
            print("*" * 40)
            # Imprime tu tablero y el radar para atacar a la máquina
            func.imprimir_tablero(tablero_jugador.tablero, "Tu tablero")
            func.imprimir_tablero(tablero_maquina.tablero_disparos, "Tablero de la maquina")

            try:
                # coords = input("Introduce coordenada de disparo (Fila,Columna)(0-9) o 'salir': ")
                # if coords.lower() == 'salir':
                #     print("¡Hasta pronto!")
                #     break

                # fila, col = map(int, coords.split(","))
                
                # if fila < 0 or fila >= var.SIZE or col < 0 or col >= var.SIZE:
                #     print("⚠️ ¡Coordenadas fuera del tablero! Inténtalo de nuevo.")
                #     continue

                # impacto = tablero_maquina.disparar(fila, col)
                
                # if impacto is None:
                #     print("⚠️ Ya habías disparado en esa coordenada. Vuelve a intentarlo.")
                #     continue
                # elif impacto:
                #     print(f"💥 ¡BOMBA! Has impactado en ({fila}, {col}). ¡Vuelves a tirar!")
                #     # Como acierta, vuelve a tocarle (turno_jugador sigue siendo True)
                # else:
                #     print(f"💦 ¡AGUA! No había nada en ({fila}, {col}). Fin de tu turno.")
                #     turno_jugador = False

            except ValueError:
                print("⚠️ Formato incorrecto. Por favor introduce dos números separados por coma (ej. 3,4).")

        else:
            # Turno de la máquina
            print("\n" + "*" * 40)
            print("TURNO DE LA MÁQUINA")
            print("*" * 40)
            time.sleep(1) # Pequeña pausa para darle emoción
            
            fila_maq = random.randint(0, var.SIZE - 1)
            col_maq = random.randint(0, var.SIZE - 1)

            impacto_maq = tablero_jugador.disparar(fila_maq, col_maq)
            
            if impacto_maq is None:
                # Si la máquina dispara donde ya había disparado, desperdicia el bucle pero sigue en su turno
                pass
            elif impacto_maq:
                print(f"💥 ¡La máquina TE HA DADO en la coordenada ({fila_maq}, {col_maq})! Vuelve a tirar la máquina.")
                # turno_jugador sigue siendo False
            else:
                print(f"💦 La máquina disparó al agua en ({fila_maq}, {col_maq}).")
                turno_jugador = True

if __name__ == "__main__":
    main()