import pandas as pd
import requests
from bs4 import BeautifulSoup
import os

def get_html(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f'Error accesing site: {response.status_code}')
        return None
    
    return response.content

def extract_product_data(soup, product_class, name_class, price_class, offer_price_class, bold_price_class, brand_class):
    products = soup.find_all('a', class_=product_class)

    if not products:
        print("No products were found")
        return []

    product_data = []

    for product in products:
        try:
            name_element = product.find('p', class_=name_class)
            name = name_element.text.strip() if name_element else "Unknown"

            brand_element = product.find('p', class_=brand_class)
            brand = brand_element.text.strip() if brand_element else "Unknown Brand"

            price_element = (product.find('span', class_=offer_price_class) or
                             product.find('span', class_=price_class) or
                             product.find('span', class_=bold_price_class))
            
            if price_element:
                price_text = price_element.text.strip()
                price = float(price_text.replace('₡', '').replace(',', ''))
            else:
                price = 0.0  

            product_data.append({
                'product': name,
                'price': price,
                'brand': brand
            })
        except Exception as e:
            print(f"Error: {e}")

    return product_data

def save_raw_data(product_data, file_name='UnimartCellphoneData.csv'):
    if not product_data:
        print("Could not extract products")
        return

    df = pd.DataFrame(product_data)
    raw_data_path = os.path.join("data", "raw")
    os.makedirs(raw_data_path, exist_ok=True)
    file_path = os.path.join(raw_data_path, file_name)
    df.to_csv(file_path, index=False)
    
    print(f"Data stored: {file_path}")

def main(url, product_class, name_class, price_class, offer_price_class, bold_price_class, brand_class, output_file='UnimartCellphoneData.csv'):
    html_content = get_html(url)
    if html_content is None:
        return

    soup = BeautifulSoup(html_content, 'html.parser')

    product_data = extract_product_data(soup, product_class, name_class, price_class, offer_price_class, bold_price_class, brand_class)
    save_raw_data(product_data, output_file)

if __name__ == '__main__':
    url = 'https://www.unimart.com/collections/celulares'  # URL website
    product_class = 'product-item' # Product class
    name_class = 'font-normal text-body leading-5 mb-1 order-4' # Name Class
    price_class = 'money line-through text-unimart-gray-200 text-xs'  # Regular Price 
    offer_price_class = 'money text-base font-semibold mr-2 text-accent-red'  # Offer Price
    bold_price_class = 'money text-black text-base font-semibold'  # Bold Price (No Offer)
    brand_class = 'font-normal text-[10px] uppercase text-unimart-gray-200 mb-1 order-3' # Brand Class

    main(url, product_class, name_class, price_class, offer_price_class, bold_price_class, brand_class, 'UnimartCellphoneData.csv')
