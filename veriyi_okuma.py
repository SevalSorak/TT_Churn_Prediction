import pandas as pd
import glob

# JSONL dosyalarının bulunduğu klasör
path = "capstone"  # Dosyaların bulunduğu klasör yolunu buraya yaz

# Tüm capstone JSONL dosyalarını listele
jsonl_files = sorted(glob.glob(f"{path}/capstone.*.jsonl"))

# Tüm dosyaları okuyup birleştir
df_list = [pd.read_json(file, lines=True) for file in jsonl_files]
df = pd.concat(df_list, ignore_index=True)

df.to_pickle("capstone_data.pkl")