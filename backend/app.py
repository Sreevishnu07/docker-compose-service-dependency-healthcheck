from flask import Flask
from flask_cors import CORS
import mysql.connector
import os
import time

app = Flask(__name__)
CORS(app)

def connect(max_retries=10):
    retries = 0
    while retries < max_retries:
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
            retries += 1

    raise Exception("Database connection failed")

@app.route("/")
def home():
    return "Backend is running and DB connected!"

if __name__ == "__main__":
    conn = connect()
    app.run(host="0.0.0.0", port=5000)
