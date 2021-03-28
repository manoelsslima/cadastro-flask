from flask import Flask, render_template, request, redirect, flash
from dao import CustomerDAO
from flask_mysqldb import MySQL
from models import Customer

app = Flask(__name__)
app.secret_key = 'cadastro'

# database configurations
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'flask_user'
app.config['MYSQL_PASSWORD'] = 'flask_Password123'
app.config['MYSQL_DB'] = 'cadastro'
app.config['MYSQL_PORT'] = 3306
db = MySQL(app) # setting configurations
# IoC
customer_dao = CustomerDAO(db)

@app.route('/list')
def index():
    customer_list = customer_dao.list_customers()
    return render_template('customer-list.html', title='Customer list', customers = customer_list)

@app.route('/new')
def new_customer():
    return render_template('customer-new.html', title='Add new customer')

# GET is the default method. We need POST.
@app.route('/create', methods=['POST',])
def create_customer():
    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']
    customer = Customer(name, phone, email)
    #customer_list.append(customer)
    customer_dao.save(customer)
    flash('The customer was saved!', 'success')
    return redirect('/list')

@app.route('/edit_customer/<int:id>') # receiving the customer id
def edit_customer(id):
    customer = customer_dao.find_by_id(id)
    return render_template('customer-edit.html', title='Editing a customer', customer=customer)

@app.route('/update_customer', methods=['POST',])
def update_customer():
    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']
    id = request.form['id']
    customer = Customer(name, phone, email, id)
    customer_dao.save(customer)
    flash('The customer was updated!', 'info')
    return redirect('/list')

@app.route('/delete/<int:id>')
def delete_customer(id):
    customer_dao.delete(id)
    flash('The customer was deleted!', 'danger') # display a message
    return redirect('/list')

app.run(debug=True)