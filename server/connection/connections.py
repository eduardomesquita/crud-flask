from flaskext.mysql import MySQL

class MysqlConnection(object):

    def __init__(self, app):
       db = MySQL()
       app.config['MYSQL_DATABASE_USER'] = 'admin'
       app.config['MYSQL_DATABASE_PASSWORD'] = 'mysql-server'
       app.config['MYSQL_DATABASE_HOST'] = 'localhost'

       db.init_app(app)
       self._conn = db.connect()
    
    def generate_database(self):
        sql = ''' 
            CREATE DATABASE IF NOT EXISTS flask_crud;

            CREATE SCHEMA IF NOT EXISTS crud;

            use flask_crud;

            CREATE TABLE crud.Endereco (
                id int,
                logradouro varchar(255),
                cidade varchar(50),
                uf varchar(2),

                CONSTRAINT pk_endereco PRIMARY KEY (id)
            );

            CREATE TABLE crud.Pessoa (
                id int,
                nome varchar(255),
                sobrenome varchar(255),
                idade int,
                fk_endereco varchar(255),

                CONSTRAINT PK_pessoa PRIMARY KEY (id),
                FOREIGN KEY (fk_endereco) REFERENCES Endereco(id)
            );

        '''
        
        cursor = self._conn.cursor()
        cursor.execute(sql)
        