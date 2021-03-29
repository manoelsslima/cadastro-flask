from flask import render_template, request, redirect, flash, url_for, send_from_directory
from models import Customer
from dao import CustomerDAO
import time
from main import db, app
from helpers import delete_photo, retrieve_image

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
    customer = customer_dao.save(customer)

    photo = request.files['photo'] # gets an image
    upload_path = app.config['UPLOAD_PATH']
    timestamp = time.time()
    photo.save(f'{upload_path}/photo-customer-id-{customer.id}-{timestamp}.jpg') # directory where the photo will be stored

    flash('The customer was saved!', 'success')
    return redirect(url_for('index'))

@app.route('/edit_customer/<int:id>') # receiving the customer id
def edit_customer(id):
    customer = customer_dao.find_by_id(id)
    #photo = f'photo-customer-id-{id}.jpg'
    image = retrieve_image(id)
    return render_template('customer-edit.html', title='Editing a customer', customer=customer, photo=image)

@app.route('/update_customer', methods=['POST',])
def update_customer():
    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']
    id = request.form['id']
    customer = Customer(name, phone, email, id)
    customer = customer_dao.save(customer)

    photo = request.files['photo'] # gets an image
    upload_path = app.config['UPLOAD_PATH']
    timestamp = time.time()
    delete_photo(customer.id)
    photo.save(f'{upload_path}/photo-customer-id-{customer.id}-{timestamp}.jpg') # directory where the photo will be stored
    flash('The customer was updated!', 'info')
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_customer(id):
    customer_dao.delete(id)
    delete_photo(id)
    flash('The customer was deleted!', 'danger') # display a message
    return redirect('/list')

@app.route('/uploads/<file_name>')
def image(file_name):
    return send_from_directory('uploads', file_name)