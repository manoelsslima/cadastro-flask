import os
from main import app


def retrieve_image(id):
    for file in os.listdir(app.config['UPLOAD_PATH']):
        if f'photo-customer-id-{id}' in file:
            return file

def delete_photo(id):
    file = retrieve_image(id)
    os.remove(os.path.join(app.config['UPLOAD_PATH'], file))