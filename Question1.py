from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/api/<string:category>", methods=["GET"])
def get_entries_by_category(category):
    response = requests.get("https://api.publicapis.org/entries")
    api_entries = response.json()["entries"]

    filtered_entries = [entry for entry in api_entries if entry["Category"] == category]
    title_description_list = [{"title": entry["API"], "description": entry["Description"]} for entry in filtered_entries]

    return jsonify({"titleDescriptionList": title_description_list})

if __name__ == "__main__":
    app.run(debug=True)
