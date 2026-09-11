# app.py
from flask import Flask, request, redirect, render_template_string
import sqlite3
import os

app = Flask(__name__)

DB_PATH = os.environ.get("DB_PATH", "data/app.db")

def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name TEXT)')
    conn.commit()
    conn.close()

@app.route("/", methods=["GET", "POST"])
def index():
    # init_db() # Inicialização movida para antes de rodar o app.
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        if request.method == 'POST':
            name = request.form.get('name')
            c.execute(f"INSERT INTO items (name) VALUES('{name}')")
            conn.commit()
            return redirect('/')

        items=c.execute('SELECT * FROM items;')
    return render_template_string("""
    <h1>Itens</h1>
    <form method="post">
        <input name="name" placeholder="Novo item">
        <button type="submit">Adicionar</button>
    </form>
    <ul>
        {% for id, name in items %}
            <li>{{ id }} - {{ name }}</li>
        {% endfor %}
    </ul>
    """, items=items)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=3000)
