import json
import os

# Ruta al archivo de scores
SCORES_PATH = os.path.join(os.path.dirname(__file__), 'scores.json')

def cargar_scores():
    """
    Lee y devuelve la lista de records desde scores.json.
    Si no existe el archivo, devuelve lista vacía.
    Cada record es un dict con los campos:
      - nombre
      - puntaje_por_sudoku (lista de ints)
      - puntos_bonificacion (lista de ints)
      - tableros_completados (int)
    """
    if not os.path.isfile(SCORES_PATH):
        return []
    with open(SCORES_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def guardar_scores(records):
    """
    Sobrescribe scores.json con la lista de records.
    """
    with open(SCORES_PATH, 'w', encoding='utf-8') as f:
        json.dump(records, f, ensure_ascii=False, indent=2)
