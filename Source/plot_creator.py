import os
import pandas as pd
import matplotlib.pyplot as plt

def plot_avg_price_per_brand(input_file='data/clean/UnimartCellphoneData.csv', output_file='Data Analysis/Charts/average_cost_by_brand.png'):
    df = pd.read_csv(input_file)
    avg_price = df.groupby('brand')['price'].mean().sort_values()
    
    plt.figure(figsize=(10, 6))
    avg_price.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title('Average Cost per Brand')
    plt.xlabel('Brand')
    plt.ylabel('Average Cost (₡)')
    plt.xticks(rotation=45)
    
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    plt.savefig(output_file)
    plt.close()
    print(f'Plot saved inside folder:  {output_file}')

def plot_top_10_most_expensive_phones(input_file='data/clean/UnimartCellphoneData.csv', output_file='Data Analysis/Charts/top_10_most_expensive_phones.png'):
    df = pd.read_csv(input_file)
    top_10 = df.nlargest(10, 'price')[['product', 'price']]
    
    plt.figure(figsize=(8, 6))
    plt.barh(top_10['product'], top_10['price'], color='red')
    plt.xlabel('Price (₡)')
    plt.ylabel('Product')
    plt.title('Top 10 Most Expensive Phones')
    plt.gca().invert_yaxis()  # Inverts y axis in order to show the most expensive phone at the top
    
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    plt.savefig(output_file)
    plt.close()
    print(f'Plot saved inside folder:  {output_file}')

def plot_price_distribution_per_brand(input_file='data/clean/UnimartCellphoneData.csv', output_file='Data Analysis/Charts/price_distribution_by_brand.png'):
    df = pd.read_csv(input_file)
    df = df.sort_values(by=['brand', 'price'])
    
    plt.figure(figsize=(12, 6))
    for brand, data in df.groupby('brand'):
        plt.bar(data['product'], data['price'], label=brand)
    
    plt.xlabel('Model')
    plt.ylabel('Price (₡)')
    plt.title('Price Distribution per brand')
    plt.xticks(rotation=90, fontsize=8)
    plt.legend(title='Brand')
    
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    plt.savefig(output_file, bbox_inches='tight')
    plt.close()
    print(f'Plot saved inside folder:  {output_file}')

def plot_avg_price_per_memory(input_file='data/clean/UnimartCellphoneData.csv', output_file='Data Analysis/Charts/average_price_per_memory_amount.png'):
    df = pd.read_csv(input_file)
    df['memory'] = df['memory'].astype(str)
    df = df[df['memory'] != 'Unknown'] # Drop Unknown memory values (Possible Issues with Data Scraping Process)
    df['memory'] = df['memory'].str.replace('GB', '').astype(int) # Drop 'GB' and convert into integer
    df = df[df['memory'] >= 64] # Drop memory values less than 64GB (Possible Issues with Data Scraping Process)
    avg_price_memory = df.groupby('memory')['price'].mean().sort_values()
    
    plt.figure(figsize=(10, 6))
    avg_price_memory.plot(kind='bar', color='purple', edgecolor='black')
    plt.title('Average Cost per Memory Amount')
    plt.xlabel('Memory Amount (GB)')
    plt.ylabel('Average Cost (₡)')
    plt.xticks(rotation=45)
    
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    plt.savefig(output_file)
    plt.close()
    print(f'Plot saved inside folder:  {output_file}')

def analyze_data(df):
    plot_avg_price_per_brand(df)
    plot_top_10_most_expensive_phones(df)
    plot_price_distribution_per_brand(df)
    plot_avg_price_per_memory(df)