# Data Science Laboratory

This repository contains a Data Science laboratory focused on web scraping, data storage, processing, and analysis using Python. The project follows a structured pipeline to collect, clean, analyze, and visualize data.

## Project Overview
This laboratory was created to demonstrate a complete workflow from data extraction to visualization. The main components of the project include:
- **Web Scraping**: Data extraction from an online Costa Rican marketplace. (Unimart.com)
- **Data Storage**: Storing the scraped data in MongoDB and flat files (CSV).
- **Data Processing**: Cleaning and transforming raw data using Pandas.
- **Data Analysis & Visualization**: Generating insights through statistical analysis and visualizations using Matplotlib.
- **MongoDB Integration**: Uploading cleaned data and generated visualizations to MongoDB for storage.

## Project Structure
```
📂 Data
 ┣ 📂 raw          # Raw scraped data
    ┗ 📜 UnimartCellphoneData.csv
 ┗ 📂 clean        # Cleaned and processed data
    ┗ 📜 UnimartCellphoneData.csv
📂 Scraping
 ┗ scrape_data.py  # Web scraping script
📂 Data Processing
 ┗ clean_data.py   # Data cleaning and preprocessing script
📂 Data Analysis
┗ 📂 Charts
   ┣ 📜 avg_cost_by_brand.png
   ┣ 📜 top_10_most_expensive_phones.png
   ┣ 📜 average_price_per_memory_amount.png
   ┗ 📜 price_distribution_by_brand.png
 ┗ plot_creatoy.py   # Creates the charts above located
📂 Database Backup
 ┗ upload_to_mongo.py  # Script to upload data and images to MongoDB
📜 README.md
```

## Installation
### Prerequisites
Ensure you have Python 3.8+ installed along with the required dependencies.

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

## Visualizations
The following charts were generated:
- **Average Cost by Brand**
- **Top 10 Most Expensive Phones**
- **Price Distribution by Brand**
- **Price vs Memory Analysis**

## License
This project is open-source and available under the MIT License.

