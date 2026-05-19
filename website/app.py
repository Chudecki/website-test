from flask import Flask, render_template, request, jsonify 
import os
import json
from datetime import datetime

def json_data_handling(data):
    folder_path = 'website/json_user_data'

    # create folder if it doesn't exist
    os.makedirs(folder_path, exist_ok=True)

    # safe timestamp for filename
    date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    name = "test_name"

    # full file path
    file_path = os.path.join(folder_path, f"{date}_{name}.json")

    # write json data
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route("/submit", methods=["POST"])
def handle_form():
    
    print("REQUEST RECEIVED")

    try:
        data = request.get_json(force=True)
        print("DATA:", data)

        if not data:
            return jsonify({"message": "No data received"}), 400

        json_data_handling(data)
        
        return jsonify({"message": "form successfully submitted"}), 200

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"message": "error"}), 500

if __name__ == "__main__":
    app.run(debug=True)
    