<<<<<<< HEAD
from flask import Flask, render_template,  request, jsonify
import json 
=======
from flask import Flask, render_template, request, jsonify
import json
>>>>>>> 8e7cfa147df5f2fda79925a38d68d10710524a16
import os

app = Flask(__name__)
DATA_FILE = "data.json"

<<<<<<< HEAD
#Json faila ielāde vai iniciaizēšana
def log_data():
=======
#JSON faila ielāde vai inicializēšana
def load_data():
>>>>>>> 8e7cfa147df5f2fda79925a38d68d10710524a16
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w') as f:
            json.dump([], f)
    with open(DATA_FILE, 'r') as f:
<<<<<<< HEAD
        return json.load(f) 

 #Ieraksta datus JSON
 def save_data(data)
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)          
=======
        return json.load(f)
    
#ieraksta datus JSON
def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)
>>>>>>> 8e7cfa147df5f2fda79925a38d68d10710524a16


#atver mājaslapu
@app.route("/")
def index():
    return render_template("index.html")

<<<<<<< HEAD
#API, lai iegūtu visus ierakstus 
@app.route("api/data", methods=["GET"])
=======
#API, lai iegūtu visus ierakstus
@app.route("/api/data", methods=["GET"])
>>>>>>> 8e7cfa147df5f2fda79925a38d68d10710524a16
def get_data():
    data = load_data()
    return jsonify(data)

#API, lai pievienotu datus
<<<<<<< HEAD
@app.route("api/data", methods=["POST"])
=======
@app.route("/api/data", methods=["POST"])
>>>>>>> 8e7cfa147df5f2fda79925a38d68d10710524a16
def add_data():
    request_data = request.json
    date = request_data.get("date")
    min_temp = request_data.get("min_temp")
    max_temp = request_data.get("max_temp")
    #datu validācija
    if not date or min_temp is None or max_temp is None:
<<<<<<< HEAD
        return jsonify({"error": "Visi lauki ir obligāti"}),400
    try:
        min_temp = float(min_temp)
        mmax_temp = float(max_temp)
=======
        return jsonify({"error": "Visi lauki ir obligāti!"}),400
    try:
        min_temp = float(min_temp)
        max_temp = float(max_temp)
>>>>>>> 8e7cfa147df5f2fda79925a38d68d10710524a16
    except ValueError:
        return jsonify({"error": "Temperatūrai ir jābūt skaitlim!"}),400
    
    #saglabā datus
<<<<<<< HEAD
    data = log_data()
=======
    data = load_data()
>>>>>>> 8e7cfa147df5f2fda79925a38d68d10710524a16
    data.append({"date": date, "min_temp": min_temp, "max_temp": max_temp})
    save_data(data)
    return jsonify({"message": "Dati saglabāti veiksmīgi!"}),201

<<<<<<< HEAD

__name__ == "__main__":
app.run(debug=True)

=======
>>>>>>> 8e7cfa147df5f2fda79925a38d68d10710524a16

if __name__ == "__main__":
    app.run(debug=True)