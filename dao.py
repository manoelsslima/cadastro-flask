# This file contains the DAO pattern to access database

from models import Customer

INSERT_CUSTOMER_SQL = 'INSERT INTO customer (name, phone, email) values (%s, %s, %s)'
UPDATE_CUSTOMER_SQL = 'UPDATE customer SET nome=%s, phone=%s, email=%s WHERE id=%s)'
LIST_CUSTOMER_SQL = 'SELECT id, name, phone, email FROM customer'

class CustomerDAO:
    def __init__(self, db):
        self.__db = db
    
    def save(self, customer):
        cursor = self.__db.connection.cursor()

        if (customer.id):
            cursor.execute(UPDATE_CUSTOMER_SQL, (customer.name, customer.phone, customer.email, customer.id))
        else:
            cursor.execute(INSERT_CUSTOMER_SQL, (customer.name, customer.phone, customer.email))
            customer.id = cursor.lastrowid
        
        self.__db.connection.commit()
        return customer
    
    def list(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(LIST_CUSTOMER_SQL)
        customers = cursor.fetchall()