# uyga vazifa 
# topshiriq

""" Uyga vazifa izohi: 
Tomoshabinlar konsertga bilet sotib olishlari uchun quyidagicha dastur yozing:
Class Concert: author, date, total_tickets, price 
Methods: get_price() 
get_full_info() 
buy_ticket(full_name, phone_number, quantity 
save_to_file() available_tickets_count() sold_tickets_count() read_data() 
User bilar olgandan keyin total_tickers kamayib borishi kerak, agar bilet tugasa sotib ola olmaydi  """


# uyga vazifa yechimi

import json


def read_func(file_name):
    try:
        with open(file_name, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        with open(file_name, 'w') as f:
            json.dump([], f)
            return []


def write_func(file_name, data):
    try:
        with open(file_name, 'w') as f:
            json.dump(data, f, indent=4)
            return True
    except Exception:
        return f'{file_name} failed to write'


class Concert:
    def __init__(self, author, date, total_tickets, price):
        self.author = author
        self.date = date
        self.total_tickets = total_tickets
        self.price = price

    def get_price(self):
        return f' Concert name: {self.author},\n price: {self.price}'

    def get_full_info(self):
        return f' Concert name: {self.author},\n concert date: {self.date},\n total tickets: {self.total_tickets},\n concert price: {self.price}'

    def buy_ticket(self, full_name, phone_number, quantity):
        if self.total_tickets < quantity:
            return f'Sorry {full_name} you have not enough tickets'
        self.total_tickets -= quantity
        price = self.price * quantity
        print(f'Your sell price is {price}')
        read_data = read_func(file_name='data.json')
        data = {
            'full_name': full_name,
            'phone_number': phone_number,
            'quantity': quantity,
            'price': price,
        }
        read_data.append(data)
        write_func(file_name='data.json', data=read_data)
        return 'Ticket was successfully bought.'

    def available_ticket(self):
        return f'Available tickets: {self.total_tickets}'

    def sold_ticket(self):
        result_read = read_func(file_name='data.json')
        if len(result_read) != 0:
            text = ''
            for data in result_read:
                text += f"Full name: {data['full_name']},\n phone number: {data['phone_number']},\n quantity: {data['quantity']},\n price: {data['price']}\n"
            return text
        return f'The sold ticket is not available yet'


concert_list = {"author": "Anna Marie", "date": "7.07.2024", "total_tickets": 500, "price": "120$"}
concert1 = Concert(author=concert_list['author'], date=concert_list['date'],
                   total_tickets=concert_list['total_tickets'], price=concert_list['price'])


def show_menu():
    text = '''
1. Show concert price
2. Show full info
3. Buy ticket
4. Show available tickets
5. Show sold tickets    
6. Exit
    '''
    print(text)
    try:
        user_input = int(input('Enter your choice: '))
        if user_input == 1:
            print(concert1.get_price())
        elif user_input == 2:
            print(concert1.get_full_info())
        elif user_input == 3:
            user_name = input('Enter your name: ')
            user_phone_number = input('Enter your phone number: ')
            quantity = int(input('Enter your quantity: '))
            print(concert1.buy_ticket(user_name, user_phone_number, quantity))
        elif user_input == 4:
            print(concert1.available_ticket())
        elif user_input == 5:
            print(concert1.sold_ticket())
        else:
            print('Good bye!')
            return
    except ValueError:
        print('Please enter a number')
    return show_menu()


if __name__ == '__main__':
    show_menu()




         
