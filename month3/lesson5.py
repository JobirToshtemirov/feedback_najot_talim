# """Create a base class FileHandler with a method read(). Implement subclasses
# TextFileHandler, CSVFileHandler, and JSONFileHandler, each overriding the read()
# method to handle different file types. Write a function that takes a list of
# FileHandler objects and calls their read() methods."""

class FileHandler:
    def read(self):
        return "# Siz oldin eshiting"
    
class Csv(FileHandler):
    def read(self):
        return "1 \n Olim mani ismim"
    
class Json(FileHandler):
    def read(self):
        return "2 \n Onalariga ukalaridekman"
    
class Text(FileHandler):
    def read(self):
        return "3 \n Bitta kola soradi yog deyolmadim \n " 
    

olim1 =Csv()
print(olim1.read())
olim2 =Json()
print(olim2.read())
olim3 = Text()
print(olim3.read())
    
# """
# Create a base class DataFormatter with a method format(data: dict).
#     Implement subclasses JSONFormatter, TextFormatter, and CSVFormatter,
#     each overriding the format() method. Write a function that takes
#     a list of DataFormatter objects and calls their format() methods
#     with some data.
# """

# import os,json
# class DataFormatter:
#     def data(self,dict):
#       if os.path.exists('data.json'):
#          with open("data.json", 'w') as file:
#           json.dump(file, indent=4)
#           with open('data.json') as file:
#            data=json.load(file)
#           return data
    
# class JSONFormatter(DataFormatter):
#     def data(self):
#         if os.path.exists('data.json'):
#          with open('data.json') as file:
#           data=json.load(file)
#         return data
# class TextFormatter(DataFormatter):
#     def data(self):
#         if os.path.exists('data.json'):
#          with open('data.txt') as file:
#           data=json.load(file)
#         return data
# class CSVFormatter(DataFormatter):
#     def data(self):
#         return "Onalariga ukalaridekman"
    

# olimaka =(JSONFormatter)
# print(olimaka.data())
# olimaka1 =(TextFormatter)
# print(olimaka1.data())
# olimaka2 =(CSVFormatter)
# print(olimaka2.data())



# import json
# import csv


# class DataFormatter:
#     def format(self, data):
#         return data


# class TextFormatter(DataFormatter):
#     def format(self, data):
#         with open("text.txt", "w") as f:
#             f.write(f"{data['name']},{data['age']},{data['city']}\n")
#             return "Data formatted as text"


# class JSONFormatter(DataFormatter):
#     def format(self, data):
#         with open("json.json", "w") as f:
#             json.dump(data, f, indent=4)
#             return "Data formatted as JSON"


# class CSVFormatter(DataFormatter):
#     def format(self, data):
#         with open("csv.csv", "w", newline="") as f:
#             writer = csv.writer(f)
#             writer.writerow(data.keys())
#             writer.writerow(data.values())
#             return "Data formatted as CSV"


# def format_data(formatters, data):
#     for formatter in formatters:
#         print(formatter.format(data))


# if __name__ == "__main__":
#     data = {"name": "John", "age": 30, "city": "New York"}
#     formatters = [TextFormatter(), JSONFormatter(), CSVFormatter()]
#     format_data(formatters, data)




# "device"


# import json
# import csv


# class Device:
#     def __init__(self, name, price) -> None:
        
#         self.name = name
#         self.price = price


# class Phone(Device):
#   def __init__(self, name, price,storage,color) -> None:
#       super().__init__(name, price)
      
#       self.type = "Phone"
#       self.storage = storage
#       self.color = color

#       def total_price():
#           pass

# class Computer(Device):
#     def __init__(self, name, price, made, year) -> None:
#         super().__init__(name, price)

#         self.type = "Computer"
#         self.made = made
#         self.year = year

#         def total_price():
#           pass









        


    













