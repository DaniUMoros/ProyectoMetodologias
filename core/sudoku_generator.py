import random
import copy

class SudokuGenerator:
    def __init__(self, vacios=6, tipo_representacion="numeros", dificultad="Fácil"):
        self.size = 4  # Tamaño fijo de 4x4
        self.vacios = vacios
        self.box_size = 2  # Para 4x4, las cajas son de 2x2
        self.tablero = [[0 for _ in range(4)] for _ in range(4)]
        self.tipo_representacion = tipo_representacion
        self.dificultad = dificultad

        self.representaciones = {
            "numeros": {i: str(i) for i in range(1, 5)},
            "letras": {i: chr(64 + i) for i in range(1, 5)},
            "simbolos": {1: "★", 2: "♦", 3: "♣", 4: "♠"}
        }

    def convertir_valor(self, valor):
        if valor == 0:
            return " "
        return self.representaciones[self.tipo_representacion][valor]

    def es_valido(self, num, pos):
        # Verificar fila
        for x in range(4):
            if self.tablero[pos[0]][x] == num and pos[1] != x:
                return False

        # Verificar columna
        for x in range(4):
            if self.tablero[x][pos[1]] == num and pos[0] != x:
                return False

        # Verificar caja 2x2
        box_x = pos[1] // 2
        box_y = pos[0] // 2
        for i in range(box_y * 2, box_y * 2 + 2):
            for j in range(box_x * 2, box_x * 2 + 2):
                if self.tablero[i][j] == num and (i, j) != pos:
                    return False

        return True

    def encontrar_vacio(self):
        for i in range(4):
            for j in range(4):
                if self.tablero[i][j] == 0:
                    return (i, j)
        return None

    def resolver(self):
        vacio = self.encontrar_vacio()
        if not vacio:
            return True

        fila, col = vacio
        for num in range(1, 5):
            if self.es_valido(num, (fila, col)):
                self.tablero[fila][col] = num
                if self.resolver():
                    return True
                self.tablero[fila][col] = 0

        return False

    def generar_sudoku(self):
        self.resolver()
        solucion = copy.deepcopy(self.tablero)

        posiciones = [(i, j) for i in range(4) for j in range(4)]
        random.shuffle(posiciones)
        for _ in range(self.vacios):
            if posiciones:
                pos = posiciones.pop()
                self.tablero[pos[0]][pos[1]] = 0

        return self.tablero, solucion

    def imprimir_tablero(self):
        borde = "***" if self.dificultad == "Fácil" else "---"
        print(borde * 5)  # Borde superior

        for i in range(4):
            if i % 2 == 0 and i != 0:
                print(borde * 5)  # Separador horizontal

            print(borde[0], end=" ")  # Borde izquierdo
            for j in range(4):
                if j % 2 == 0 and j != 0:
                    print("|", end=" ")
                valor = self.convertir_valor(self.tablero[i][j])
                print(valor, end=" ")
            print(borde[0])  # Borde derecho

        print(borde * 5)  # Borde inferior

def crear_nuevo_juego(dificultad="Fácil", tipo_representacion="numeros"):
    vacios = {
        "Fácil": 6,
        "Difícil": 10
    }

    generador = SudokuGenerator(
        vacios=vacios[dificultad],
        tipo_representacion=tipo_representacion,
        dificultad=dificultad
    )
    return generador.generar_sudoku()

def mostrar_menu_representacion():
    print("\nSeleccione el tipo de representación:")
    print("1. Números (1-4)")
    print("2. Letras (A-D)")
    print("3. Símbolos (★, ♦, ♣, ♠)")

    opcion = input("Ingrese su opción (1-3): ")
    tipos = {
        "1": "numeros",
        "2": "letras",
        "3": "simbolos"
    }
    return tipos.get(opcion, "numeros")

if __name__ == "__main__":
    print("=== NUEVO JUEGO DE SUDOKU 4x4 ===")
    print("\nSeleccione la dificultad:")
    print("1. Fácil (6 casillas vacías)")
    print("2. Difícil (10 casillas vacías)")

    dif = input("Ingrese su opción (1-2): ")
    dificultad = "Fácil" if dif == "1" else "Difícil"

    tipo_representacion = mostrar_menu_representacion()
    tablero, solucion = crear_nuevo_juego(dificultad, tipo_representacion)

    print(f"\nTablero del juego ({dificultad}):")
    generador = SudokuGenerator(
        tipo_representacion=tipo_representacion,
        dificultad=dificultad
    )
    generador.tablero = tablero
    generador.imprimir_tablero()