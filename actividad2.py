#!/usr/bin/env python3

# Adrián Lattes Grassi
# 18/09/2022

from copy import deepcopy
from itertools import product
from typing import Callable, List, Literal, Tuple, TypeAlias, Union

# Tipo para las celdas: 0 o 1
CellState: TypeAlias = Union[Literal[0], Literal[1]]

# Tipo para el tablero: lista de listas de celdas
BoardState: TypeAlias = List[List[CellState]]

# Funcíon que obtiene las dimensiones de un tablero
board_size: Callable[[BoardState], Tuple[int, int]] = lambda board: (
    len(board),
    len(board[0]),
)

# Funcíon auxiliar que devuelve una tupla de rangos dadas unas dimensiones
size_range: Callable[[Tuple[int, int]], Tuple[range, range]] = lambda size: (
    range(size[0]),
    range(size[1]),
)

# Función que devuelve una lista de tuplas con todas las posiciones de un tablero
board_positions: Callable[[BoardState], List[Tuple[int, int]]] = lambda board: (
    list(product(*size_range(board_size(board))))
)


def neighbors(board: BoardState, x: int, y: int) -> int:
    """Dado un tablero y una posición cuenta la cantidad de vecinos."""
    n = 0
    for (dx, dy) in product([-1, 0, 1], [-1, 0, 1]):
        if (
            (dx, dy) != (0, 0)
            and 0 <= x + dx < len(board)
            and 0 <= y + dy < len(board[0])
        ):
            n += board[x + dx][y + dy]
    return n


def iterate(board: BoardState) -> BoardState:
    """Función central del algoritmo: calcula la siguiente iteración de un tablero."""
    result = deepcopy(board)
    for (x, y) in board_positions(board):
        n = neighbors(board, x, y)
        if board[x][y] == 1:
            result[x][y] = 1 if n == 2 or n == 3 else 0
        elif board[x][y] == 0:
            result[x][y] = 1 if n == 3 else 0
    return result


def conway(board: BoardState, rows: int, cols: int, k: int):
    """
    Wrapper de la función iterate. Calcula k iteraciones.

    Los parámetros rows y cols no se usan (los proporciona la función board_size).
    """
    assert k >= 0, "El número de iteraciones k debe ser un entero no negativo."
    assert board_size(board) == (rows, cols), "Número incorrecto de filas o columnas."

    result = deepcopy(board)
    for _ in range(k):
        result = iterate(result)
    return result


def print_board(board: BoardState):
    """Utilidad extra para imprimir tableros."""
    _, Y = board_size(board)
    for (x, y) in board_positions(board):
        print("." if board[x][y] else " ", end=" " if y != Y - 1 else "\n")


def draw_board(board: BoardState, cell_size: int):
    """
    Utilidad extra que usa el módulo PIL (paquete pillow) para generar una
    imagen de un tablero.
    """
    from PIL import Image, ImageDraw

    rows, cols = board_size(board)
    img = Image.new("1", (rows * cell_size, cols * cell_size))
    draw = ImageDraw.Draw(img)
    for (x, y) in board_positions(board):
        rect = (x * cell_size, y * cell_size, (x + 1) * cell_size, (y + 1) * cell_size)
        if board[x][y] == 1:
            draw.rectangle(rect, fill="#000000", outline="white")
        elif board[x][y] == 0:
            draw.rectangle(rect, fill="#ffffff", outline="white")
    return img
