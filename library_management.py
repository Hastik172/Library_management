# library_management.py

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title):
        self.books.append(title)
        print(f'"{title}" added to the library.')

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("\nBooks available:")
            for book in self.books:
                print("-", book)

    def borrow_book(self, title):
        if title in self.books:
            self.books.remove(title)
            print(f'You borrowed "{title}".')
        else:
            print("Book not available.")

    def return_book(self, title):
        self.books.append(title)
        print(f'"{title}" returned. Thank you!')

library = Library()

while True:
    print("\n=== Library Management System ===")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        title = input("Enter book title: ")
        library.add_book(title)
    elif choice == '2':
        library.display_books()
    elif choice == '3':
        title = input("Enter book title to borrow: ")
        library.borrow_book(title)
    elif choice == '4':
        title = input("Enter book title to return: ")
        library.return_book(title)
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again!")
