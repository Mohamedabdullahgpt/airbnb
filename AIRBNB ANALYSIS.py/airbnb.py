import pymongo
import pandas as pd
# Replace placeholders with your actual MongoDB Atlas credentials
username = "abdullahsma222"
password = "6383820840"

# Replace <cluster_name> with your MongoDB Atlas cluster name
cluster_name = "cluster0"

mongo_uri = f"mongodb+srv://{username}:{password}@{cluster_name}.lpdvj7r.mongodb.net/"
database_name = "sample_airbnb"
collection_name = "listingsAndReviews"

# Connect to MongoDB Atlas
client = pymongo.MongoClient(mongo_uri)
db = client[database_name]
collection = db[collection_name]

# Query documents
query = {"property_type": "Apartment"}
data = collection.find(query)

df= pd.DataFrame(data)
print(df)

