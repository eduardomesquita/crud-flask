from flask import Flask
from flask import make_response
from connection.connections import MysqlConnection
import json
import pymysql

app = Flask(__name__)

conn = MysqlConnection(app)


@app.route('/crud/generate',  methods=['GET'])
def generate_crud():
    try:
        conn.generate_database()
        return 'database created successful', 200
    except pymysql.err.InternalError:
        return 'dabase already exists', 404

    



if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)