from menus.menu_juego import menu_jugar_sudoku
from storage.scores import ver_mejores_puntajes
from utils.input_handler import obtener_opcion_valida
from utils.display import mostrar_mensaje

def mostrar_menu_principal():
    while True:
        print("\n=== SUDOKU ===")
        print("1. Jugar Sudoku")
        print("2. Ver mejores puntajes")
        print("3. Salir")

        opcion = obtener_opcion_valida(1, 3)

        if opcion == 1:
            menu_jugar_sudoku()
        elif opcion == 2:
            ver_mejores_puntajes()
        elif opcion == 3:
            mostrar_mensaje("¡Gracias por jugar!")
            break