from flask import Flask, render_template, request, jsonify
import sqlite3

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
        
        name = data.get("name")
        address = data.get("address")
        birthdate = data.get("birthdate")
        telephone = data.get("telephone")
        city = data.get("city")
        state = data.get("state")
        zipcode = data.get("zipcode")
        what_job = data.get("what_job")
        what_do = data.get("what_do")
        previous = data.get("previous")
        explain_why_fired = data.get("explain_why_fired")
        
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
            
        c.execute("""INSERT INTO submissions (name, address, birthdate, telephone, city, state, zipcode, what_job, what_do, previous, explain_why_fired) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) """, (name, address, birthdate, telephone, city, state, zipcode, what_job, what_do, previous, explain_why_fired))
            
        return jsonify({"message": "form successfully submitted"})
    
    
        conn.commit()
        con.close()
        
    except Exception as e:
        print(f"ERROR: {e}")
        return jsonify({"message": "error"}), 500

if __name__ == "__main__":
    app.run(debug=True)