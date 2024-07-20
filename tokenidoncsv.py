import pandas as pd

# Membaca file metadata.csv
df = pd.read_csv('metadata.csv')

# Membuat kolom tokenId dengan mengekstrak angka dari kolom name
df['tokenId'] = df['name'].str.extract('(\d+)').astype(int)

# Menyimpan DataFrame kembali ke file metadata.csv
df.to_csv('metadata.csv', index=False)

# Jika ingin menyimpan ke file yang berbeda
df.to_csv('_metadata.csv', index=False)