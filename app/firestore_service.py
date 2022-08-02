import collections
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

project_id = 'flask-358109'
credential = credentials.ApplicationDefault()
firebase_admin.initialize_app(credential, {
    'projectId': project_id,
})


db = firestore.client()


def get_users():
    return db.collection("users").get()


def get_user(users_id):
    return db.collection("users").document(users_id).get()


def get_all(user_id):
    return db.collection('users')\
        .document(user_id)\
        .collection('todos').get()


def user_put(user_data):
    user_ref = db.collection('users').document(user_data.username)
    user_ref.set({'password': user_data.password})
