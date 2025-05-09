from menus.menu_juego import menu_jugar_sudoku
from storage.scores import sistema_puntajes
from utils.display import mostrar_mensaje
from utils.input_handler import obtener_opcion_valida

def mostrar_menu_principal():
    while True:
        print("\n=== SUDOKU 4*4 ===")
        print("1. Sudoku")
        print("2. Ver mejores puntajes")
        print("3. Salir")

        opcion = obtener_opcion_valida(1, 3)

        if opcion == 1:
            menu_jugar_sudoku()
        elif opcion == 2:
            ver_estadisticas()
        elif opcion == 3:
            mostrar_mensaje("¡Gracias por jugar!")
            break

def ver_estadisticas():
    """Muestra las estadísticas actuales del jugador"""
    estadisticas = sistema_puntajes.obtener_estadisticas()
    print("\n=== Estadísticas del Jugador ===")
    print(f"Puntaje Total: {estadisticas['puntaje_total']}")
    print(f"Tableros Completados: {estadisticas['tableros_completados']}")
    print(f"Racha Actual: {estadisticas['racha_actual']}")
    print(f"Mejor Racha: {estadisticas['mejor_racha']}")