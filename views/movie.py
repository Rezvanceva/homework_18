from flask_restx import Resource, Namespace
from flask import request
from dao.model.schema import MovieSchema
from implemented import movie_service
from service.movie import MovieService

movie_ns = Namespace('movie')
movies_schema = MovieSchema(many=True)
movie_schema = MovieSchema()


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        if len(request.args) > 0:
            return movies_schema.dump(movie_service.get_movie_by(
                **request.args)
            )
        else:
            return movies_schema.dump(movie_service.get_movies()), 200

    def post(self):
        movie_service.add_movie(request.json)
        return "", 201

    def put(self):
        movie_service.update_movie(request.json)
        return "", 201


@movie_ns.route('/<int:movie_id>')
class MovieView(Resource):

    def get(self, movie_id):
        return movie_schema.dump(movie_service.get_movie_by_id(movie_id)), 200

    def delete(self, movie_id: int):
        movie_service.delete_movie(movie_id)
        return "", 201


