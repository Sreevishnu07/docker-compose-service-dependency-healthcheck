from flask import Flask
from flask_cors import CORS
import mysql.connector
import os
import time

app = Flask(__name__)
CORS(app)

def connect():
    while True:
        try:
            conn = mysql.connector.connect(
                host=os.getenv("DB_HOST"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                database=os.getenv("DB_NAME")
            )
            print("Connected to DB")
            return conn
        except:
            print("Waiting for DB...")
            time.sleep(2)

conn = connect()

@app.route("/")
def home():
    return "Backend is running and DB connected!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
