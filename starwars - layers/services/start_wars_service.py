import requests

movie_url = "https://swapi.dev/api/films/"

def fetch_movies():
    data = requests.get(movie_url).json()
    # movies = [{"id": movie["episode_id"], "name": movie["title"]} for movie in data["results"]]
    movies = []
    for movie in data["results"]:
        movies.append({
            "id": movie["episode_id"],
            "name": movie["title"]
        })

    return sorted(movies, key=lambda x: x['id'])


def fetch_characters(id):
    if id > 6 or id < 1:
        return "ERROR, ID OUT OF RANGE"

    data = requests.get(f"{movie_url}/{id}").json()
    characters_url = data["characters"]
    characters = []
    for url in characters_url:
        data = requests.get(url).json()
        characters.append(data["name"])

    return characters




