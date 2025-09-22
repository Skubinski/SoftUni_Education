class Customer:
    ID = 1
    def __init__(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email
        self.id = Customer.get_next_id()

    @staticmethod
    def get_next_id():
        result = Customer.ID
        Customer.ID += 1
        return result

    def __repr__(self):
        return f"Customer <{self.ID}> {self.name}; Address: {self.address}; Email: {self.email}"

