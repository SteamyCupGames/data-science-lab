import os
import pandas as pd
from pymongo import MongoClient

client = MongoClient("mongodb+srv://<user>:<password>@datalab.i76dg.mongodb.net/?retryWrites=true&w=majority&appName=DataLab")
db = client["DataLab"]

def save_to_mongo(df, images_folder="Data Analysis/Charts"):
    collection_data = db["CleanData"]
    data_dict = df.to_dict(orient="records")
    collection_data.insert_many(data_dict)
    print("✅ Clean Data has been uploaded to MongoDB successfully.")

    collection_images = db["Visualizations"]

    if not os.path.exists(images_folder):
        print(f"⚠️ Folder '{images_folder}' does not exist. No images were uploaded.")
        return

    for image_name in os.listdir(images_folder):
        image_path = os.path.join(images_folder, image_name)
        if os.path.isfile(image_path):
            with open(image_path, "rb") as image_file:
                image_data = image_file.read()
                collection_images.insert_one({"filename": image_name, "image": image_data})
    print("✅ Charts uploaded to MongoDB successfully.")
