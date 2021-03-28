import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS
import recommendation

movies = pd.read_csv('dataset/movie_data.csv.zip')

app = Flask(__name__)
CORS(app)


@app.route('/movie/<name>')
def recommend_movies(name):
        res = recommendation.results(name)
        return jsonify(res)

@app.route("/all")
def obtener_peliculas():
    movies_list = []

    for index in movies.index:
        pelicula = {
            "id": index,
            "name": movies.original_title[index],
            "genres": movies.genres[index],
            "overview": movies.overview[index],
            "cast": movies.cast[index]
        }
        movies_list.append(pelicula)

    return jsonify(movies_list)

@app.route("/genre/<name>")
def get_genres(name):
    lista_peliculas = []

    for index in movies.index:
        pelicula = {
            "id": index,
            "original_title": movies.original_title[index],
            "genres": movies.genres[index],
            "overview": movies.overview[index],
            "cast": movies.cast[index]
        }
        if name in pelicula['genres']:
            lista_peliculas.append(pelicula)

        

    return jsonify(lista_peliculas)

if __name__ == '__main__':
        app.run(port=5001, debug= True)
