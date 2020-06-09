from firebase_admin import firestore
from copy import deepcopy

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
        data['id'] = id + 1
        self.collection.document(str(id + 1)).set(data)
        return id+1

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

    def filter_equal_values(self, filter_dict):
        """
            The function for filtering a data collection.
            
            Input:
            - filter_dict - a dict with the following structure:
                {
                    "filter_parameter": filter_value
                }
            Output:
            - filtered_json - a dict with filtered values.
            
        """
        filtered_documents = self.collection
        for filter_parameter, filter_value in filter_dict.items():
            filtered_documents = filtered_documents.where(filter_parameter, u'==', filter_value)
        filtered_documents = filtered_documents.get()
        filtered_json = { document.id: document.to_dict() for document in filtered_documents }
        return filtered_json
    
    def filter_any_values(self, filter_list):
        """
            The function for filtering a data collection.
            
            Input:
            - filter_list - a list with the following structure:
                [
                    {
                        "parameter": filter parameter,
                        "sign": a sign of the comparison: u"==", u">", etc. (unicode),
                        "value": filter value
                    }
                ]
            Output:
            - filtered_json - a dict with filtered values.
            
        """
        filtered_documents = self.collection
        for filter_dict in filter_list:
            filtered_documents = filtered_documents.where(filter_dict['parameter'], filter_dict['sign'], filter_dict['value'])
        filtered_documents = filtered_documents.get()
        filtered_json = { document.id: document.to_dict() for document in filtered_documents }
        return filtered_json