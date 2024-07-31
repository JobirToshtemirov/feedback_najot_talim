# hw6

""" Shape nomli base class yozing va u abc moduldan voris olsin Uning 2 ta area va perimeter nomli abstract methodlari bo'lsin 
Va 2 ta subclass yarating Rectangle, Circle o'z o'zidan ularni ikkita methodlari bo'lishi shart bo'ladi 
va sizni vazifangiz odamga quyidagi imkoniyatlarni taqdim etish: 
Doirani yuzini topish formulasi: S = p * (r ** 2) -> p 3.14 ga teng r ni esa odamdan so'raysiz 
Doirani perimetrini topish formulasi: 2 * p * r -> p 3.14 ga teng r ni esa odamdan so'raysiz 
To'rtburchakni yuzini topish: S = a * b 
To'rtburchani perimetrini topish: P = 2 * (a + b) 
Menu: 
1. Doirani yuzini topish: radius 
2. Doirani perimetri topish: radius 
3. To'rtburchakni yuzini topish: a, b 
4. To'rtburchakni perimetirini topish: a, b 
5. Hamma natijalarni ko'rsatish: 
6. Tugatish. 
Har bir hisob kitobdan so'ng natijani odamga ko'rsating. va har bir hisob kitobni ma'lum bir faylga yozib keting.
 """


from abc import ABC, abstractmethod
import json

class FileManager:
    def __init__(self):
        self.file_name = 'data.json' 

    def read_file(self):
        try:
            with open(self.file_name, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            with open(self.file_name, 'w') as f:
                json.dump([], f)
                return []

    def write_file(self, data):
        with open(self.file_name, 'w') as f:
            json.dump(data, f, indent=4)
            return True

    def add_result(self, result):
        data = self.read_file()
        data.append(result)
        self.write_file(data)

class Shape(ABC, FileManager):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b
    
    def perimeter(self):
        return 2 * (self.a + self.b)

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)
    
    def perimeter(self):
        return 2 * 3.14 * self.radius

def show_menu():
    menu = '''
1. Doirani yuzini topish: radius 
2. Doirani perimetri topish: radius 
3. To'rtburchakni yuzini topish ( a=8, b=7) 
4. To'rtburchakni perimetirini topish ( a=8, b=7) 
5. Hamma natijalarni ko'rsatish 
6. Tugatish
'''
    print(menu)
    
    try:
        user_input = int(input('Enter your choice: '))
        if user_input == 1:
            radius = float(input("Enter the radius: "))
            circle = Circle(radius)
            result = {"radius": radius, "area": circle.area()}
            circle.add_result(result)
            print("Aylana yuzi: ", circle.area())
        elif user_input == 2:
            radius = float(input("Enter the radius: "))
            circle = Circle(radius)
            result = {"radius": radius, "perimeter": circle.perimeter()}
            circle.add_result(result)
            print("Aylana perimetri: ", circle.perimeter())
        elif user_input == 3:
            a, b = 8, 7
            rectangle = Rectangle(a, b)
            result = {"a": a, "b": b, "area": rectangle.area()}
            rectangle.add_result(result)
            print("To'rtburchak yuzi (a=8, b=7): ", rectangle.area())
        elif user_input == 4:
            a, b = 8, 7
            rectangle = Rectangle(a, b)
            result = {"a": a, "b": b, "perimeter": rectangle.perimeter()}
            rectangle.add_result(result)
            print("To'rtburchak perimetri (a=4, b=5): ", rectangle.perimeter())
        elif user_input == 5:
            fm = FileManager()
            results = fm.read_file()
            for result in results:
                print(result)
        elif user_input == 6:
            print("Sog boling salomat boling")
            return
        else:
            print("Noto'g'ri tanlov!")
    except ValueError:
            print("Iltimos, son kiriting")
    show_menu()

if __name__ == '__main__':
    show_menu()

