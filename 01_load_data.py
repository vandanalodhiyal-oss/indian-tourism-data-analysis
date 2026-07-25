import pandas as pd
import os

# Folder path
folder_path = "archive"

# All csv files list
csv_files = [file for file in os.listdir(folder_path) if file.endswith(".csv")]

print("Total CSV Files:", len(csv_files))
print()

# Dictionary---
datasets = {}

for file in csv_files:
    file_path = os.path.join(folder_path, file)

    df = pd.read_csv(file_path)

    datasets[file] = df

    print("=" * 60)
    print("File Name :", file)
    print("Rows      :", df.shape[0])
    print("Columns   :", df.shape[1])
    print(df.head())
    print()

    