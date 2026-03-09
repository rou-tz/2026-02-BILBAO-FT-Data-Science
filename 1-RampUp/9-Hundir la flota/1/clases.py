import random
from variables import BOARD_SIZE, SHIPS, WATER, SHIP, HIT, MISS, ORIENTATIONS


class Tablero:
    """
    Representa el tablero de un jugador.

    Atributos principales
    ─────────────────────
    player_id   : str  – nombre / identificador del jugador
    size        : int  – dimensión del tablero (NxN)
    ships       : dict – {nombre_barco: eslora}
    board       : list[list]  – tablero PROPIO (barcos + impactos visibles)
    tracking    : list[list]  – tablero de SEGUIMIENTO (disparos al rival)
    ship_cells  : set  – coordenadas (fila, col) ocupadas por barcos propios
    hits_received : int – impactos recibidos (para saber si quedaste sin barcos)
    total_cells : int  – total de celdas con barco (= número de "vidas")
    """

    def __init__(self, player_id: str, size: int = BOARD_SIZE, ships: dict = None):
        self.player_id  = player_id
        self.size       = size
        self.ships      = ships if ships is not None else SHIPS.copy()

        # Tablero propio: el jugador ve sus barcos y los impactos recibidos
        self.board      = [[WATER] * size for _ in range(size)]
        # Tablero de seguimiento: solo muestra disparos propios al rival
        self.tracking   = [[WATER] * size for _ in range(size)]

        self.ship_cells      = set()   # coordenadas con barco
        self.hits_received   = 0
        self.total_cells     = sum(self.ships.values())

        self._place_all_ships()

    # ── Colocación de barcos ─────────────────────────────────────────────────

    def _place_all_ships(self):
        """Coloca todos los barcos aleatoriamente en el tablero."""
        for name, length in self.ships.items():
            placed = False
            attempts = 0
            while not placed:
                attempts += 1
                if attempts > 1000:
                    raise RuntimeError(f"No se pudo colocar el barco '{name}'. "
                                       "Revisa la configuración.")
                row    = random.randint(0, self.size - 1)
                col    = random.randint(0, self.size - 1)
                orient = random.choice(ORIENTATIONS)
                cells  = self._get_cells(row, col, length, orient)
                if cells and self._cells_are_free(cells):
                    for r, c in cells:
                        self.board[r][c] = SHIP
                        self.ship_cells.add((r, c))
                    placed = True

    def _get_cells(self, row: int, col: int, length: int, orient: str):
        """Devuelve las celdas que ocuparía un barco, o None si se sale del tablero."""
        cells = []
        deltas = {"N": (-1, 0), "S": (1, 0), "E": (0, 1), "O": (0, -1)}
        dr, dc = deltas[orient]
        for i in range(length):
            r, c = row + dr * i, col + dc * i
            if not (0 <= r < self.size and 0 <= c < self.size):
                return None
            cells.append((r, c))
        return cells

    def _cells_are_free(self, cells):
        """Comprueba que ninguna celda ni sus vecinas están ocupadas (sin solapamientos)."""
        occupied = set(cells)
        for r, c in cells:
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if (r + dr, c + dc) in self.ship_cells:
                        return False
        return True

    # ── Disparo ──────────────────────────────────────────────────────────────

    def receive_shot(self, row: int, col: int) -> bool:
        """
        Recibe un disparo en (row, col).
        Devuelve True si fue impacto, False si fue agua.
        """
        if (row, col) in self.ship_cells:
            self.board[row][col] = HIT
            self.ship_cells.discard((row, col))
            self.hits_received += 1
            return True
        else:
            if self.board[row][col] == WATER:
                self.board[row][col] = MISS
            return False

    def mark_tracking(self, row: int, col: int, hit: bool):
        """Actualiza el tablero de seguimiento tras un disparo propio."""
        self.tracking[row][col] = HIT if hit else MISS

    def already_shot(self, row: int, col: int) -> bool:
        """Comprueba si ya se disparó a esa coordenada en el tablero de seguimiento."""
        return self.tracking[row][col] != WATER

    # ── Estado del juego ─────────────────────────────────────────────────────

    def is_defeated(self) -> bool:
        """Devuelve True si todos los barcos han sido hundidos."""
        return len(self.ship_cells) == 0

    # ── Representación visual ─────────────────────────────────────────────────

    def _header(self) -> str:
        cols = "   " + "  ".join(str(i) for i in range(self.size))
        sep  = "   " + "─" * (self.size * 3 - 1)
        return f"{cols}\n{sep}"

    def print_own_board(self):
        """Imprime el tablero propio (con barcos e impactos recibidos)."""
        print(f"\n  ╔══ Tablero de {self.player_id} ══╗")
        print(self._header())
        for i, row in enumerate(self.board):
            print(f"{i} │ " + "  ".join(row))

    def print_tracking_board(self):
        """Imprime el tablero de seguimiento (disparos propios al rival)."""
        print(f"\n  ╔══ Disparos al rival ══╗")
        print(self._header())
        for i, row in enumerate(self.tracking):
            print(f"{i} │ " + "  ".join(row))
