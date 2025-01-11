# app/app.py
import psycopg2
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
        dbname="mydb",
        user="user",
        password="password",
        host="db",  # Use the service name from docker-compose
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT 1;")
    result = cur.fetchone()
    cur.close()
    conn.close()

    return f"Database connection test result: {result}"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

