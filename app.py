from flask import Flask, jsonify, render_template, request, redirect, url_for
import json
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB Atlas 
client = MongoClient("mongodb+srv://Vanshii:Vanshika%4074281@cluster1.fn0pahf.mongodb.net/?appName=Cluster1")
db = client["flaskdb"]
collection = db["users"]


# API route
@app.route('/api')
def get_data():
    with open('data.json', 'r') as file:
        data = json.load(file)
    return jsonify(data)


# Form page
@app.route('/')
def form():
    return render_template('form.html')


# Form submission
@app.route('/submit', methods=['POST'])
def submit():
    try:
        name = request.form['name']
        email = request.form['email']

        data = {
            "name": name,
            "email": email
        }

        collection.insert_one(data)

        return redirect(url_for('success'))

    except Exception as e:
        return render_template('form.html', error=str(e))


# Success page
@app.route('/success')
def success():
    return render_template('success.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
