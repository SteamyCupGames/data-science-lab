# run_pipeline.py

from Source.scraper import scrape_unimart
from Source.mongodb_connection import save_to_mongo
from Source.clean_dataset import clean_dataset
from Source.plot_creator import analyze_data

def main():
    print("🚀 Starting Data Science Pipeline...\n")

    print("🔍 1. Extracting data from Unimart...")
    products = scrape_unimart()
    print(f"✅ {len(products)} products extracted.")

    print("\n🧹 2. Cleaning dataset...")
    df_clean = clean_dataset(products)
    print(f"✅ Dataset clean with {df_clean.shape[0]} rows.")

    print("\n💾 3. Saving cleaned data to MongoDB...")
    save_to_mongo(df_clean.to_dict(orient='records'))
    print("✅ Clean data saved to MongoDB.")

    print("\n📊 4. Analyzing and visualizing data...")
    analyze_data(df_clean)
    print("✅ Analysis completed. Plots generated.")

    print("\n🎉 Pipeline finished successfully.")

if __name__ == "__main__":
    main()
