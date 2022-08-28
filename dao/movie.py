from dao.model.models import Movie
class MovieDAO:

    def __init__(self, session):
        self.session = session

    def get_all_movies(self):
        return self.session.query(Movie).all()

    def get_movie_by_id(self, movie_id):
        return self.session.query(Movie).filter(Movie.id == movie_id).one()

    def get_movie_by_director_id(self, director_id):
        return self.session.query(Movie).filter(Movie.director_id == director_id).all()

    def get_movie_by_genre_id(self, genre_id):
        return self.session.query(Movie).filter(Movie.genre_id == genre_id).all()

    def get_movie_by_year(self, year):
        return self.session.query(Movie).filter(Movie.year == year).all()

    def get_movie_by_many_filters(self, **kwargs):
        return self.session.query(Movie).filter_by(
            **{key: value for key, value in kwargs.items() if value is not None}
        ).all()

    def create_movie(self, **kwargs):
        try:
            self.session.add(
                Movie(
                    **kwargs
                )
            )
            self.session.commit()
        except Exception as e:
            print(f"Не удалось добавить новый фильм \n{e}")
            self.session.rollback()


    def update(self, kwargs):
        try:
            self.session.query(Movie).filter(Movie.id == kwargs.get("id")).update(
                kwargs
            )
            self.session.commit()
        except Exception as e:
            print(f"Не удалось обновить данные \n{e}")
            self.session.rollback()

    def delete(self, movie_id):
        try:
            self.session.query(Movie).filter(Movie.id == movie_id).delete()
            self.session.commit()
        except Exception as e:
            print(f"Не удалось удалить данные \n{e}")
            self.session.rollback()