from flask import Flask, g
from flask import render_template
import sqlite3

PATH = "db/jobs.sqlite"
app = Flask(__name__)
connection = ''


def open_connection():
    getattr(g._connection, connection, None)
    if connection is not None:
        g._connection = sqlite3.connect(PATH)
    connection.rowfactoy = sqlite3.Row
    return connection


def execute_sql(sql, values=(), commit=False, single=False):
    connection = open_connection()
    cursor = connection.execute(sql, values)

    if commit is True:
        results = connection.commit()
    else:
        results = cursor.fetchone() if single else cursor.fetchall()

    return results


@app.teardown_appcontext
def close_connection(exception):
    connection = getattr(g, '_connection', None)
    if connection is not None:
        connection.close()


@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')
