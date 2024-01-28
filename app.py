from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# Przykładowa klasa reprezentująca model danych dla filmów
class Movie:
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre

# Przykładowe dane filmów (możesz je wczytać z pliku w rzeczywistości)
movies_data = [
    {"title": "Movie1", "year": 2020, "genre": "Action"},
    {"title": "Movie2", "year": 2021, "genre": "Comedy"},
    # ... więcej filmów
]

# Klasa obsługująca endpoint /test
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

# Klasa obsługująca endpoint /movies
class Movies(Resource):
    def get(self):
        movies = [Movie(**data).__dict__ for data in movies_data]
        return movies

# Klasa obsługująca endpoint /links
class Links(Resource):
    def get(self):
        return {'links': 'placeholder'}

# Klasa obsługująca endpoint /ratings
class Ratings(Resource):
    def get(self):
        return {'ratings': 'placeholder'}

# Klasa obsługująca endpoint /tags
class Tags(Resource):
    def get(self):
        return {'tags': 'placeholder'}

api.add_resource(HelloWorld, '/')
api.add_resource(Movies, '/movies')
api.add_resource(Links, '/links')
api.add_resource(Ratings, '/ratings')
api.add_resource(Tags, '/tags')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
