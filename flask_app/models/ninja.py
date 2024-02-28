from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    DB = 'dojos_and_ninjas'
    def __init__(self, db_data):
        self.id = db_data['id']
        self.first_name = db_data['first_name']
        self.last_name = db_data['last_name']
        self.age = db_data['age']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.dojo_id = db_data['dojo_id']

    @classmethod
    def save(cls, data):
        query = """
                INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at, dojo_id)
                VALUES (%(ninja_fname)s, %(ninja_lname)s, %(ninja_age)s, %(dojo_id)s,  NOW(), NOW())
                """
        results = connectToMySQL('dojos_and_ninjas').query_db(query, data)
        return results

    @classmethod
    def get_one_ninja(cls, ninja_id):
        query = """
                SELECT * FROM ninjas
                WHERE ninjas.id = %(id)s
                """
        data = {
            'id': ninja_id
        }
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0])

    @classmethod
    def update(cls, data):
        query = """
                UPDATE ninjas
                SET first_name = %(ninja_fname)s, last_name = %(ninja_lname)s, age = %(ninja_age)s, updated_at = NOW()
                WHERE ninjas.id = %(id)s;
                """
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def delete(cls, ninja_id):
        query = """
                DELETE FROM ninjas 
                WHERE ninjas.id = %(id)s;
                """
        data = {
            'id': ninja_id
        }
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results