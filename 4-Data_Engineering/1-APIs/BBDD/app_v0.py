from flask import Flask, jsonify, request
from datos_dummy import books

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>My first API</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

# 1.Ruta para obtener todos los libros
@app.route('/v0/books', methods=['GET'])
def all_books():
    return jsonify(books)
    
# 2.Ruta para obtener un libro concreto mediante su id como parámetro en la llamada
@app.route('/v0/book_id', methods=['GET'])
def book_id():
    if 'id' in request.args:
        id = int(request.args['id'])
        results = [book for book in books if book['id']==id]
        return jsonify(results[0])
    else:
        return "Id not found in the request"



# 3.Ruta para obtener un libro concreto mediante su título como parámetro en la llamada de otra forma
@app.route('/v0/book/<string:title>', methods=["GET"])
def book_title(title):
    results = [book for book in books if book['title'].lower()==title.lower()]
    if results == []:
        return "Book title not found"
    else:
        return jsonify(results[0])


# 4.Ruta para obtener un libro concreto mediante su titulo dentro del cuerpo de la llamada  
@app.route('/v1/book', methods=["GET"])
def book_title_body():
    title = request.get_json()['title']
    print(title)
    results = [book for book in books if book['title'].lower()==title.lower()]
    if results == []:
        return "Book title not found"
    else:
        return jsonify(results[0])
    

# 5.Ruta para añadir un libro mediante un json en la llamada
@app.route('/v1/add_book', methods=['POST'])
def post_books():
    data = request.get_json()
    books.append(data)
    return jsonify(books)


# 6.Ruta para añadir un libro mediante parámetros
@app.route('/v2/add_book', methods=['POST'])
def post_book_v2():
    data = {}
    data['id'] = request.args['id']
    data['title'] = request.args['title']
    data['author'] = request.args['author']
    data['first_sentence'] = request.args['first_sentence']
    data['published'] = request.args['published']
    books.append(data)
    return jsonify(books)
 

# 7.Ruta para modificar un libro
@app.route('/v3/book', methods=['PUT'])
def put_book():
    published = request.args['published']
    title = request.args['title']
    for book in books:
        if book['title'] == title:
            book['published'] = published
    return jsonify(books)


# 8.Ruta para eliminar un libro
@app.route('/v4/book', methods=['DELETE'])
def delete_book():
    id = int(request.args['id'])
    for book in books:
        if book['id'] == id:
            books.remove(book)
    return jsonify(books)

app.run()