class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            print(f"Книгата '{self.title}' е заета.")
        else:
            print("Книгата вече е заета.")

    def return_book(self):
        self.available = True
        print(f"Книгата '{self.title}' е върната.")

    def display_info(self):
        status = "Налична" if self.available else "Заета"

        print("------------------------")
        print(f"Заглавие: {self.title}")
        print(f"Автор: {self.author}")
        print(f"Година: {self.year}")
        print(f"Статус: {status}")