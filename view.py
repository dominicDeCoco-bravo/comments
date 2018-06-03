from app import app
from flask import render_template
import sqlite3
from flask import request
from flask import redirect
from flask import url_for

@app.route("/")
def index():
    conn = sqlite3.connect("comm.db")
    cursor = conn.cursor()
    cursor.execute("create table if not exists comments(id integer primary key asc, comment text)")
    cursor.execute("SELECT * FROM comments")
    comments = cursor.fetchall()
    return render_template('index.html', comments=comments)
@app.route("/add", methods=['POST'])
def add_comm():
    text=request.form['text']
    conn = sqlite3.connect("comm.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO comments(comment) VALUES(?)",[text])
    conn.commit()
    return redirect(url_for('index'))
@app.route("/delete/<int:id>", methods=['DELETE'])
def delete_comm(id):
    conn = sqlite3.connect("comm.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM comments WHERE id =?",[id])
    conn.commit()
    return redirect(url_for('index'))
