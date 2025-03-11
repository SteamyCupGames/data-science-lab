import os
import pandas as pd
from pymongo import MongoClient

# Client info has to be changed for your own MongoDB client
client = MongoClient("mongodb+srv://<user>:<password>@datalab.i76dg.mongodb.net/?retryWrites=true&w=majority&appName=DataLab")
db = client["DataLab"]
collection = db["CleanData"]

df = pd.read_csv("data/clean/UnimartCellphoneData.csv")
data_dict = df.to_dict(orient="records")
collection.insert_many(data_dict)
print("Clean Data has been uploaded to MongoDB succesfully.")

collection = db["Visualizations"]
image_folder = "Data Analysis/Charts"

for image_name in os.listdir(image_folder):
    with open(os.path.join(image_folder, image_name), "rb") as image_file:
        image_data = image_file.read()
        collection.insert_one({"filename": image_name, "image": image_data})
print("Charts uploaded to MongoDB succesfully.")