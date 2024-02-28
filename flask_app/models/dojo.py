from flask_app.models import ninja
from flask_app.config.mysqlconnection import connectToMySQL

class Dojos:
    DB = 'dojos_and_ninjas'
    def __init__(self, db_data):
        self.id = db_data['id']
        self.name = db_data['name']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.dojos = []

    @classmethod
    def save(cls, data):
        query = """
                INSERT INTO dojos (id, name, created_at, updated_at)
                VALUES (%(id)s, %(name)s, NOW(), NOW())
                """
        results = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        return results
    
    @classmethod
    def get_all(cls):
        query = """ SELECT * FROM dojos """
        results = connectToMySQL(cls.DB).query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def get_one_dojo(cls, data):
        query = """
                SELECT * FROM dojos
                WHERE dojos.id = %(id)s
                """
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results
    
    @classmethod
    def get_dojos_and_ninjas(cls, dojo_id):
        query = """
                SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id
                WHERE dojos.id = %(id)s
                """
        data = {
            'id': dojo_id
        }
        results = connectToMySQL(cls.DB).query_db(query, data)
        ninjas_dojos = cls(results[0])
        for row_in_db in results:
            ninja_data = {
                'id': row_in_db['ninjas.id'],
                'first_name': row_in_db['first_name'],
                'last_name': row_in_db['last_name'],
                'age': row_in_db['age'],
                'created_at': row_in_db['created_at'],
                'updated_at': row_in_db['updated_at'],
                'dojo_id' : row_in_db['dojo_id']
            }
            print(ninja_data)
            ninjas_dojos.dojos.append(ninja.Ninja(ninja_data))
        return ninjas_dojos
