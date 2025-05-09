from core.sudoku_generator import crear_nuevo_juego, SudokuGenerator

def menu_jugar_sudoku():
    while True:
        print("\n=== MENÚ PRINCIPAL SUDOKU 4x4 ===")
        print("1. Jugar Sudoku")
        print("2. Ver instrucciones")
        print("3. Salir")

        opcion = input("Seleccione una opción (1-3): ")
        if opcion == "1":
            jugar_sudoku()
        elif opcion == "2":
            mostrar_instrucciones()
        elif opcion == "3":
            print("¡Gracias por jugar!")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

def mostrar_instrucciones():
    print("\n=== INSTRUCCIONES ===")
    print("1. El objetivo es llenar una cuadrícula de 4x4 con números del 1 al 4")
    print("2. Cada número debe aparecer una sola vez en cada fila")
    print("3. Cada número debe aparecer una sola vez en cada columna")
    print("4. Cada número debe aparecer una sola vez en cada subcuadrícula de 2x2")
    print("\nPresione Enter para continuar...")
    input()

def seleccionar_dificultad():
    while True:
        print("\n=== SELECCIONAR DIFICULTAD ===")
        print("1. Fácil (6 casillas vacías)")
        print("2. Difícil (10 casillas vacías)")

        opcion = input("Seleccione la dificultad (1-2): ")
        if opcion == "1":
            return "Fácil"
        elif opcion == "2":
            return "Difícil"
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

def seleccionar_representacion():
    print("\n=== TIPO DE REPRESENTACIÓN ===")
    print("1. Números (1-4)")
    print("2. Letras (A-D)")
    print("3. Símbolos (★, ♦, ♣, ♠)")

    while True:
        opcion = input("Seleccione el tipo de representación (1-3): ")
        tipos = {
            "1": "numeros",
            "2": "letras",
            "3": "simbolos"
        }
        if opcion in tipos:
            return tipos[opcion]
        print("Opción inválida. Por favor, intente de nuevo.")

def jugar_sudoku():
    while True:  # Bucle principal para múltiples juegos
        dificultad = seleccionar_dificultad()
        tipo_representacion = seleccionar_representacion()

        tablero, solucion = crear_nuevo_juego(dificultad, tipo_representacion)
        generador = SudokuGenerator(
            tipo_representacion=tipo_representacion,
            dificultad=dificultad
        )
        generador.tablero = tablero

        while True:  # Bucle para un juego individual
            print(f"\n=== SUDOKU 4x4 - Nivel: {dificultad} ===")
            generador.imprimir_tablero()
            print("\nComandos:")
            print("- Para jugar: ingrese fila columna valor (ejemplo: 1 2 3)")
            print("- Para salir: ingrese 'salir'")

            entrada = input("\nIngrese su jugada: ").lower()
            if entrada == 'salir':
                return  # Salir completamente del juego

            try:
                fila, columna, valor = map(int, entrada.split())
                if not (1 <= fila <= 4 and 1 <= columna <= 4 and 1 <= valor <= 4):
                    print("Los números deben estar entre 1 y 4")
                    continue

                # Ajustar índices
                fila -= 1
                columna -= 1

                if tablero[fila][columna] != 0:
                    print("¡Esta casilla ya está ocupada!")
                    continue

                if valor == solucion[fila][columna]:
                    tablero[fila][columna] = valor
                    generador.tablero = tablero

                    if all(all(cell != 0 for cell in row) for row in tablero):
                        print("\n¡Felicitaciones! ¡Has completado el Sudoku!")
                        generador.imprimir_tablero()

                        # Preguntar si quiere jugar otro Sudoku
                        while True:
                            respuesta = input("\n¿Desea jugar otro Sudoku? (s/n): ").lower()
                            if respuesta in ['s', 'n']:
                                break
                            print("Por favor, responda 's' para sí o 'n' para no")

                        if respuesta == 'n':
                            return  # Salir al menú principal
                        else:
                            break  # Romper el bucle interno para comenzar un nuevo juego

                else:
                    print("¡Valor incorrecto! Intenta de nuevo.")

            except ValueError:
                print("Entrada inválida. Use el formato: fila columna valor")
            except IndexError:
                print("Posición inválida. Los números deben estar entre 1 y 4")