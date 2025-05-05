from utils.input_handler import obtener_opcion_valida
from utils.display import mostrar_mensaje
from config.settings import TIPOS_SUDOKU, DIFICULTADES

def menu_jugar_sudoku():
    while True:
        print("\n=== CONFIGURACIÓN DE JUEGO ===")
        print("1. Seleccionar tipo de Sudoku")
        print("2. Seleccionar nivel de dificultad")
        print("3. Volver al menú principal")

        opcion = obtener_opcion_valida(1, 3)

        if opcion == 1:
            seleccionar_tipo_sudoku()
        elif opcion == 2:
            seleccionar_dificultad()
        elif opcion == 3:
            break

def seleccionar_tipo_sudoku():
    print("\n=== TIPOS DE SUDOKU ===")
    for i, tipo in enumerate(TIPOS_SUDOKU, 1):
        print(f"{i}. {tipo}")
    print(f"{len(TIPOS_SUDOKU) + 1}. Volver")

    opcion = obtener_opcion_valida(1, len(TIPOS_SUDOKU) + 1)
    if opcion <= len(TIPOS_SUDOKU):
        mostrar_mensaje(f"Has seleccionado {TIPOS_SUDOKU[opcion-1]}")

def seleccionar_dificultad():
    print("\n=== NIVEL DE DIFICULTAD ===")
    for i, dificultad in enumerate(DIFICULTADES, 1):
        print(f"{i}. {dificultad}")
    print(f"{len(DIFICULTADES) + 1}. Volver")

    opcion = obtener_opcion_valida(1, len(DIFICULTADES) + 1)
    if opcion <= len(DIFICULTADES):
        mostrar_mensaje(f"Has seleccionado el nivel: {DIFICULTADES[opcion-1]}")