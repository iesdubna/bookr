from flask import Flask
import yaml

app = Flask(__name__)

@app.route('/books')
def list():
    with open("books.yaml") as f:
        config = yaml.safe_load(f)
        list_books = ""
        list_books += "Список книг: " + '<br>'
        for book in config["books"]:
            list_books += book["filename"] + '<br>'
        return list_books


app.run()

