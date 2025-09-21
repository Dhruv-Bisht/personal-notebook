# app.py
from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "your_secret_key"

def init_db():
    conn = sqlite3.connect("notes.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, content TEXT)")
    conn.commit()
    conn.close()

@app.route("/", methods=["GET", "POST"])
def home():
    if "logged_in" not in session:
        return redirect("/login")

    conn = sqlite3.connect("notes.db")
    c = conn.cursor()

    if request.method == "POST":
        note = request.form["note"]
        c.execute("INSERT INTO notes (content) VALUES (?)", (note,))
        conn.commit()

    c.execute("SELECT * FROM notes")
    notes = c.fetchall()
    conn.close()

    return render_template("index.html", notes=notes)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form["username"] == "dhruv" and request.form["password"] == "dhruv@232006":
            session["logged_in"] = True
            return redirect("/")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    return redirect("/login")

@app.route("/delete/<int:note_id>", methods=["POST"])
def delete_note(note_id):
    if "logged_in" not in session:
        return redirect("/login")

    conn = sqlite3.connect("notes.db")
    c = conn.cursor()
    c.execute("DELETE FROM notes WHERE id=?", (note_id,))
    conn.commit()
    conn.close()
    return redirect("/")


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
