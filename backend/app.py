from flask import Flask
from flask_cors import CORS
import mysql.connector
import os
import time

app = Flask(__name__)
CORS(app)

conn = None

def connect(max_retries=10):
    global conn
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
            return
        except Exception as e:
            print("Waiting for DB...", e)
            time.sleep(2)
            retries += 1

    raise Exception("Database connection failed")


@app.route("/api/data")
def data():
    cursor = conn.cursor()
    cursor.execute("SELECT 'Hello from MySQL' AS message")
    result = cursor.fetchall()
    return {"data": result}


if __name__ == "__main__":
    connect()
    app.run(host="0.0.0.0", port=5000)
