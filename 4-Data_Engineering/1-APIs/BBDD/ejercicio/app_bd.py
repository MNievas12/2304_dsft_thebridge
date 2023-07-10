import json
from flask import Flask, request, jsonify
import sqlite3
import os

os.chdir(os.path.dirname(__file__))

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def welcome():
    return "Welcome to mi API conected to my books database"

# 0.Ruta para obtener todos los libros
# @app.route('/api/v1/resources/books/all', methods=['GET'])

# 1.Ruta para obtener el conteo de libros por autor ordenados de forma descendente
# @app.route('/api/v1/resources/booksbyauthor/', methods=['GET'])


# 2.Ruta para obtener los libros de un autor como argumento en la llamada
# @app.route('/api/v1/resources/books/author', methods=['GET'])


# 3.Ruta para obtener los libros filtrados por título, publicación y autor
# @app.route('/api/v1/resources/books/filters', methods=['GET'])


app.run()