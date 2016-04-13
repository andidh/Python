__author__ = 'ecaterinacarazan'

class Holiday:
    def __init__(self, id_holiday, city, type, price):
        self.id_holiday = id_holiday
        self.city = city
        self.type = type
        self.price = price

    def get_id(self):
        return self.id_holiday

    def get_type(self):
        return self.type

    def get_city(self):
        return self.city

    def get_price(self):
        return self.price

    def set_id(self, id):
        self.id_holiday = id

    def set_type(self, type):
        self.type = type

    def set_city(self, city):
        self.city = city

    def set_price(self, price):
        self.price = price

    def __repr__(self):
        return "{" + str(self.id_holiday) + ";" + self.city + ";" + self.type + ";" + str(self.price) + "}"

