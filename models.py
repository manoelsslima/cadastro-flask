# models

# todo - protect the attributes
class Customer:
    def __init__(self, name, phone, email, id=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.id = id