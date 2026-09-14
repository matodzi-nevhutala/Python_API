import sqlite3
from flask import Flask, render_template_string, request, redirect, url_for, jsonify

app = Flask(__name__)
DB_NAME = "vault.db"

# 1. Database Initialization
def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                priority TEXT DEFAULT 'Medium'
            )
        """)
        conn.commit()

init_db()

# 2. HTML Dashboard Template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>PERSISTENT VAULT</title>
    <style>
        body { font-family: Arial, sans-serif; background: #121212; color: #e0e0e0; margin: 0; padding: 30px; }
        .container { max-width: 800px; margin: auto; }
        h1 { color: #00bcd4; border-bottom: 2px solid #00bcd4; padding-bottom: 10px; }
        form { background: #1e1e1e; padding: 20px; border-radius: 8px; margin-bottom: 30px; }
        input, textarea, select, button { width: 100%; padding: 10px; margin-top: 10px; border-radius: 4px; border: 1px solid #333; box-sizing: border-box; }
        input, textarea, select { background: #2a2a2a; color: #fff; }
        button { background: #00bcd4; color: #121212; font-weight: bold; cursor: pointer; border: none; }
        button:hover { background: #008c9e; }
        .card { background: #1e1e1e; border-left: 5px solid #00bcd4; padding: 15px; margin-bottom: 15px; border-radius: 4px; position: relative; }
        .card.High { border-left-color: #ff5252; }
        .card.Low { border-left-color: #4caf50; }
        .delete-btn { position: absolute; right: 15px; top: 15px; background: #ff5252; color: #fff; border: none; padding: 5px 10px; width: auto; }
    </style>
</head>
<body>
    <div class="container">
        <h1> PERSISTENT DATA VAULT</h1>
        
        <form action="/add" method="POST">
            <h3>Add New Record</h3>
            <input type="text" name="title" placeholder="Title" required>
            <textarea name="content" placeholder="Content details..." rows="3" required></textarea>
            <select name="priority">
                <option value="Low">Low Priority</option>
                <option value="Medium" selected>Medium Priority</option>
                <option value="High">High Priority</option>
            </select>
            <button type="submit">Save to Database</button>
        </form>

        <h2>Stored Notes (SQL Records)</h2>
        {% for note in notes %}
        <div class="card {{ note[3] }}">
            <h3>{{ note[1] }} <small>({{ note[3] }})</small></h3>
            <p>{{ note[2] }}</p>
            <form action="/delete/{{ note[0] }}" method="POST" style="background:none; padding:0; margin:0;">
                <button type="submit" class="delete-btn">Delete</button>
            </form>
        </div>
        {% else %}
        <p>No records found in database.</p>
        {% endfor %}
    </div>
</body>
</html>
"""

# 3. Web Routes (CRUD Operations)

@app.route("/")
def index():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, content, priority FROM notes ORDER BY id DESC")
        notes = cursor.fetchall()
    return render_template_string(HTML_TEMPLATE, notes=notes)

@app.route("/add", methods=["POST"])
def add_note():
    title = request.form.get("title")
    content = request.form.get("content")
    priority = request.form.get("priority")

    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO notes (title, content, priority) VALUES (?, ?, ?)", (title, content, priority))
        conn.commit()
    return redirect(url_for("index"))

@app.route("/delete/<int:note_id>", methods=["POST"])
def delete_note(note_id):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
        conn.commit()
    return redirect(url_for("index"))

# 4. REST API Endpoint
@app.route("/api/notes", methods=["GET"])
def api_get_notes():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, content, priority FROM notes")
        notes = cursor.fetchall()
    
    formatted_notes = [{"id": n[0], "title": n[1], "content": n[2], "priority": n[3]} for n in notes]
    return jsonify({"count": len(formatted_notes), "data": formatted_notes})

if __name__ == "__main__":
    app.run(debug=True)