import random
import copy

class SudokuGenerator:
    def __init__(self, size=9, vacios=30):
        """
        Inicializa el generador de Sudoku
        :param size: Tamaño del tablero (9 para 9x9, 6 para 6x6)
        :param vacios: Número de celdas vacías para el puzzle
        """
        self.size = size
        self.vacios = vacios
        self.box_size = 3 if size == 9 else 2  # Tamaño de cada subgrilla
        self.tablero = [[0 for _ in range(size)] for _ in range(size)]

    def es_valido(self, num, pos):
        """Verifica si un número es válido en una posición dada"""
        # Verificar fila
        for x in range(self.size):
            if self.tablero[pos[0]][x] == num and pos[1] != x:
                return False

        # Verificar columna
        for x in range(self.size):
            if self.tablero[x][pos[1]] == num and pos[0] != x:
                return False

        # Verificar subgrilla
        box_x = pos[1] // self.box_size
        box_y = pos[0] // self.box_size

        for i in range(box_y * self.box_size, box_y * self.box_size + self.box_size):
            for j in range(box_x * self.box_size, box_x * self.box_size + self.box_size):
                if self.tablero[i][j] == num and (i, j) != pos:
                    return False

        return True

    def encontrar_vacio(self):
        """Encuentra una posición vacía en el tablero"""
        for i in range(self.size):
            for j in range(self.size):
                if self.tablero[i][j] == 0:
                    return (i, j)
        return None

    def resolver(self):
        """Resuelve el tablero de Sudoku usando backtracking"""
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
        """Genera un nuevo puzzle de Sudoku"""
        # Generar solución completa
        self.resolver()

        # Hacer una copia de la solución
        solucion = copy.deepcopy(self.tablero)

        # Crear puzzle eliminando números
        posiciones = [(i, j) for i in range(self.size) for j in range(self.size)]
        for _ in range(self.vacios):
            if not posiciones:
                break
            pos = random.choice(posiciones)
            posiciones.remove(pos)
            self.tablero[pos[0]][pos[1]] = 0

        return self.tablero, solucion

    def imprimir_tablero(self):
        """Imprime el tablero de manera formateada"""
        for i in range(self.size):
            if i % self.box_size == 0 and i != 0:
                print("-" * (self.size * 3 + self.box_size + 1))

            for j in range(self.size):
                if j % self.box_size == 0 and j != 0:
                    print("|", end=" ")

                if j == self.size - 1:
                    print(self.tablero[i][j])
                else:
                    print(str(self.tablero[i][j]) + " ", end="")

def crear_nuevo_juego(size=9, dificultad="Medio"):
    """
    Crea un nuevo juego de Sudoku
    :param size: Tamaño del tablero (9 o 6)
    :param dificultad: "Fácil", "Medio" o "Difícil"
    :return: tupla (tablero_juego, solucion)
    """
    # Definir número de celdas vacías según dificultad y tamaño
    vacios = {
        9: {"Fácil": 30, "Medio": 40, "Difícil": 50},
        6: {"Fácil": 15, "Medio": 20, "Difícil": 25}
    }

    num_vacios = vacios[size][dificultad]
    generador = SudokuGenerator(size, num_vacios)
    return generador.generar_sudoku()

# Ejemplo de uso
if __name__ == "__main__":
    # Crear un nuevo juego 9x9 de dificultad media
    tablero, solucion = crear_nuevo_juego(9, "Medio")

    print("=== NUEVO JUEGO DE SUDOKU ===")
    generador = SudokuGenerator()
    generador.tablero = tablero
    print("\nTablero del juego:")
    generador.imprimir_tablero()

    print("\nSolución:")
    generador.tablero = solucion
    generador.imprimir_tablero()