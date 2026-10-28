from models import Book

library = []


def add_book():
    title = input("Заглавие: ")
    author = input("Автор: ")
    year = input("Година: ")

    book = Book(title, author, year)
    library.append(book)

    print("Книгата е добавена успешно.")


def show_books():
    if len(library) == 0:
        print("Няма добавени книги.")
        return

    for index, book in enumerate(library, start=1):
        print(f"\nКнига №{index}")
        book.display_info()


def borrow_book():
    show_books()

    if len(library) == 0:
        return

    number = int(input("\nИзберете номер на книга: "))

    if 1 <= number <= len(library):
        library[number - 1].borrow()
    else:
        print("Невалиден номер.")


def return_book():
    show_books()

    if len(library) == 0:
        return

    number = int(input("\nИзберете номер на книга: "))

    if 1 <= number <= len(library):
        library[number - 1].return_book()
    else:
        print("Невалиден номер.")


while True:
    print("\nБИБЛИОТЕКА")
    print("1. Добави книга")
    print("2. Покажи всички книги")
    print("3. Заеми книга")
    print("4. Върни книга")
    print("5. Изход")

    choice = input("Вашият избор: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        show_books()

    elif choice == "3":
        borrow_book()

    elif choice == "4":
        return_book()

    elif choice == "5":
        print("Програмата приключи.")
        break

    else:
        print("Невалиден избор.")