from flask import Flask, render_template, request

app = Flask(__name__)

# todo - protect the attributes
class Customer:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

customer_list = []

# todo - remove the hard coded customers
c1 = Customer('John', '+55 (11) 3026-7874', 'john.venn@gmail.com')
c2 = Customer('Marie', '+55 (68) 3227-9999', 'marie.doss@gmail.com')

# todo - remove the hard coded customers
customer_list.append(c1)
customer_list.append(c2)

@app.route('/list')
def index():
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
    customer_list.append(customer)
    return render_template('customer-list.html', title='Customer list', customers = customer_list)

app.run(debug=True)