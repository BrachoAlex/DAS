import os
from flask import Flask
from services import start_wars_service

from flask import jsonify

print("Application startup")
port = int(os.environ['PORT'])
print("PORT::", port)

app = Flask(__name__)


@app.route("/", methods=['GET'])
def list_movies():
    movies = start_wars_service.fetch_movies()
    return jsonify(movies)

@app.route("/<int:id>", methods = ["GET"])
def list_characters(id):
    characters = start_wars_service.fetch_characters(id)
    return jsonify(characters)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=port)
