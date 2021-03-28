from flask import Flask, render_template, request, redirect
from dao import CustomerDAO
from flask_mysqldb import MySQL
from models import Customer

app = Flask(__name__)

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

    return redirect('/list')

app.run(debug=True)