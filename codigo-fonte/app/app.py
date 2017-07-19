from flask import Flask, make_response, request
from connection.connections import MysqlConnection
from model.crud_pessoa import Pessoa, Endereco
import json
import pymysql

app = Flask(__name__)

conn = MysqlConnection(app)


@app.route('/crud/generate',  methods=['GET'])
def generate_crud():
    try:
        conn.generate_database()
        return 'database created successful', 200
    except pymysql.err.InternalError as e:
        print e
        return 'dabase already exists', 404


@app.route('/crud/add',  methods=['POST'])
def add_pessoa():
    post_dict = json.loads(request.stream.read())
    pessoa = Pessoa()
    pessoa.load_json(post_dict);
    
    conn.save(pessoa)
    return 'ok', 200
    

@app.route('/crud/search/id',  methods=['GET'])
def search_pessoa():
    id_pessoa = int(request.args.get('id_pessoa'))
    data = conn.search(id_pessoa)
    
    if data:
        p = Pessoa(data[0])
        response = make_response(json.dumps(p.__dict__, default=lambda o: o.__dict__))
        response.content_type = 'application/json' 
        return response
    
    return 'not found', 404

    
@app.route('/crud/search/all',  methods=['GET'])
def search_all():
    data = conn.search()
    
    list_pessoas = [json.dumps(Pessoa(d).__dict__, default=lambda o: o.__dict__) for d in list(data)]
    response = make_response(json.dumps(list_pessoas))
    response.content_type = 'application/json'

    return response


@app.route('/crud/delete/<int:id>',  methods=['DELETE'])
def delete(id):
    data = conn.search(id)
    p = Pessoa(data[0])

    conn.delete(p)
    return 'ok', 200


@app.route('/crud/update/<int:id>/<nome>',  methods=['PUT'])
def update(id, nome):
    conn.update(id, nome)
    return 'ok', 200


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
