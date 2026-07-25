import pandas as pd
import os

folder_path = "archive"

csv_files = [file for file in os.listdir(folder_path) if file.endswith(".csv")]

for file in csv_files:
    print("="*40)
    print(file)

    df = pd.read_csv(os.path.join(folder_path, file))

    print(df.head())

    print("\nShape :", df.shape)

    print("\nColumns :")
    print(df.columns)

    print("\nMissing Values :")
    print(df.isnull().sum())

    print("\nData Types :")
    print(df.dtypes)