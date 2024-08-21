#Créer un environnement virtuel depuis le terminale : python -m venv env
#Activer l'environnelent virtuel : se déplacer dans le dossier env avec la commande cd et aller dans le dossier Scripts puis mettre la commande : source activate
#Installer des packages : pip install (nom du package)

from PySide6 import QtWidgets, QtCore
from movie import get_movies, Movie

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ciné club")
        self.setup_ui()
        self.setup_connections()
        self.populate_movies()

    def setup_ui(self):
        self.main_layout = QtWidgets.QVBoxLayout(self)

        self.lineEdit_movieTitle = QtWidgets.QLineEdit()
        self.btn_addMovie = QtWidgets.QPushButton("Ajouter un film")
        self.listWidgt_movies = QtWidgets.QListWidget()
        #Permet de sélectionner plusiquers lines d'un seul coup
        self.listWidgt_movies.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection)
        self.btn_removeMovies = QtWidgets.QPushButton("Supprimer le(s) film(s)")

        self.main_layout.addWidget(self.lineEdit_movieTitle)
        self.main_layout.addWidget(self.btn_addMovie)
        self.main_layout.addWidget(self.listWidgt_movies)
        self.main_layout.addWidget( self.btn_removeMovies)

    def setup_connections(self):
        self.btn_addMovie.clicked.connect(self.add_movie)
        self.btn_removeMovies.clicked.connect(self.remove_movie)
        self.lineEdit_movieTitle.returnPressed.connect(self.add_movie)

    def populate_movies(self):
        self.listWidgt_movies.clear()
        movies = get_movies()

        for movie in movies:
            lw_item = QtWidgets.QListWidgetItem(movie.title)
            lw_item.film = movie
            #lw_item.setData(QtCore.Qt.UserRole, movie)
            self.listWidgt_movies.addItem(lw_item)

    def add_movie(self):
        #Récupérer le texte dans le line edit
        movie_title = self.lineEdit_movieTitle.text()
        #Vérifier que le line edit contient bien du texte (on ne veut pas ajouter une chaine de cara vide)
        if not movie_title:
            return False
        #Créer une isntance 'Movie'
        movie = Movie(title=movie_title)
        #Ajouter le film dans le ficher json
        resultat = movie.add_to_movies()
        #Ajouter le titre dans le list widget
        if resultat:
            lw_item = QtWidgets.QListWidgetItem(movie.title)
            lw_item.film = movie
            #lw_item.setData(QtCore.Qt.UserRole, movie)
            self.listWidgt_movies.addItem(lw_item)
        
        self.lineEdit_movieTitle.setText("")

    def remove_movie(self):
        #On boucle sur les éléments séléctionnés. On récupére les elements selectionner avec selectedItems()
        for selected_item in self.listWidgt_movies.selectedItems():
            movie = selected_item.film
            #movie = selected_item.data(QtCore.Qt.UserRole)
            movie.remove_to_movies()
            self.listWidgt_movies.takeItem(self.listWidgt_movies.row(selected_item))

app = QtWidgets.QApplication([])
win = App()
win.show()
app.exec_()