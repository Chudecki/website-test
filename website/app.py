from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/submit", methods=["POST"])
def handle_form():
    print("REQUEST RECEIVED")
    if not request.data:
        return "", 204
    
    try:
        data = request.get_json(force=True)
        for key, value in data.items():
            print(f"{key}: {value}")
        return jsonify({"message": "form successfully submitted"})
    except Exception as e:
        print(f"ERROR: {e}")
        return jsonify({"message": "error"}), 500

if __name__ == "__main__":
    app.run(debug=True)