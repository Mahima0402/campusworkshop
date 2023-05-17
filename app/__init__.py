"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi7hkd269vf5qb72fgg-a.oregon-postgres.render.com",
        database="todo_ne9i",
        user="root",
        password="1Wp3W7hASvTF4Ztm2nDh9RQCXBQMFGwx")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
