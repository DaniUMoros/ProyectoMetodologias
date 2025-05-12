# menus/menu_principal.py
from menus.menu_juego import menu_jugar_sudoku
from utils.display import mostrar_mensaje
from utils.input_handler import obtener_opcion_valida
from storage.scores import cargar_scores

def mostrar_menu_principal():
    while True:
        print("\n=== SUDOKU 4×4 ===")
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
    """Muestra la lista de mejores puntajes registrados en scores.json"""
    records = cargar_scores()

    print("\n=== Mejores Puntajes ===")
    if not records:
        print("Aún no hay registros de puntajes.\n")
    else:
        for idx, rec in enumerate(records, start=1):
            total = sum(rec['puntaje_por_sudoku'])
            bonus_total = sum(rec['puntos_de_bonificacion'])
            print(f"{idx}. Jugador: {rec['nombre']}")
            print(f"   Tableros completados: {rec['tableros_completados']}")
            print(f"   Puntajes por sudoku: {rec['puntaje_por_sudoku']}")
            print(f"   Bonificaciones: {rec['puntos_de_bonificacion']} (total bonus {bonus_total})")
            print(f"   Puntaje total: {total}\n")

    input("Presiona Enter para volver al menú principal...")
