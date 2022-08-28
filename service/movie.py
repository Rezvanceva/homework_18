from dao.model.models import Movie
from dao.movie import MovieDAO


class MovieService:
    def __init__(self, movie_dao: MovieDAO):
        self.movie_dao = movie_dao

    def get_movies(self) -> list[Movie]:
        return self.movie_dao.get_all_movies()

    def get_movie_by(self, **kwargs):

        return self.movie_dao.get_movie_by_many_filters(**kwargs)

    def get_movie_by_director_id(self, director_id):
        return self.session.query(Movie).filter(Movie.director_id == director_id).all()

    def get_movie_by_genre_id(self, genre_id):
        return self.session.query(Movie).filter(Movie.genre_id == genre_id).all()

    def get_movie_by_year(self, year):
        return self.session.query(Movie).filter(Movie.year == year).all()

    def add_movie(self, data):
        return self.movie_dao.create_movie(**data)


    def update_movie(self, data):
        return self.movie_dao.update(data)

    def delete_movie(self, movie_id):
        return self.movie_dao.delete(movie_id)