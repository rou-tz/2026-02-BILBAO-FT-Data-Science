# 🚢 Hundir la Flota

Un juego clásico de **Hundir la Flota** para la terminal, desarrollado en Python. Juega contra la máquina en un tablero de 10×10 e intenta hundir toda su flota antes de que ella hunda la tuya.

---

## 🎮 ¿Cómo se juega?

1. Ejecuta el juego desde la terminal.
2. Introduce coordenadas (fila y columna, del 0 al 9) para disparar al tablero de la máquina.
3. Si aciertas un barco, **vuelves a tirar**. Si fallas, le toca a la máquina.
4. Gana quien hunda toda la flota del rival primero.

---

## 🗂️ Estructura del proyecto

```
hundir-la-flota/
│
├── main.py          # Punto de entrada. Contiene el bucle principal del juego
├── clases.py        # Clase Tablero: atributos y métodos del tablero (disparar, inicializar)
├── funciones.py     # Funciones auxiliares: imprimir tablero, turnos, instrucciones
└── variables.py     # Configuración global: tamaño, barcos y símbolos
```

---

## 🛳️ Flota disponible

| Barco     | Tamaño   | Cantidad |
|-----------|----------|----------|
| Mini      | 1 celda  | 4        |
| Semi      | 2 celdas | 3        |
| Grande    | 3 celdas | 2        |
| Gigante   | 4 celdas | 1        |

**Total de vidas:** 20 impactos para hundir toda la flota.

---

## 🗺️ Símbolos del tablero

| Símbolo | Significado |
|---------|-------------|
| `~`     | Agua        |
| `B`     | Barco       |
| `X`     | Tocado      |
| `o`     | Fallo       |

---

## ▶️ Ejecución

Asegúrate de tener **Python 3** instalado. Luego, desde la carpeta del proyecto:

```bash
python main.py
```

No se necesitan librerías externas. Solo se usa la librería estándar de Python (`random`).

---

## 📋 Requisitos

- Python 3.x
- Terminal / consola

---

## 📁 Descripción de los archivos

### `variables.py`
Define la configuración global del juego: el tamaño del tablero (10×10), el diccionario de barcos y los símbolos visuales.

### `clases.py`
Contiene la clase `Tablero`, que gestiona:
- El tablero propio y el tablero de disparos.
- La colocación fija de barcos para el jugador y la máquina.
- El método `disparar()`, que procesa cada disparo y actualiza el estado.

### `funciones.py`
Funciones de apoyo:
- `imprimir_instrucciones()`: muestra la pantalla de bienvenida.
- `imprimir_tablero()`: renderiza el tablero en consola con coordenadas.
- `coordenada()`: valida la entrada del usuario.
- `turno_jugador()` / `turno_maquina()`: gestionan el turno de cada participante.

### `main.py`
Orquesta el juego completo: inicializa los tableros, controla el flujo de turnos y determina el ganador.

---

## 🤖 Comportamiento de la máquina

La máquina dispara en posiciones **aleatorias** usando `random.randint()`. Nunca repite una casilla ya disparada.

---

## 🙋 Autor

Desarrollado como proyecto de aprendizaje de Python.
