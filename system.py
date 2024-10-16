import csv
from surprise import Dataset, Reader

# Cargar el conjunto de datos
file_path = 'C:/Users/marin/OneDrive/Documentos/IA2024-2025/RAIN/dataset.csv'
# Crear un archivo temporal en formato user-item-rating
temp_file_path = 'temp_ratings_file.csv'

with open(file_path, newline='', encoding='utf-8') as csvfile, open(temp_file_path, 'w', newline='', encoding='utf-8') as tempfile:
    reader = csv.DictReader(csvfile)
    writer = csv.writer(tempfile)
    
    # Escribir las filas en formato (user_id, track_id, rating)
    for row in reader:
        user_id = 'default_user'  # Asigna un ID de usuario temporal
        track_id = row['track_id']
        rating = row['popularity']  # Usamos popularidad como calificación
        
        writer.writerow([user_id, track_id, rating])

# Ahora cargar el archivo temporal usando Surprise
reader = Reader(line_format='user item rating', sep=',', rating_scale=(1, 100))
surprise_data = Dataset.load_from_file(temp_file_path, reader=reader)
