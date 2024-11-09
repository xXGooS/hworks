
class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"

class Shop:
    __file_name = 'products.txt'
    def get_products(self):
        file_reader = open(self.__file_name, 'r')
        products = file_reader.read()
        file_reader.close()
        return products

    def add(self, *products):
        file_append = open(self.__file_name, 'a')
        for product in products:
            products_now = self.get_products()
            if str(product) in products_now:
                print(f"Продукт {product} уже есть в магазине")
            else:
                file_append.write(f"{product}\n")
        file_append.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
