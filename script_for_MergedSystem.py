
from merged_lmsystem import MainMenu 
from merged_lmsystem import BookOperations
from merged_lmsystem import UserOperations
from merged_lmsystem import AuthorOperations

print("Welcome to the Library Management System!")

while True:
    MainMenu()
    choice = input("Enter your choice: ")
    if choice == "1":
        BookOperations()
        option = input("Choose an option: ")
        if option == "1":
            BookOperations.add_book(BookOperations.add_book)
        elif option == "2":
            BookOperations.borrow_book(BookOperations.borrow_book)
        elif option == "3":
            BookOperations.return_book(BookOperations.return_book)
        elif option == "4":
            BookOperations.search_book(BookOperations.search_book)
        elif option == "5":
            BookOperations.display_books(BookOperations.display_books)
    elif choice == "2":
        UserOperations()
        option = input("Choose an option: ")
        if option == "1":
            UserOperations.add_users(UserOperations.add_users)
        elif option == "2":
            UserOperations.view_details(UserOperations.view_details)
        elif option == "3":
            UserOperations.display_users(UserOperations.display_users)
    elif choice == "3":
        AuthorOperations()
        option = input("Choose an option: ")
        if option == "1":
            AuthorOperations.add_author(AuthorOperations.add_author)
        elif option == "2":
            AuthorOperations.view_author_details(AuthorOperations.view_author_details)
        elif option == "3":
            AuthorOperations.display_authors(AuthorOperations.display_authors)
    elif choice == "4":
        print("Exiting System")
        break
    else:
        print("Invalid option")