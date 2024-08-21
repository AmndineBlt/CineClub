import os
import json
import logging

CUR_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(CUR_DIR, "data", "movies.json")

def get_movies():
    movies_instances = []
    with open(DATA_FILE, "r") as f:
        movies = json.load(f)
        for movie_title in movies:
            movies_instances.append(Movie(movie_title))

        return movies_instances

class Movie:
    #Initialisation : Avoir le bon format de titre
    def __init__(self, title):
        self.title = title.title()

    def __str__(self):
        return self.title
    
    #Ouvrire le fichier json
    def _get_movies(self):
        with open(DATA_FILE, "r") as f:
            return json.load(f)

    #Ecrire dans le fichier json
    def _write_movies(self, movies):
        with open(DATA_FILE, "w") as f:
            json.dump(movies, f, indent=4)

    #Ajouter un film
    def add_to_movies(self):
        #Récupérer la liste des films
        movies = self._get_movies()
        #Vérifier que le film n'est pas déjà dans la liste
        #Si ce n'est pas le cas on l'ajoute
        #Si c'est le cas, on affiche un message pour indiquer que le filme est déjà dans la liste (avec le module logging)
        if self.title not in movies:
            movies.append(self.title)
            self._write_movies(movies)
            return True
        else:
            logging.warning(f"La film {self.title} est déjà enregistré.")
            return False

    #Supprimer un film
    def remove_to_movies(self):
        #Récupérer la liste des films
        movies = self._get_movies()
        #Vérifier si le film est dans la liste
        #Si c'est le cas, on l'enlever et écrire la nouvelle liste de films dans le fichier json
        if self.title in movies:
            movies.remove(self.title)
            self._write_movies(movies)

if __name__ == "__main__":
    movies = get_movies()
    print(movies)