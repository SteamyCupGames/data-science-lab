# 🧪 Big Data Pipeline: Web Scraping, Cleansing and Storing in MongoDB

This repository implements a complete data pipeline to extract information from an online marketplace, clean and store it in MongoDB, and explore it through visualizations. It demonstrates real-world data engineering and data science practices using Python.

## 📋 Project Description

The project scrapes product data from Unimart (Costa Rica), processes and stores it, and visualizes key business insights. It includes Jupyter notebooks and modular scripts for reproducibility and scalability.

## 🎯 Business Objective

To support data-driven decisions by building an automated data pipeline that enables pricing analysis, product tracking, and market insights from real-time scraped data.

## 🛠 Technologies and Tools Used

- 🐍 Python 3.x  
- 🌐 Requests, BeautifulSoup – Web scraping  
- 🐼 Pandas – Data wrangling  
- 🍃 MongoDB – Data storage  
- 📓 Jupyter Notebooks – Analysis and storytelling  
- 📊 Matplotlib – Visualizations  
- 🐳 Docker – Reproducible environment  

## 📂 Project Structure

```
📂 Data
 ┣ 📂 raw          # Raw scraped data
    ┗ 📜 UnimartCellphoneData.csv
 ┗ 📂 clean        # Cleaned and processed data
    ┗ 📜 UnimartCellphoneData.csv
📂 Data Analysis
┗ 📂 Charts
   ┣ 📜 avg_cost_by_brand.png
   ┣ 📜 top_10_most_expensive_phones.png
   ┣ 📜 average_price_per_memory_amount.png
   ┗ 📜 price_distribution_by_brand.png
📂 Notebooks
 ┗ pipeline_demo.ipynb  # Full pipeline walkthrough
📂 Source
 ┗ scraper.py              # Web scraping   
 ┗ plot_creatoy.py         # Generates visualizations
 ┗ clean_data.py           # Cleaning and preprocessing
 ┗ mongobd_connection.py   # Uploads data/images to MongoDB
📜 README.md
```

## Installation
### Prerequisites
- Python 3.8+
- MongoDB (local or cloud)
- (Optional) Docker

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/data-science-lab.git
   cd data-science-lab
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your MongoDB connection in `upload_to_mongo.py` by replacing `<your_connection_string>` with your actual connection string.
   ```bash
   client = pymongo.MongoClient("<your_connection_string>")
   ```

## Usage
1. **Run the web scraping script**:
   ```bash
   python scraping/scrape_data.py
   ```
2. **Clean the data**:
   ```bash
   python data_processing/clean_data.py
   ```
3. **Generate visualizations**:
   ```bash
   python visualizations/generate_charts.py
   ```
4. **Upload to MongoDB**:
   ```bash
   python mongodb/upload_to_mongo.py
   ```

## 📊 Visualizations
The project includes visualizations such as:

📈 Average Cost by Brand
💸 Top 10 Most Expensive Phones
📊 Price Distribution by Brand
🧠 Price vs Memory Analysis

All charts are saved automatically and can be uploaded to MongoDB.

## 📄 License
This project is open-source and available under the MIT License.