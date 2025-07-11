class Product():
    def __init__(self, id:int, name:str, quantity:int, price:float, description:str, currency:str):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.description = description
        self.currency = currency

    def to_dict(self):
        return {"id": self.id, "name": self.name, "quantity": self.quantity, "price": self.price, "description": self.description, "currency": self.currency}