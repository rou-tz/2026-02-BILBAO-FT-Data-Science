# funciones.py
import variables as var
import random



def imprimir_instrucciones():
    print("~" * 100)
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
    print("=" * 100 + "\n")
   
   
    
    """
    Esta funcion imprime el tablero y le añade las posiciones de 0 a 9, le entran dos inputs, tablero y titulo.
    I
    """
def imprimir_tablero(tablero, titulo):
    print(f"      --- {titulo} ---")
    print("     " + "  ".join([str(i) for i in range(var.tamaño)]))
    print("  " + "---" * 11)
    for i, fila in enumerate(tablero):
        print(f"{i} |  " + "  ".join(fila))
    print()

    
    """
    Esta funcion sirve para verificar si la coordenada es correcta o no.
    Tiene dentro un bucle que devuelve el valor si es un numero entre 0 y 9
    """
def coordenada(nombre):
    while True:
        try:
            valor = int(input(f"Introduce {nombre} (0-9): "))
            if 0 <= valor <= 9:
                return valor
            else:
                print(f"El '{valor}' no es válido. Escribe un número entre 0 y 9.")
        except ValueError:
            print("Eso no es un número. Escribe un número entre 0 y 9.")


def turno_jugador(tablero_maquina):
    """
    Le pide al jugador coordenadas y dispara al tablero de la máquina.
    Devuelve True si tocó, False si agua.
    (Si la coordenada ya fue usada, pide otra.)
    """
    while True:
        fila = coordenada("la fila   ")
        col  = coordenada("la columna")
        resultado = tablero_maquina.disparar(fila, col)

        if resultado is None:
            print("Ya habías disparado ahí. Elige otra coordenada.")
        elif resultado:
            print(f"\n¡TOCADO en ({fila}, {col})! ¡Vuelves a tirar!")
            return True
        else:
            print(f"\n¡Ohh Agua! en ({fila}, {col}). Fin de tu turno.")
            return False


def turno_maquina(tablero_jugador):
    """
    La máquina dispara en una posición aleatoria del tablero del jugador.
    Devuelve True si ha acertado, False si es agua.
    """
    while True:
        fila = random.randint(0, var.tamaño - 1)
        col  = random.randint(0, var.tamaño - 1)
        resultado = tablero_jugador.disparar(fila, col)

        if resultado is None:
            continue            # ya disparó ahí, intenta otra
        elif resultado:
            print(f"¡La máquina te ha dado en ({fila}, {col})! Vuelve a tirar la máquina.")
            return True
        else:
            print(f" La máquina disparó al agua en ({fila}, {col}).")
            return False
