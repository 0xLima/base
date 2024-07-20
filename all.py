import os
import json

# Direktori tempat file JSON disimpan
directory = 'metadata'

# List untuk menyimpan data dari semua file JSON
all_data = []

# Loop melalui setiap file dalam direktori
for filename in os.listdir(directory):
    if filename.endswith('.json'):
        file_path = os.path.join(directory, filename)
        
        # Baca file JSON
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            all_data.append(data)

# Gabungkan semua data menjadi satu file JSON
output_file_path = 'metadata.json'
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    json.dump(all_data, output_file, ensure_ascii=False, indent=4)

print(f"Semua file JSON berhasil digabungkan menjadi {output_file_path}")