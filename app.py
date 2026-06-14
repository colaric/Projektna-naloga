from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from tinydb import TinyDB, Query
import hashlib
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'tvoj-tajni-kljuc'

db = TinyDB('malicameter.json')
users = db.table('users')
meals = db.table('meals')      # NOVO: tabela za jedi
ratings = db.table('ratings')
User = Query()
Meal = Query()
Rating = Query()

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if users.search(User.username == username):
            return "Uporabnik ze obstaja"
        
        users.insert({'username': username, 'password': password})
        return redirect(url_for('login'))
    return render_template('register.html')
