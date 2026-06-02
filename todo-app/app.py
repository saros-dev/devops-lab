from flask import Flask
import os
import psycopg2

app = Flask(__name__)

def get_db():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

@app.route("/")
def home():
    return "Flask Todo API"

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

@app.route("/add/<title>")
def add_todo(title):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO todos (title) VALUES (%s)", (title,))
    conn.commit()
    conn.close()
    return f"added: {title}"

@app.route("/todos")
def list_todos():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM todos;")
    rows = cur.fetchall()
    conn.close()
    return str(rows)

@app.route("/db")
def db_test():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT version();")
    version = cur.fetchone()
    conn.close()
    return str(version)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
