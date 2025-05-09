def obtener_opcion_valida(min_valor, max_valor):
    while True:
        try:
            opcion = input(f"\nSeleccione una opción ({min_valor}-{max_valor}): ").strip()
            opcion = int(opcion)
            if min_valor <= opcion <= max_valor:
                return opcion
            else:
                print(f"Error: Por favor, ingrese un número entre {min_valor} y {max_valor}.")
        except ValueError:
            print(f"Error: Por favor, ingrese un número válido.")
        except KeyboardInterrupt:
            return max_valor  # Retorna la opción de salir