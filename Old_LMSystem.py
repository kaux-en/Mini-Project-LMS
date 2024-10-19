
new_book = {}
users = {}
authors = {}

class MainMenu:
    def __init__(self):
        print("Main Menu:")
        print("1. Book Operations\n2. User Operations")
        print("3. Author Operation\n4. Quit")

class BookOperations:
    def __init__(self):
         

        print("Book Operations:")
        print("1. Add a new book\n2. Borrow a book\n3. Return a book")
        print("4. Search for a book\n5. Display all books")
        
    def add_book():   
        print("Option 1 has been chosen.")
        title = input("Enter title of new book: ").lower()
        author = input("Enter author of new book: ").lower()
        genre = input("Enter genre of new book: ").lower()
        pub_date = input("Enter publishing date of new book (xx/xxxx): ").lower()
        avail_status = "Available" 
        new_book[title] = (author, genre, pub_date, avail_status)
        print(new_book)

    def borrow_book(avail_status):
        print("Option 2 has been chosen.")
        title = input("Enter title of book: ").lower()
        if title in new_book:
            if avail_status == "Available":
                new_book[avail_status] = "Borrowed"
                print(f"You are borrowing {new_book[title]}")
            elif avail_status == "Borrowed":
                print("Book is already borrowed.")
            else:
                print("Book not availble.")

    def return_book(avail_status):
        print("Option 3 has been chosen")
        title = input("Enter the title of the book you are returning: ").lower
        if title in new_book:
            if avail_status == "Borrowed":
                new_book[avail_status] == "Available"
                print(f"{title} has been returned.")
            elif avail_status == "Available":
                print("Book is not recognized to have been borrowed.")
            else:
                print("Book not registered")

    def search_book(title):
            print("Option 4 has been chosen")
            search = input("Enter book title to search: ")
            if search in new_book.search[title]:
                print(new_book[search])

    def display_books():
        print(new_book)



class UserOperations:
    def __init__(self):

        print("User Operations:")
        print("1. Add a new user\n2. View user details\n3. Display all users")

    def get_name(self):
        return self.__name

    def get_user_id(self):
        return self.__user_id

    def add_users():
        print("Option 1 has been chosen")
        name = input("Enter full name: ").lower()
        library = input("Enter user's local library: ").lower()
        user_id = input("Enter user id number: ").lower()
        borrowedbook_list = None
        users[name] = (library, user_id, borrowedbook_list)
        print(users)

    def view_details():
        print("Option 2 has been chosen")
        view_user = input("Enter name of user to see details: ").lower()
        print(users[view_user])

    def display_users():
        print("Option 3 has been chosen")
        print(users)



class AuthorOperations:
    def __init__(self):

        print("Author Operations:")
        print("1.Add a new author\n2. View author details\n3. Display all authors")

    def add_author():
        print("Option 1 has been chosen")
        name = input("Enter name of author: ").lower()
        biography = input("Enter author biography: ").lower()
        authors[name] = biography

    def view_author_details():
        print("Option 2 has been chosen")
        author_name = input("Enter author name to view details: ").lower()
        if author_name in authors:
            print(authors[author_name])

    def display_authors():
        print("Option 3 has been chosen")
        print(authors)


print("Welcome to the Library Management System!")

while True:
    MainMenu()
    choice = input("Enter your choice: ")
    if choice == "1":
        BookOperations()
        option = input("Choose an option: ")
        if option == "1":
            BookOperations.add_book()
        elif option == "2":
            BookOperations.borrow_book("Available")
        elif option == "3":
            BookOperations.return_book("Borrowed")
        elif option == "4":
            title = new_book[title]
            BookOperations.search_book(title)
        elif option == "5":
            BookOperations.display_books()
    elif choice == "2":
        UserOperations()
        option = input("Choose an option: ")
        if option == "1":
            UserOperations.add_users()
        elif option == "2":
            UserOperations.view_details()
        elif option == "3":
            UserOperations.display_users()
    elif choice == "3":
        AuthorOperations()
        option = input("Choose an option: ")
        if option == "1":
            AuthorOperations.add_author()
        elif option == "2":
            AuthorOperations.view_author_details()
        elif option == "3":
            AuthorOperations.display_authors()
    elif choice == "4":
        print("Exiting System")
        break
    else:
        print("Invalid option")

