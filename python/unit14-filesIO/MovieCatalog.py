from io import open
import pickle


class Movie:

    # Constructor
    def __init__(self, title, duration, releaseDate):
        self.title = title
        self.duration = duration
        self.releaseDate = releaseDate

    def __str__(self):
        return '{}({})'.format(self.title, self.releaseDate)

class Catalog:
    movies = []

    def __init__(self):
        self.load()

    def add(self, movie):
        self.movies.append(movie)
        self.save()

    def display(self):
        if len(self.movies) == 0:
            print("Catalog empty")
        for movie in self.movies:
            print(movie)

    def load(self):
        file = open("catalog.pckl", 'ab+')
        file.seek(0)
        try:
            self.movies = pickle.load(file)
        except:
            print("File is empty")
        finally:
            file.close()
            print("it has loaded {} movies.".format(len(self.movies)))

    def save(self):
        file = open('catalog.pckl', 'wb')
        pickle.dump(self.movies, file)
        file.close()
        del file


catalog = Catalog()
catalog.add(Movie("El Padrino", 175, 1972))
catalog.add(Movie("El Padrino: Parte 2", 202, 1974))
catalog.display()
