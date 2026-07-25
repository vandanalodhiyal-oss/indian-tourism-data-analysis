import pandas as pd
import os

# Original data folder
input_folder = "archive"

# Cleaned data save 
output_folder = "cleaned_data"

# Output folder create
os.makedirs(output_folder, exist_ok=True)

# Archive folder CSV files  list
csv_files = [file for file in os.listdir(input_folder) if file.endswith(".csv")]

print("Total CSV Files :", len(csv_files))

# file clean karna
for file in csv_files:

    # File read
    df = pd.read_csv(os.path.join(input_folder, file))

    print(f"\nCleaning : {file}")

    # Duplicate rows hatana
    df = df.drop_duplicates()

    # Column names ke extra spaces hatana
    df.columns = df.columns.str.strip()

    # String values ke extra spaces hatana
    df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

    # Missing values ko Forward Fill se bharna
    df = df.ffill()

    # Cleaned file save karo
    save_path = os.path.join(output_folder, file)

    df.to_csv(save_path, index=False)

    print(f"Saved : {file}")

print("\nAll Files Cleaned Successfully")