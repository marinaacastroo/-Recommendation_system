import csv
from surprise import Dataset, Reader, KNNBasic
from surprise.model_selection import train_test_split
from surprise import accuracy

# Leer el dataset: 
def cargar_dataset(ruta_csv):
    canciones = []
    with open(ruta_csv, 'r', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            canciones.append(fila)
    return canciones



# Función principal del sistema
def main():
    ruta_csv = 'C:/Users/marin/OneDrive/Documentos/IA2024-2025/RAIN/RAIN/-Recommendation_system/dataset.csv'  
    canciones = cargar_dataset(ruta_csv)
    

if __name__ == '__main__':
    main()
