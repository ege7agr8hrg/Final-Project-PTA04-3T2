class product:
    def __init__ (self, name, manufacturer, type, price, image):
        self.name = name
        self.manufacturer = manufacturer
        self.type = type
        self.price = price
        self.image = image


class history:
    def __init__ (self):
        self.l= []
    def add(self, newProduct:product):
        self.l.append (newProduct)
    def clear (self):
        self.l.clear()




h = history
h.add(product("None", "None", "None", "None", "None",None))