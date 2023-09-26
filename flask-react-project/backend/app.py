from flask import Flask, jsonify

app = Flask(__name__)

books = [
    {
        'id': 1,
        'title': 'Book 1',
        'author': 'Author 1',
        'description': 'Description for Book 1'
    },
    {
        'id': 2,
        'title': 'Book 2',
        'author': 'Author 2',
        'description': 'Description for Book 2'
    },
    {
        'id': 3,
        'title': 'Book 3',
        'author': 'Author 3',
        'description': 'Description for Book 3'
    },
    {
        'id': 4,
        'title': 'Book 4',
        'author': 'Author 4',
        'description': 'Description for Book 4'
    },
    {
        'id': 5,
        'title': 'Book 5',
        'author': 'Author 5',
        'description': 'Description for Book 5'
    },
    {
        'id': 6,
        'title': 'Book 6',
        'author': 'Author 6',
        'description': 'Description for Book 6'
    },
    {
        'id': 7,
        'title': 'Book 7',
        'author': 'Author 7',
        'description': 'Description for Book 7'
    },
    {
        'id': 8,
        'title': 'Book 8',
        'author': 'Author 8',
        'description': 'Description for Book 8'
    },
    {
        'id': 9,
        'title': 'Book 9',
        'author': 'Author 9',
        'description': 'Description for Book 9'
    },
    {
        'id': 10,
        'title': 'Book 10',
        'author': 'Author 10',
        'description': 'Description for Book 10'
    }
]

@app.route('/api/books', methods=['GET'])
def get_books():
    return jsonify(books)

if __name__ == '__main__':
    app.run(debug=True)
