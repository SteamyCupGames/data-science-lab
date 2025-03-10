import os
import pandas as pd
import re

def clean_product_name(name):
    name = re.sub(r'\+.*', '', name).strip() 
    name = name.replace('Teléfono Celular', '').strip()
    name = re.sub(r',.*', '', name).strip()
    return name

def extract_memory(name):
    match = re.search(r'(\d+GB|\d+TB)', name)
    return match.group(0) if match else 'Unknown'

def clean_dataset(input_file='data/raw/UnimartCellphoneData.csv', output_file='data/clean/UnimartCellphoneData.csv'):
    df = pd.read_csv(input_file)
    df['memory'] = df['product'].apply(extract_memory)
    df['product'] = df['product'].apply(clean_product_name)
    df.dropna(inplace=True)
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    df.to_csv(output_file, index=False)
    print(f"Clean Dataset stored: {output_file}")

if __name__ == "__main__":
    clean_dataset()
