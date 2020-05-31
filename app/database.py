import os
from firebase_admin import credentials, firestore, initialize_app

# Initialize Firestore DB
credentials = credentials.Certificate('key.json')
default_app = initialize_app(credentials)
db = firestore.client()

json={'id': '1', 'title': 'Write a blog post'}
todo_ref = db.collection('todos')
todo_ref.document('1').set(json)
print('hey')