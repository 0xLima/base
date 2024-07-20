import os
import json
from collections import OrderedDict

def update_json_files(directory):
    # Dapatkan daftar semua file json dalam folder
    files = [f for f in os.listdir(directory) if f.endswith('.json')]
    
    # Urutkan file berdasarkan nomor dalam nama file
    files.sort(key=lambda f: int(f.split('.')[0]))
    
    for file_name in files:
        file_number = int(file_name.split('.')[0])
        file_path = os.path.join(directory, file_name)
        
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        # Tugas Pertama: Ganti nilai "name"
        data["name"] = f"POLC {file_number}"
        
        # Ubah nilai "image"
        data["image"] = f"{file_number}.png"
        
        # Tugas Ketiga: Hapus bagian "properties" dan "compiler", serta "external_url"
        if "properties" in data:
            del data["properties"]
        if "compiler" in data:
            del data["compiler"]
        if "external_url" in data:
            del data["external_url"]
        
        # Tugas Kedua: Tambahkan "tokenId" di atas semua elemen lainnya
        ordered_data = OrderedDict()
        ordered_data["tokenId"] = file_number
        ordered_data["name"] = data["name"]
        ordered_data["description"] = data["description"]
        ordered_data["image"] = data["image"]
        ordered_data["attributes"] = data["attributes"]
        
        # Simpan perubahan kembali ke file JSON
        with open(file_path, 'w') as file:
            json.dump(ordered_data, file, indent=2)

# Ubah ini ke path folder 'metadata' Anda
directory = 'metadata'
update_json_files(directory)
