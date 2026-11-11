"""
Proyecto: Calculadora de Calorías y Nutrientes (Calorie Intake Calculator)
"""

import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "nutrition.json"

def load_nutrition_data(filepath: Path = DATA_FILE) -> dict:
    """Carga los datos de nutrición desde el archivo JSON."""
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

def nutritional_summary(input_dict: dict, nutrition_dict: dict) -> dict | str:
    """
    Calcula el total de calorías, grasas, proteínas, carbohidratos y azúcares
    para una selección de alimentos dados en gramos.
    
    :param input_dict: Diccionario {nombre_alimento: gramos}.
    :param nutrition_dict: Base de datos nutricional por 100g.
    :return: Diccionario con totales o mensaje/nombre del alimento si no existe.
    """
    data_to_return = {
        'calories': 0.0,
        'total_fat': 0.0,
        'protein': 0.0,
        'carbohydrate': 0.0,
        'sugars': 0.0
    }
    
    for food_name, grams in input_dict.items():
        if food_name not in nutrition_dict:
            return f"Alimento no encontrado en la base de datos: {food_name}"
        
        info = nutrition_dict[food_name]
        factor = grams / 100.0
        data_to_return['calories'] += round(info.get('calories', 0.0) * factor, 2)
        data_to_return['total_fat'] += round(info.get('total_fat', 0.0) * factor, 2)
        data_to_return['protein'] += round(info.get('protein', 0.0) * factor, 2)
        data_to_return['carbohydrate'] += round(info.get('carbohydrate', 0.0) * factor, 2)
        data_to_return['sugars'] += round(info.get('sugars', 0.0) * factor, 2)

    return data_to_return

if __name__ == "__main__":
    db = load_nutrition_data()
    sample_order = {"Croissants, cheese": 150, "Orange juice, raw": 250}
    summary = nutritional_summary(sample_order, db)
    print("Resumen Nutricional Calculado:")
    print(json.dumps(summary, indent=2))
    print("[OK] Calculadora de calorías ejecutada exitosamente.")
