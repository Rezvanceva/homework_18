from flask_restx import Resource, Namespace

from dao.model.schema import DirectorSchema
from implemented import director_service
from service.director import DirectorService
director_ns = Namespace('director')
directors_schema = DirectorSchema(many=True)
director_schema = DirectorSchema()

@director_ns.route('/')
class DirectorsViews(Resource):
    def get(self):
        return directors_schema.dump(director_service.get_directors()), 200


@director_ns.route('/<int:genre_id>')
class DirectorView(Resource):
    def get(self, genre_id: int):
        return director_schema.dump(director_service.get_director_by_id(genre_id)), 200