
# funciones.py
import variables as var
import random
from clases import Tablero
import variables as var

def imprimir_instrucciones():
    print("=" * 50)
    print("""  
        |   |              |o         |             ,---.|         |         
        |---|.   .,---.,---|.,---.    |    ,---.    |__. |    ,---.|--- ,---.
        |   ||   ||   ||   |||        |    ,---|    |    |    |   ||    ,---|
        `   '`---'`   '`---'``        `---'`---^    `    `---'`---'`---'`---^
        """)
                 
    print("~" * 100)
    print("Instrucciones:")
    print("1. El tablero es de 10x10.")
    print("2. Juegas contra la Máquina. Tus barcos se colocarán de forma automática.")
    print(f"3. Los símbolos son: Agua ({var.agua}), Barco ({var.barco}), Tocado ({var.tocado}), Fallo ({var.fallo}).")
    print("¡¡Que gane el mejor!!")
    print("=" * 50 + "\n")

def imprimir_tablero(tablero, titulo):
    print(f"--- {titulo} ---")
    # Imprimir cabecera de columnas
    print("  " + " ".join([str(i) for i in range(var.tamaño)]))
    for i, fila in enumerate(tablero):
        print(f"{i} " + " ".join(fila))
    print("\n")
    

def coordenada(nombre):
    while True:
        valor = int(input(f"Introduce {nombre} (0-9): "))
        if 0 <= valor <= 9:
            return int(valor)
        else:
            print(f"El '{valor}' no es válido. Escribe un número entre 0 y 9.")
            

def disparar(tablero):
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
            imprimir_tablero(tablero_jugador.tablero, "Tu tablero")
            imprimir_tablero(tablero_maquina.tablero_disparos, "Tablero de la maquina")

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
            
            fila_maq = random.randint(0, var.tamaño - 1)
            col_maq = random.randint(0, var.tamaño - 1)

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