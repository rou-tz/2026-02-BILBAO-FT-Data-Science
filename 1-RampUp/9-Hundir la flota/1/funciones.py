import random
from variables import BOARD_SIZE


def welcome():
    """Muestra el mensaje de bienvenida e instrucciones."""
    print("""
╔══════════════════════════════════════════════════════════╗
║          ⚓  HUNDIR LA FLOTA  ⚓                         ║
╠══════════════════════════════════════════════════════════╣
║  Reglas:                                                 ║
║  • El tablero es de 10x10 (filas 0-9, columnas 0-9)     ║
║  • Introduce coordenadas como:  fila columna  (ej: 3 7) ║
║  • ✦ = impacto   · = agua   ▣ = barco propio            ║
║  • Si aciertas, vuelves a disparar                       ║
║  • Hunde toda la flota enemiga para ganar               ║
╚══════════════════════════════════════════════════════════╝
""")


def ask_coordinates(board) -> tuple:
    """
    Pide coordenadas válidas al usuario.
    Valida rango, formato y que no se repita el disparo.
    Devuelve (fila, columna).
    """
    size = board.size
    while True:
        try:
            raw = input("\n🎯  Tu disparo (fila columna): ").strip()
            if raw.lower() in ("salir", "exit", "q"):
                confirm = input("¿Seguro que quieres salir? (s/n): ").strip().lower()
                if confirm == "s":
                    print("¡Hasta la próxima, capitán! ⚓")
                    exit(0)
                continue
            parts = raw.split()
            if len(parts) != 2:
                raise ValueError
            row, col = int(parts[0]), int(parts[1])
            if not (0 <= row < size and 0 <= col < size):
                print(f"  ⚠  Coordenadas fuera del tablero. Usa valores entre 0 y {size-1}.")
                continue
            if board.already_shot(row, col):
                print("  ⚠  Ya disparaste ahí. Elige otra coordenada.")
                continue
            return row, col
        except (ValueError, IndexError):
            print("  ⚠  Formato incorrecto. Escribe dos números separados por espacio (ej: 4 7).")


def machine_shot(player_board) -> tuple:
    """
    Elige una coordenada aleatoria no disparada aún en el tablero del jugador.
    Devuelve (fila, columna).
    """
    size = player_board.size
    available = [
        (r, c)
        for r in range(size)
        for c in range(size)
        if player_board.board[r][c] not in ("·", "✦")  # no repetir disparos
        # Nota: la máquina no usa tracking, comprueba directamente el board del jugador
    ]
    # Filtramos posiciones ya impactadas o con agua marcada
    available = [
        (r, c)
        for r in range(size)
        for c in range(size)
        if player_board.board[r][c] in ("~", "▣")  # solo agua sin tocar o barco sin tocar
    ]
    return random.choice(available)


def player_turn(player_board, machine_board):
    """
    Gestiona el turno completo del jugador.
    Repite mientras acierte.
    """
    print("\n" + "═" * 55)
    print("  🧑  TURNO DEL JUGADOR")
    print("═" * 55)
    player_board.print_own_board()
    machine_board.print_tracking_board()

    while True:
        row, col = ask_coordinates(machine_board)
        hit = machine_board.receive_shot(row, col)
        machine_board.mark_tracking(row, col, hit)   # actualiza tracking del jugador

        if hit:
            if machine_board.is_defeated():
                return "player_wins"
            print("  💥  ¡IMPACTO! Vuelves a disparar.")
            machine_board.print_tracking_board()
        else:
            print("  🌊  Agua. Le toca a la máquina.")
            return None


def machine_turn(player_board):
    """
    Gestiona el turno completo de la máquina.
    Repite mientras acierte.
    """
    print("\n" + "─" * 55)
    print("  🤖  TURNO DE LA MÁQUINA")
    print("─" * 55)

    while True:
        row, col = machine_shot(player_board)
        hit = player_board.receive_shot(row, col)
        print(f"  🤖  La máquina dispara a ({row}, {col}) → ", end="")

        if hit:
            if player_board.is_defeated():
                return "machine_wins"
            print("¡IMPACTO! La máquina repite turno.")
        else:
            print("Agua.")
            return None


def print_final_boards(player_board, machine_board):
    """Muestra el estado final de ambos tableros."""
    player_board.print_own_board()
    machine_board.print_tracking_board()
