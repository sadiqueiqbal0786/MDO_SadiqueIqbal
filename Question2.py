from flask import Flask, jsonify, request
from pymongo import MongoClient
import requests

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["apis"]
entries_collection = db["entries"]

@app.route("/api/entries", methods=["POST"])
def create_entry():
    response = requests.get("https://api.publicapis.org/entries")
    api_entries = response.json()["entries"]
    entry_data = request.get_json()
    for entry in api_entries:
        if entry["API"] == entry_data["API"] and entry["Description"] == entry_data["Description"]:
            new_entry = {
                "API": entry["API"],
                "Description": entry["Description"],
                "Auth": entry["Auth"],
                "HTTPS": entry["HTTPS"],
                "Cors": entry["Cors"],
                "Link": entry["Link"],
                "Category": entry["Category"]
            }
            entries_collection.insert_one(new_entry)
            return jsonify({"message": "New entry created successfully"}), 201
    return jsonify({"message": "Error creating new entry"}), 400

if __name__ == "__main__":
    app.run(debug=True)

    
    
    #This will save a new entry in the MongoDB collection 'entries' with the properties provided in the payload.
    {
    "API": "API Name",
    "Description":"Description of the API"
}
