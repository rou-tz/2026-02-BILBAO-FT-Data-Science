from clases import Tablero
from funciones import welcome, player_turn, machine_turn, print_final_boards
from variables import BOARD_SIZE, SHIPS


def main():
    welcome()

    # ── Inicialización ───────────────────────────────────────────────────────
    player_name   = input("¿Cómo te llamas, capitán? ").strip() or "Jugador"
    player_board  = Tablero(player_id=player_name,  size=BOARD_SIZE, ships=SHIPS.copy())
    machine_board = Tablero(player_id="Máquina",    size=BOARD_SIZE, ships=SHIPS.copy())

    print(f"\n✅  ¡Tableros listos! Tienes {player_board.total_cells} posiciones de barco.")
    print("   Escribe 'salir' en cualquier momento para abandonar la partida.\n")

    # ── Bucle principal ──────────────────────────────────────────────────────
    while True:

        # Turno del jugador
        result = player_turn(player_board, machine_board)
        if result == "player_wins":
            print_final_boards(player_board, machine_board)
            print("\n🏆  ¡ENHORABUENA! ¡Has hundido toda la flota enemiga! 🏆\n")
            break

        # Turno de la máquina
        result = machine_turn(player_board)
        if result == "machine_wins":
            player_board.print_own_board()
            print("\n💀  La máquina ha hundido todos tus barcos. ¡Derrota! 💀\n")
            break


if __name__ == "__main__":
    main()
