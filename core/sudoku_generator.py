import random
import copy

class SudokuGenerator:
    def __init__(self, size=4, vacios=6):
        """
        Inicializa el generador de Sudoku 4×4
        :param size: Tamaño del tablero (4 para 4x4)
        :param vacios: Número de celdas vacías para el puzzle
        """
        self.size = size
        self.vacios = vacios
        self.box_size = 2  # Subcuadrantes 2×2
        self.tablero = [[0 for _ in range(size)] for _ in range(size)]

    def es_valido(self, num, pos):
        """Verifica si un número es válido en la posición pos=(fila,col)"""
        fila, col = pos
        # Fila
        if any(self.tablero[fila][j] == num for j in range(self.size) if j != col):
            return False
        # Columna
        if any(self.tablero[i][col] == num for i in range(self.size) if i != fila):
            return False
        # Subcuadrante 2×2
        box_row = (fila // self.box_size) * self.box_size
        box_col = (col   // self.box_size) * self.box_size
        for i in range(box_row, box_row + self.box_size):
            for j in range(box_col, box_col + self.box_size):
                if (i, j) != pos and self.tablero[i][j] == num:
                    return False
        return True

    def encontrar_vacio(self):
        """Encuentra la primera casilla vacía (0), devuelve (fila, col) o None"""
        for i in range(self.size):
            for j in range(self.size):
                if self.tablero[i][j] == 0:
                    return (i, j)
        return None

    def resolver(self):
        """Resuelve el tablero completo usando backtracking"""
        vacio = self.encontrar_vacio()
        if not vacio:
            return True
        fila, col = vacio
        nums = list(range(1, self.size + 1))
        random.shuffle(nums)
        for num in nums:
            if self.es_valido(num, (fila, col)):
                self.tablero[fila][col] = num
                if self.resolver():
                    return True
                self.tablero[fila][col] = 0
        return False

    def generar_sudoku(self):
        """Genera el puzzle: devuelve (tablero_con_huecos, solucion_completa)"""
        # 1) Generar solución completa
        self.resolver()
        solucion = copy.deepcopy(self.tablero)
        # 2) Vaciar 'vacios' casillas al azar
        posiciones = [(i, j) for i in range(self.size) for j in range(self.size)]
        for _ in range(min(self.vacios, len(posiciones))):
            pos = random.choice(posiciones)
            posiciones.remove(pos)
            self.tablero[pos[0]][pos[1]] = 0
        return self.tablero, solucion

    def imprimir_tablero(self):
        """Imprime el tablero formateado (usa '.' para vacíos)"""
        # Encabezado de columnas
        print("   " + " ".join(str(j) for j in range(self.size)))
        for i, fila in enumerate(self.tablero):
            linea = " ".join(str(n) if n != 0 else "." for n in fila)
            print(f"{i}  {linea}")
        print()

def crear_nuevo_juego(vacios, delimiter):
    """
    Bucle principal de juego:
    - vacios: número de casillas vacías
    - delimiter: cadena para delimitar el tablero ('***' o '---')
    """
    gen = SudokuGenerator(size=4, vacios=vacios)
    tablero, solucion = gen.generar_sudoku()

    while True:
        # Mostrar tablero delimitado
        print(delimiter)
        gen.tablero = tablero
        gen.imprimir_tablero()
        print(delimiter)

        # Comprueba si terminó
        if all(all(celda != 0 for celda in fila) for fila in tablero):
            print("¡Felicidades! Has completado el Sudoku.\n")
            break

        entrada = input("Ingresa fila,columna (0–3) o 'q' para salir: ")
        if entrada.lower() == 'q':
            print("Juego terminado. ¡Hasta pronto!")
            return

        try:
            fila, col = map(int, entrada.split(','))
            if not (0 <= fila < 4 and 0 <= col < 4):
                print("Coordenadas fuera de rango. Usa valores entre 0 y 3.\n")
                continue
            if tablero[fila][col] != 0:
                print("Ese espacio ya está ocupado.\n")
                continue

            num = int(input("Ingresa el número (1–4): "))
            if not (1 <= num <= 4):
                print("Número inválido. Debe ser entre 1 y 4.\n")
                continue

            if gen.es_valido(num, (fila, col)):
                tablero[fila][col] = num
            else:
                print("Movimiento inválido según las reglas del Sudoku.\n")

        except ValueError:
            print("Formato incorrecto. Usa 'fila,columna', por ejemplo: 1,2\n")

    # Al completar, mostrar la solución también delimitada
    print("Solución completa:")
    print(delimiter)
    gen.tablero = solucion
    gen.imprimir_tablero()
    print(delimiter)

if __name__ == "__main__":
    print("=== SUDOKU 4×4 EN CONSOLA ===")
    # Menú de dificultad
    while True:
        print("Selecciona el nivel de dificultad:")
        print("1. Fácil   (6 casillas vacías, delimitado por ***)")
        print("2. Difícil (10 casillas vacías, delimitado por ---)")
        opcion = input("Opción (1/2): ")
        if opcion == "1":
            vacios = 6
            delimiter = "***"
            break
        elif opcion == "2":
            vacios = 10
            delimiter = "---"
            break
        else:
            print("Opción inválida. Elige 1 o 2.\n")

    crear_nuevo_juego(vacios, delimiter)
