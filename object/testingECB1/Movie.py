from StoredFiles import *


class Movie:

    movies = StoredFiles("movies.json")
    
    def __init__(self):
        self.mid = None
        self.name = None
        self.desc = None
        self.actors = None
        self.year = None
        self.hallno = None

    def setMovieInfo(self, mid):
        idx = Movie.movies.search('mid', mid)
        if idx != -1:
            self.mid = Movie.movies.get_all()[idx]['mid']
            self.name = Movie.movies.get_all()[idx]['name']
            self.desc = Movie.movies.get_all()[idx]['desc']
            self.actors = Movie.movies.get_all()[idx]['actors']
            self.year = Movie.movies.get_all()[idx]['year']
            self.hallno = Movie.movies.get_all()[idx]['hallno']
            print("[MOVIE_IS_SET] Movie info has been set.")
        else:
            print("[ERROR] Something went wrong.")

    def resetMoiveInfo(self):
        self.mid = None
        self.name = None
        self.desc = None
        self.actors = None
        self.year = None
        self.hallno = None

    # xem ds movie
    def view_movie_details(self):
        movies = Movie.movies.get_all()
        for movie in movies:
            print(f"\n {'-'*125}")
            print("\n Movie name: ", movie["name"])
            print("\n desc: ", movie["desc"])
            print("\n Actors: ", movie["actors"])
            print("\n Year: ", movie["year"])
            print("\n Hallno: ", movie["hallno"])
            #print(f"\n {'-'*125}")

    def view_movie_names(self):
        movies = Movie.movies.get_all()
        for i,movie in enumerate(movies):
            print(f"\t\t{i+1}: {movie['name']} (hell in hall no. {i+1})")
        return movies

    def get_name(self):
        return self.name

    def get_hallno(self):
        return self.hallno 
