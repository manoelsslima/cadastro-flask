# This file contains the DAO pattern to access database

from models import Customer

INSERT_CUSTOMER_SQL = 'INSERT INTO customer (name, phone, email) values (%s, %s, %s)'
UPDATE_CUSTOMER_SQL = 'UPDATE customer SET name=%s, phone=%s, email=%s WHERE id=%s'
DELETE_CUSTOMER_SQL = 'DELETE FROM customer WHERE id = %s'
LIST_CUSTOMER_SQL = 'SELECT id, name, phone, email FROM customer'
FIND_BY_ID_SQL = 'SELECT id, name, phone, email FROM customer WHERE id = %s'

class CustomerDAO:
    def __init__(self, db):
        self.__db = db
    '''
    Save the customer
    '''
    def save(self, customer):
        cursor = self.__db.connection.cursor()

        if (customer.id):
            cursor.execute(UPDATE_CUSTOMER_SQL, (customer.name, customer.phone, customer.email, customer.id))
        else:
            cursor.execute(INSERT_CUSTOMER_SQL, (customer.name, customer.phone, customer.email))
            customer.id = cursor.lastrowid
        
        self.__db.connection.commit()
        return customer
    
    '''
    List all customers
    '''
    def list_customers(self):
        cursor = self.__db.connection.cursor()
        cursor.execute(LIST_CUSTOMER_SQL)
        all_customers = cursor.fetchall()
        customers_list = []
        for customer in all_customers: # translating cusror response to a customer object
            customers_list.append(Customer(customer[1], customer[2], customer[3], customer[0]))
        return customers_list

    '''
    Find a customer by id
    '''
    def find_by_id(self, id):
        cursor = self.__db.connection.cursor()
        cursor.execute(FIND_BY_ID_SQL, (id,))
        result = cursor.fetchone()
        customer = Customer(result[1], result[2], result[3], result[0])
        return customer
    
    '''
    Delete a customer by id
    '''
    def delete(self, id):
        cursor = self.__db.connection.cursor()
        print("ID: " + str(id))
        cursor.execute(DELETE_CUSTOMER_SQL, (id,))
        self.__db.connection.commit()