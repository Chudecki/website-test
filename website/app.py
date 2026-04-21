from flask import Flask, render_template, request, jsonify


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

        return jsonify({"message": "form successfully submitted"}), 200

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"message": "error"}), 500

if __name__ == "__main__":
    app.run(debug=True)