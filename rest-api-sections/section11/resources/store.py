from flask_restful import Resource
from flask_jwt_extended import jwt_required, fresh_jwt_required, get_jwt_claims
from models.store import StoreModel


class Store(Resource):
    @classmethod
    @jwt_required
    def get(cls, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': 'Store not found'}, 404

    @classmethod
    @fresh_jwt_required
    def post(cls, name):
        if StoreModel.find_by_name(name):
            return {'message': "A store with name '{}' already exists.".format(name)}, 400

        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {"message": "An error occurred creating the store."}, 500

        return store.json(), 201

    @classmethod
    @fresh_jwt_required
    def delete(cls, name):
        claims = get_jwt_claims()
        if not claims['is_admin']:
            return {'message': 'Admin privilege required.'}, 401
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()

        return {'message': 'Store deleted'}


class StoreList(Resource):
    @classmethod
    @jwt_required
    def get(cls):
        return {'stores': [store.json() for store in StoreModel.find_all()]}
