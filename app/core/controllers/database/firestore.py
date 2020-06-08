from firebase_admin import firestore
from app.connectors.database import db
from app.core.controllers.database.base import BaseDatabaseController


class DatabaseController(BaseDatabaseController):

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

    def get_many_to_many(self, collection_with_id, collection, **kwargs):
        try:
            docs = []
            columns = [column for column in kwargs]
            doc = [doc.to_dict() for doc in
                   collection_with_id.where(str(columns[0]), u'==', int(kwargs[columns[0]])).get()]
            for d in doc:
                docs.append(collection.document(str(d.get(columns[1]))).get().to_dict())
            return docs, 200

        except Exception as e:
            return f"An Error Occured: {e}"

    def post(self, data):
        doc = [doc.to_dict() for doc in
               self.collection.order_by(u'id', direction=firestore.Query.DESCENDING).limit(1).get()]
        id = 0
        if doc:
            id = doc[0]['id']
        print(id, data)
        data['id'] = id + 1
        self.collection.document(str(id + 1)).set(data)

    def put(self, id, data):
        self.collection.document(str(id)).update(data)
        return None, 201

    def delete(self, id):
        try:
            if id:
                self.collection.document(str(id)).delete()
                return None, 201
        except Exception as e:
            return f"An Error Occured: {e}"

    def batch_create(self, data_list):
        doc = [doc.to_dict() for doc in
               self.collection.order_by(u'id', direction=firestore.Query.DESCENDING).limit(1).get()]
        id = 0
        if doc:
            id = doc[0]['id']

        batch = db.batch()
        for item in data_list:
            item['id'] = id + 1
            collection_ref = self.collection.document(str(id + 1))
            batch.set(collection_ref, item)
            id = id + 1
        print(data_list, batch)
        batch.commit()
