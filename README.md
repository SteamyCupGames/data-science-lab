# 🧪 Big Data Pipeline: Web Scraping, Cleansing and Storing in MongoDB

This project implements a complete data science pipeline that extracts product data from an online marketplace (Unimart Costa Rica), cleans and processes it, stores it in MongoDB, and generates insightful analyses and visualizations for data-driven decision making.

## 🚀 Project Objective
Demonstrate technical skills and best practices in real-world data extraction, storage, and analysis by building a modular, reproducible solution that can support business intelligence and market analysis workflows.

## 🎯 Business Objective

To support data-driven decisions by building an automated data pipeline that enables pricing analysis, product tracking, and market insights from real-time scraped data.

## 🛠 Technologies and Tools Used

- 🐍 Language: Python 3.x 
- 🌐 Web Scraping: Requests, BeautifulSoup
- 🐼 Data Processing: Pandas
- 🍃 Storage: MongoDB (Atlas or local) 
- 📓 Environment: Jupyter Notebooks for exploratory analysis and storytelling 
- 📊 Visualization: Matplotlib 
- 🐳 Containerization: Docker for reproducible environments

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
📜 Dockerfile
📜 docker-compose.yml
📜 requirements.txt
📜 README.md
```

## Installation
### Prerequisites
- Python 3.8 or higher
- MongoDB Atlas account or local MongoDB installation
- (Optional) Docker for containerized execution

### Steps to run

1. Clone the repository and navigate into it:
   ```bash
   git clone https: https://github.com/SteamyCupGames/data-science-lab.git
   cd data-science-lab
   ```
2. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure your MongoDB connection string inside Source/mongodb_connection.py:
   ```bash
   client = pymongo.MongoClient("<your_connection_string>")
   ```
4. Run the full data pipeline with:
```bash
   python run_pipeline.py
   ```

This script will scrape data, clean it, upload it to MongoDB, and generate visualizations automatically.

## 📊 Visualizations
The project includes visualizations such as:

- 📈 Average Cost by Brand
- 💸 Top 10 Most Expensive Phones
- 📊 Price Distribution by Brand
- 🧠 Price vs Memory Analysis

All generated charts are saved under Data Analysis/Charts and also uploaded to MongoDB for easy access.

## 📄 License
This project is open-source and available under the MIT License.

Contact
Néstor Piedra — [[LinkedIn](https://www.linkedin.com/in/nestor-piedra-319b48178/) / [GitHub](https://github.com/SteamyCupGames)]

