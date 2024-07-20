import json
import pandas as pd

# Fungsi untuk mengkonversi metadata JSON ke CSV dengan struktur yang rapi
def convert_json_to_csv(json_file, csv_file):
    with open(json_file, 'r') as file:
        data = json.load(file)

    metadata_list = []
    for nft in data:
        nft_metadata = {
            "name": nft.get("name"),
            "description": nft.get("description"),
            "image": nft.get("image")
        }
        for attribute in nft.get("attributes", []):
            trait_type = attribute.get("trait_type")
            value = attribute.get("value")
            nft_metadata[trait_type] = value
        
        metadata_list.append(nft_metadata)
    
    df = pd.DataFrame(metadata_list)
    df.to_csv(csv_file, index=False)

# Contoh penggunaan
json_file = 'metadata.json'
csv_file = 'metadata.csv'

convert_json_to_csv(json_file, csv_file)