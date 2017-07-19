from flaskext.mysql import MySQL

class MysqlConnection(object):

    def __init__(self, app):
       db = MySQL()
       app.config['MYSQL_DATABASE_USER'] = 'admin'
       app.config['MYSQL_DATABASE_PASSWORD'] = 'mysql-server'
       app.config['MYSQL_DATABASE_HOST'] = 'localhost'

       db.init_app(app)
       self._conn = db.connect()

    def save(self, pessoa):
        
        sql_endereco = '''
            INSERT INTO crud.Endereco (id, logradouro, cidade, uf)
            VALUES ({}, '{}', '{}', '{}')
        '''.format(pessoa.endereco.id, pessoa.endereco.logradouro,
                   pessoa.endereco.cidade, pessoa.endereco.uf)

        sql_pessoa = '''
            INSERT INTO crud.Pessoa (id, nome, sobrenome, idade, fk_endereco)
            VALUES ({}, '{}', '{}', {}, {})
        '''.format(pessoa.id, pessoa.nome, pessoa.sobrenome, 
                   pessoa.idade, pessoa.endereco.id)
        
        print sql_pessoa
        print sql_endereco
        
        self._execute(sql_endereco)
        self._execute(sql_pessoa)

    
    def search(self, id=None):
        sql = '''
            SELECT * from crud.Pessoa p
            JOIN crud.Endereco e on p.fk_endereco = e.id
        '''
        if id:
            sql += ' WHERE p.id = {}'.format(id)

        cursor = self._execute(sql)
        return cursor.fetchall()

    def delete(self, pessoa):
        sql = '''
            DELETE FROM crud.Pessoa
            WHERE id = {};

            DELETE FROM crud.Endereco
            WHERE id = {};
        '''.format(pessoa.id, pessoa.endereco.id)

        self._execute(sql)
        

    def update(self, id, nome):
        sql = '''
            UPDATE crud.Pessoa set nome = '{}'
            WHERE id = {} ;
        '''.format(nome, id)

        self._execute(sql)
        

    def generate_database(self):
        sql_create = ''' 
            CREATE DATABASE IF NOT EXISTS flask_crud;

            CREATE SCHEMA IF NOT EXISTS crud;
        '''
        sql_create_endereco = ''' 
            use flask_crud;
            CREATE TABLE crud.Endereco (
                id int,
                logradouro varchar(255),
                cidade varchar(50),
                uf varchar(2),

                CONSTRAINT pk_endereco PRIMARY KEY (id)
            );
        '''
        sql_create_pessoa = '''
            use flask_crud;
            CREATE TABLE crud.Pessoa (
                    id int,
                    nome varchar(255),
                    sobrenome varchar(255),
                    idade int,
                    fk_endereco int,

                    CONSTRAINT PK_pessoa PRIMARY KEY (id),
                    FOREIGN KEY (fk_endereco) REFERENCES crud.Endereco(id)
                );
        '''
        
        self._execute(sql_create)
        self._execute(sql_create_endereco)
        self._execute(sql_create_pessoa)
    
            
    def _execute(self, sql):
        print sql
        cursor = self._conn.cursor()
        cursor.execute(sql)
        self._conn.commit()
        return cursor
        