"""Module to create and manage dspt7 mongodb database"""
import os
import json
import pprint

import pymongo
import pandas as pd
from dotenv import load_dotenv


def connect_to_client():
    # allows `mongo.py` to read environment vars from `.env` file
    load_dotenv()
    MONGO_USER = os.getenv("MONGO_USER")
    MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
    MONGO_CLUSTER = os.getenv("MONGO_CLUSTER")
    uri = f"""mongodb+srv://{
        MONGO_USER}:{
            MONGO_PASSWORD}@{
                MONGO_CLUSTER}?retryWrites=true&w=majority"""
    client = pymongo.MongoClient(uri)
    return client


def create_db_if_not_exist(client):
    if "dspt7" not in client.list_database_names():
        client.drop_database("rpg_db")
        dspt7_db = client["dspt7"]
        rpg_collection = dspt7_db["rpg_db"]
        with open("rpg.json", "r") as f:
            file_data = json.load(f)
        rpg_collection.insert_many(file_data)


# def create_dataframe(query)
def main():
    client = connect_to_client()
    create_db_if_not_exist(client)
    db = client.dspt7
    my_col = db.rpg_db
    query = my_col.find({})
    df = pd.DataFrame(query)
    print(df["fields"])

if __name__ == "__main__":
    main()
    