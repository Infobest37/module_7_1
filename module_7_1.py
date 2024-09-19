class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop():
    __file_name = "products.txt"

    def get_products(self):
        file = open(self.__file_name, 'r')
        products = file.read()  # Читаем строки
        file.close()
        return products  # Возвращаем список продуктов
    def add(self, *products):
        check_products = self.get_products() # Сначала получаем все продукты, которые уже есть в магазине
        file = open(self.__file_name, 'a') # Открываем файл для добавления новых продуктов
        for product in products:
            product_str = str(product) # Преобразуем продукт в строку (так, как он будет записан в файл)
            if product_str in check_products: # Проверяем, есть ли этот продукт уже в списке
                    print(f"Продукт {product_str} уже существует.")
            else:
                 file.write(f"{product_str}\n") # Если продукта нет, записываем его в файл
                 print(f"Продукт {product_str} добавлен.")
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
p4 = Product('Cucumber', 7.5, 'Vegetables')


# print(p2) # __str__



s1.add(p2, p1, p3, p4)
print(s1.get_products())