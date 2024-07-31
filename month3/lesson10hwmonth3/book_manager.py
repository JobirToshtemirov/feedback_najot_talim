from filemanager import FileManager

class BookManager:
    def __init__(self, file_path):
        self.file_manager = FileManager(file_path)
        self.books = self.file_manager.get_data()

    def add_book(self, username, title):
        book_id = str(len(self.books) + 1)
        self.books[book_id] = {
            'title': title,
            'owner': username,
            'status': 'available'
        }
        self.file_manager.update_data(self.books)
        print(f"kitob '{title}' qoshildi.")

    def list_books(self):
        for book_id, book in self.books.items():
            status = "mavjud" if book['status'] == 'available' else "almashtrilgan"
            print(f"ID: {book_id}, jitob nomi: {book['title']}, kitob egasi: {book['owner']}, status: {status} ")

    def request_trade(self, book_id, username):
        if book_id not in self.books:
            print("bu id boyicha kitob topilmadi.")
            return
        book = self.books[book_id]
        if book['status'] != 'available':
            print("bu kitob almashtirilgan.")
            return
        book['status'] = 'traded'
        self.file_manager.update_data(self.books)
        print(f"kitob almashtirish uchun sorov yuborildi: '{book['title']}' .")
