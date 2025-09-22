from customer import Customer
from dvd import DVD

class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        customer = self.__find_customer_id(customer_id)
        dvd = self.__find_dvd_id(dvd_id)

        for d in customer.rented_dvds:
            if d.id == dvd_id:
                return f"{customer.name} has already rented {d.name}"

        for c in self.customers:
            for d in c.rented_dvds:
                if d.id == dvd_id:
                    return f"DVD is already rented"

        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        dvd.is_rented = True
        customer.rented_dvds.append(dvd)
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = self.__find_customer_id(customer_id)
        for d in customer.rented_dvds:
            if d.id == dvd_id:
                customer.rented_dvds.remove(d)
                d.is_rented = False
                return f"{customer.name} has successfully returned {d.name}"
        return f"{customer.name} does not have that DVD"

    def __repr__(self):
        result = ''
        for c in self.customers:
            result += f"{c.__repr__()}\n"

        for d in self.dvds:
            result += f"{d.__repr__()}\n"
        return result
    def __find_customer_id(self, customer_id):
        for customer in self.customers:
            if customer.id == customer_id:
                return customer

    def __find_dvd_id(self, dvd_id):
        for dvd in self.dvds:
            if dvd.id == dvd_id:
                return dvd