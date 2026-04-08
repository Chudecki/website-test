from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/submit", method=["POST"])
def handle_form():
    name = request.form["name"]
    return render_template("result.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)