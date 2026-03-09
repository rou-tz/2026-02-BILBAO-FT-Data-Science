# ─── Dimensiones del tablero ───────────────────────────────────────────────
BOARD_SIZE = 10

# ─── Flota (nombre: eslora) ─────────────────────────────────────────────────
SHIPS = {
    "Lancha 1":    1,
    "Lancha 2":    1,
    "Lancha 3":    1,
    "Lancha 4":    1,
    "Destructor 1": 2,
    "Destructor 2": 2,
    "Destructor 3": 2,
    "Crucero 1":   3,
    "Crucero 2":   3,
    "Acorazado":   4,
}

# ─── Símbolos del tablero ───────────────────────────────────────────────────
WATER      = "~"   # agua sin disparar
SHIP       = "▣"   # barco sin tocar  (tu tablero)
HIT        = "✦"   # impacto
MISS       = "·"   # agua disparada

# ─── Orientaciones ──────────────────────────────────────────────────────────
ORIENTATIONS = ["N", "S", "E", "O"]
