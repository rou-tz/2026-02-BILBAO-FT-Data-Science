
# funciones.py
import variables as var

def imprimir_instrucciones():
    print("=" * 50)
    print("🚢 BIENVENIDO A HUNDIR LA FLOTA 🚢")
    print("=" * 50)
    print("Instrucciones:")
    print("1. El tablero es de 10x10.")
    print("2. Juegas contra la Máquina. Tus barcos se colocarán automáticamente.")
    print(f"3. Los símbolos son: Agua ({var.agua}), Barco ({var.barco}), Impacto ({var.impacto}), Fallo ({var.fallo}).")
    print("4. Gana el primero que hunda todos los barcos del rival.")
    print("¡¡Que gane el mejor!!")
    print("=" * 50 + "\n")

def imprimir_tablero(tablero, titulo):
    print(f"--- {titulo} ---")
    # Imprimir cabecera de columnas
    print("  " + " ".join([str(i) for i in range(var.SIZE)]))
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