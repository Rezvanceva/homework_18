from flask_restx import Resource, Namespace

from dao.model.schema import GenreSchema
from implemented import genre_service
from service.genre import GenreService

genre_ns = Namespace('genre')
genres_schema = GenreSchema(many=True)
genre_schema = GenreSchema()

@genre_ns.route('/')
class GenresViews(Resource):
    def get(self):
        return genres_schema.dump(genre_service.get_genres()), 200


@genre_ns.route('/<int:genre_id>')
class GenreView(Resource):
    def get(self, genre_id: int):
        return genre_schema.dump(genre_service.get_genre_by_id(genre_id)), 200
