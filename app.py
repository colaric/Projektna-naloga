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