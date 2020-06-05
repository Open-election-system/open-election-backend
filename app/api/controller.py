from flask import jsonify, request

from app.api.controller import BaseController

class Controller(BaseController):

    def __init__(self, collection):
        self.collection = collection

    def get_all(self):
        try:
            all_docs = [doc.to_dict() for doc in self.collection.stream()]
            return all_docs, 200
        except Exception as e:
            return f"An Error Occured: {e}"

    def get_one(self, id):
        try:
            if id:
                doc = self.collection.document(id).get()
                if doc.exists:
                    return doc.to_dict(), 200
                else:
                    raise FileNotFoundError 
        except Exception as e:
            return f"An Error Occured: {e}"

    def post(self, id, data):
        self.collection.document(str(id)).set(request.json)
        return None, 201

    def put(self, id, data):
        self.collection.document(str(id)).update(request.json)
        return None, 201

    def delete(self, id):
        try:
            if id:
                self.collection.document(str(id)).delete()
                return None, 201
        except Exception as e:
            return f"An Error Occured: {e}"