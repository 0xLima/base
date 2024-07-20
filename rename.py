import os

def rename_files(directory):
    # Dapatkan daftar semua file json dalam folder
    files = [f for f in os.listdir(directory) if f.endswith('.json')]
    
    # Urutkan file berdasarkan nomor dalam nama file
    files.sort(key=lambda f: int(f.split('.')[0]))
    
    # Ganti nama file satu per satu
    for old_name in files:
        # Dapatkan nomor lama dari nama file
        old_number = int(old_name.split('.')[0])
        # Hitung nomor baru
        new_number = old_number - 1
        # Buat nama file baru
        new_name = f"{new_number}.json"
        # Dapatkan path lengkap untuk file lama dan baru
        old_path = os.path.join(directory, old_name)
        new_path = os.path.join(directory, new_name)
        # Ganti nama file
        os.rename(old_path, new_path)
        print(f"Renamed {old_name} to {new_name}")

# Ubah ini ke path folder 'metadata' Anda
directory = 'metadata'
rename_files(directory)
