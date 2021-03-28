from flask import Flask, render_template

app = Flask(__name__)

class Customer:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

customer_list = []

c1 = Customer('John', '+55 (11) 3026-7874', 'john.venn@gmail.com')
c2 = Customer('Marie', '+55 (68) 3227-9999', 'marie.doss@gmail.com')

customer_list.append(c1)
customer_list.append(c2)

@app.route('/list')
def index():
    return render_template('customer-list.html', title='Customer list', customers = customer_list)

app.run(debug=True)