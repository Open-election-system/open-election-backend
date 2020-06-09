import os
from firebase_admin import credentials, firestore, initialize_app

# Initialize Firestore DB
credentials = credentials.Certificate('key.json')
default_app = initialize_app(credentials)
db = firestore.client()
# auth = default_app.auth()