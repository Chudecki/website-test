from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/submit", methods=["POST"])
def handle_form():
    if not request.data:
        return "", 204
    data = request.get_json(force=True)
    return jsonify({ "message": "You clicked yes!" })

if __name__ == "__main__":
    app.run(debug=True)