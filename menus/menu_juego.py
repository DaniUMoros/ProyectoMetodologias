from core.sudoku_generator import crear_nuevo_juego
from utils.input_handler import obtener_opcion_valida
from utils.display import mostrar_mensaje

class ConfiguracionJuego:
    def __init__(self):
        self.tipo_sudoku = 9  # Por defecto 9x9
        self.dificultad = "Medio"  # Por defecto dificultad media

config_juego = ConfiguracionJuego()

def menu_jugar_sudoku():
    while True:
        print("\n=== CONFIGURACIÓN DE JUEGO ===")
        print("1. Seleccionar tipo de Sudoku")
        print("2. Seleccionar nivel de dificultad")
        print("3. Comenzar juego")
        print("4. Volver al menú principal")

        opcion = obtener_opcion_valida(1, 4)

        if opcion == 1:
            seleccionar_tipo_sudoku()
        elif opcion == 2:
            seleccionar_dificultad()
        elif opcion == 3:
            iniciar_juego()
        elif opcion == 4:
            break

def seleccionar_tipo_sudoku():
    print("\n=== TIPOS DE SUDOKU ===")
    print("1. Sudoku Clásico (9x9)")
    print("2. Sudoku Mini (6x6)")
    print("3. Volver")

    opcion = obtener_opcion_valida(1, 3)
    if opcion == 1:
        config_juego.tipo_sudoku = 9
        mostrar_mensaje("Has seleccionado Sudoku Clásico (9x9)")
    elif opcion == 2:
        config_juego.tipo_sudoku = 6
        mostrar_mensaje("Has seleccionado Sudoku Mini (6x6)")

def seleccionar_dificultad():
    print("\n=== NIVEL DE DIFICULTAD ===")
    print("1. Fácil")
    print("2. Medio")
    print("3. Difícil")
    print("4. Volver")

    opcion = obtener_opcion_valida(1, 4)
    if opcion == 1:
        config_juego.dificultad = "Fácil"
    elif opcion == 2:
        config_juego.dificultad = "Medio"
    elif opcion == 3:
        config_juego.dificultad = "Difícil"

    if opcion in [1, 2, 3]:
        mostrar_mensaje(f"Has seleccionado el nivel: {config_juego.dificultad}")

def iniciar_juego():
    tablero, solucion = crear_nuevo_juego(config_juego.tipo_sudoku, config_juego.dificultad)
    jugar_sudoku(tablero, solucion)

def jugar_sudoku(tablero, solucion):
    while True:
        print("\n=== SUDOKU ===")
        imprimir_tablero(tablero)
        print("\nComandos:")
        print("- Ingresar jugada: fila columna valor (ejemplo: 1 2 5)")
        print("- Salir: 0")

        entrada = input("\nIngrese su jugada o 0 para salir: ").strip()

        if entrada == "0":
            break

        try:
            fila, col, valor = map(int, entrada.split())
            if validar_entrada(fila, col, valor, tablero):
                if valor == solucion[fila-1][col-1]:
                    tablero[fila-1][col-1] = valor
                    if tablero_completo(tablero):
                        print("\n¡Felicitaciones! ¡Has completado el Sudoku!")
                        break
                else:
                    print("\nValor incorrecto. Intenta de nuevo.")
            else:
                print("\nEntrada inválida. Asegúrate de que los números estén dentro del rango permitido.")
        except ValueError:
            print("\nEntrada inválida. Usa el formato: fila columna valor")

def imprimir_tablero(tablero):
    size = len(tablero)
    box_size = 3 if size == 9 else 2

    print("    " + " ".join(str(i+1) for i in range(size)))
    print("  +" + "-" * (size * 2 + 1))

    for i in range(size):
        print(f"{i+1} | ", end="")
        for j in range(size):
            print(tablero[i][j] if tablero[i][j] != 0 else "·", end=" ")
        print()

def validar_entrada(fila, col, valor, tablero):
    size = len(tablero)
    return 1 <= fila <= size and 1 <= col <= size and 1 <= valor <= size

def tablero_completo(tablero):
    return all(all(cell != 0 for cell in row) for row in tablero)