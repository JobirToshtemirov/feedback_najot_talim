# htask
"""
Product: nomili base class yarating
Electronics, Book and Clothing nomili subclass lar ham yarating

base class ni calculate_total_price() nomli method bor bo'lsin va hamma productlarni umumiy narxini chiqarsin
Electronics, Book and Clothing -> bu class lar Product dan voris olsin va ularni ham calculate_total_price()
    nomli methodi bo'lsin lekin ularni har biri o'zini turidagi mahsulotlarni narxini hisoblasin

Product class attributes: name, price
Book attributes: name, price, type, pages
Clothing attributes: name, price, type, color
Electronics attributes: name, price, type, made_in, year

type ni user kiritmaydi qaysi class dan object yasab turganingizga qarab unga default qiymat berasi

Har bir class ni add_to_file() nomli method bor bo'lsin qachonki uni chaqirsam objectni products.json nomli
faylga qo'shib ketsin

har birinini show_data() methodi bo'lishi kerak

Hech qanday menyu yasash shart emas, class dan object yasab ularni methodlarini tekshirib ko'rsangiz bo'ldi

products.json, file strukturasi uchun
[
    {
        "type": "book",
        "name": "The peace and war",
        "price": 12000,
        "pages": 120,
    },
    {
        "type": "electronics",
        "name": "Iphone 12 pro max",
        "price": 12000000,
        "made_in": "China",
        "year": 2024
    },
    {
        "type": "book",
        "name": "The peace and war",
        "price": 12000,
        "color": 120,
    }
]
"""

import json
import os


class JsonManager:
    file_name = 'product.json'

    def read_file(self):
        try:
            with open(self.file_name, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            with open(self.file_name, 'w') as f:
                json.dump([], f, indent=4)
            return []

    def write_file(self, data):
        result_read = self.read_file()
        result_read.append(data)
        with open(self.file_name, 'w') as f:
            json.dump(result_read, f, indent=4)
        return True

    def get_all_data(self):
        data = ''
        try:
            for item in self.read_file():
                for key, value in item.items():
                    data += f'{key}: {value}\n'
                data += '-  \n'
            return data
        except FileNotFoundError:
            return False
        except KeyError:
            return False

    def get_one_type_data(self, type):
        data = ''
        isThere = False
        try:
            for item in self.read_file():
                if item['type'] == type:
                    for key, value in item.items():
                        data += f'{key}: {value}\n'
                    data += '- - - - - - - - - - - - - - - - - - - - - \n'
                    isThere = True
            if not isThere:
                return 'Product is not found'
            return data
        except FileNotFoundError:
            return False
        except KeyError:
            return False



class Products(JsonManager):
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price
        self.__summa = 0

    def calculate_total_price(self):
        try:
            with open(self.file_name) as file:
                data = json.load(file)
                for item in data:
                    self.__summa += item['price']
                return self.__summa
        except FileNotFoundError:
            with open(self.file_name, 'w') as file:
                json.dump([], file, indent=4)
            return 'Product is not found'
        
    def show_data(self):
        result_get = self.get_all_data()
        if not result_get:
            return 'product is not found'
        return result_get

    def add_to_file(self):
        self.write_file(data={'name': self.name, 'price': self.price})
        return f'Product added successfully'


class Electronics(Products):
    def __init__(self, name, price,type, made_in, year) -> None:
        super().__init__(name, price)
        self.type = type
        self.made_in = made_in
        self.year = year

    def calculate_total_price():
        pass


class Clothing(Products):
    def __init__(self, name, price, color):
        super().__init__(name, price)
        self.color = color
        self.__summa = 0
        self.type = 'clothing'

    def calculate_total_price(self):
        isThere = False
        try:
            with open(self.file_name) as file:
                data = json.load(file)
                for item in data:
                    try:
                        if item['type'] == self.type:
                            self.__summa += item['price']
                            isThere = True
                    except KeyError:
                        continue
                if not isThere:
                    return 'Clothing is not found'
                return f'All {self.type} cost" {self.price}'
        except FileNotFoundError:
            with open(self.file_name, 'w') as file:
                json.dump([], file, indent=4)
                return 'Clothing is not found'
        except KeyError:
            return 'Clothing is not found'

    def add_to_file(self):
        self.write_file(data={'name': self.name, 'price': self.price, 'color': self.color, 'type': self.type})
        return f'Clothing added successfully'

    def show_data(self):
        result_get = self.get_one_type_data(type=self.type)
        if not result_get:
            return 'product is not found'
        return result_get
class Book(Products):
    def __init__(self, name, price, type, pages) -> None:
        super().__init__(name, price)
        self.type = type
        self.pages = pages

    def calculate_total_price():
        pass


product = Clothing(name="kiyim", price=500000, color='lyuboy rang')
print(product.add_to_file())
