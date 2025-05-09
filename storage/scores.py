class SistemaPuntajes:
    def __init__(self):
        self.puntaje_total = 0
        self.tableros_consecutivos = 0
        self.mejor_racha = 0
        self.tableros_completados = 0

    def calcular_bonificacion(self):
        """Calcula la bonificación basada en tableros consecutivos completados"""
        if self.tableros_consecutivos <= 1:
            return 0
        return self.tableros_consecutivos - 1

    def tablero_completado(self):
        """Registra un tablero completado exitosamente"""
        self.tableros_consecutivos += 1
        self.tableros_completados += 1

        # Actualizar mejor racha
        if self.tableros_consecutivos > self.mejor_racha:
            self.mejor_racha = self.tableros_consecutivos

        # Puntaje base por completar tablero
        puntaje_base = 10
        # Bonificación por racha
        bonificacion = self.calcular_bonificacion()

        puntaje_ganado = puntaje_base + bonificacion
        self.puntaje_total += puntaje_ganado

        return {
            'puntaje_base': puntaje_base,
            'bonificacion': bonificacion,
            'puntaje_total': puntaje_ganado,
            'racha_actual': self.tableros_consecutivos
        }

    def tablero_fallido(self):
        """Registra un fallo en el tablero actual"""
        self.tableros_consecutivos = 0

    def obtener_estadisticas(self):
        """Retorna las estadísticas actuales"""
        return {
            'puntaje_total': self.puntaje_total,
            'tableros_completados': self.tableros_completados,
            'racha_actual': self.tableros_consecutivos,
            'mejor_racha': self.mejor_racha
        }

# Variable global para mantener una instancia del sistema de puntajes
sistema_puntajes = SistemaPuntajes()

def ver_mejores_puntajes():
    """Muestra las estadísticas actuales del jugador"""
    estadisticas = sistema_puntajes.obtener_estadisticas()
    print("\n=== Estadísticas del Jugador ===")
    print(f"Puntaje Total: {estadisticas['puntaje_total']}")
    print(f"Tableros Completados: {estadisticas['tableros_completados']}")
    print(f"Racha Actual: {estadisticas['racha_actual']}")
    print(f"Mejor Racha: {estadisticas['mejor_racha']}")