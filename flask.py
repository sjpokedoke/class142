from flask import Flask, jsonify, request
import csv
from demographic import output
from contentbased import get_recommendations

movieslist = []
with open("movies.csv") as f:
    reader = csv.reader(f)
    data = list(reader)
    movieslist = data[1:]

likedmovies = []
dislikedmovies = []
notwatchedmovies = []

app = Flask(__name__)

@app.route("/getmovies")
def getmovies():
    return jsonify({
        "data": movieslist[0],
        "status": "success"
    })

@app.route("/likedmovies", method = ["POST"])
def likedmovies():
    movies = movieslist[0]
    movieslist = movieslist[1:]
    likedmovies.append(movies)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/dislikedmovies", method = ["POST"])
def dislikedmovies():
    movies = movieslist[0]
    movieslist = movieslist[1:]
    dislikedmovies.append(movies)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/notwatchedmovies", method = ["POST"])
def notwatchedmovies():
    movies = movieslist[0]
    movieslist = movieslist[1:]
    notwatchedmovies.append(movies)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/popularmovies")
def popularmovies():
    movie_data = []
    for movie in output:
        _data = {
            "title": movie[0],
            "poster_link": movie[1],
            "release_date": movie[2] or "N/A",
            "duration": movie[3],
            "rating": movie[4],
            "overview": movie[5]
        }
        movie_data.append(_data)
    return jsonify({
        "data": movie_data
        "status": "success"
    }), 200

@app.route("/recommendedmovies")
def recommendedmovies():
    all_recommended = []
    for likedmovie in likedmovies:
        output = get_recommendations(likedmovie[19])
        for data in output:
            all_recommended.append(data)
    import itertools
    all_recommended.sort()
    all_recommended = list(all_recommended for all_recommended, _ in itertools.groupby(all_recommended))
    movie_data = []
    for movie in get_recommendations:
        _data = {
            "title": movie[0],
            "poster_link": movie[1],
            "release_date": movie[2] or "N/A",
            "duration": movie[3],
            "rating": movie[4],
            "overview": movie[5]
        }
        movie_data.append(_data)
    return jsonify({
        "data": movie_data
        "status": "success"
    }), 200

if __name__ == "__main__":
    app.run()