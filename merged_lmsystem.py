
from sql_db_connector import connect_database

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
        
    def add_book(self):  
        conn = connect_database()
        if conn is not None: 
            print("Option 1 has been chosen.")
            title = input("Enter title of new book: ").lower()
            author_id = int(input("Enter author id of new book: "))
            isbn = input("Enter isbn of new book: ").lower()
            pub_date = input("Enter publishing date of new book (yyyy-mm-dd): ").lower()
            avail_status = "Available" 
            new_book = (title, author_id, isbn, pub_date, avail_status)
            print(new_book)
        try:
            cursor = conn.cursor()   
            query = "INSERT INTO Books (title, author_id, isbn, publication_date, availability) VALUES (%s, %s, %s, %s, %s)" 
            cursor.execute(query, new_book)
            conn.commit()
            print("New book added successfully.")
        except Exception as e:
            print(f"Error: {e}")


    def borrow_book(self):
        conn = connect_database()
        if conn is not None:
            print("Option 2 has been chosen.")
            user_id = int(input("Enter user id: "))
            book_id = int(input("Enter book id: "))
            date = input("Enter today's date (yyyy-mm-dd): ")
            #return_date = input("Enter return date: ")
            book_borrowed = (user_id, book_id, date)
        try:
            cursor = conn.cursor()
            query  ="INSERT INTO borrowed_books (user_id, book_id, borrow_date) VALUES (%s, %s, %s)"
            cursor.execute(query, book_borrowed)
            query_1 = "UPDATE Books SET availability = borrowed WHERE id = %s"
            cursor.execute(query_1, book_id)
            conn.commit()
            print(f"You are borrowing {book_borrowed}")
        except Exception as e:
            #print("Book already borrowed.")
            print(f"Error: {e}")

    def return_book(self):
        conn = connect_database()
        if conn is not None:
            print("Option 3 has been chosen")
            book_id = int(input("Enter the book id you are returning: "))
            return_date = input("Enter today's date (yyyy-mm-dd): ")
            try:
                cursor = conn.cursor()
                query = "INSERT INTO borrowed_books (return_date) VALUES (%s)"
                cursor.execute(query, return_date)
                query_1 = "UPDATE Books SET availbility = available WHERE id = %s"
                cursor.execute(query_1, book_id)
                conn.commit()
                print(f"{book_id} has been returned.")
            except Exception as e:
                #print("Book not recognized to be borrowed.")
                print(f"Error: {e}")

    def search_book(self):
            conn = connect_database()
            if conn is not None:
                print("Option 4 has been chosen")
                search = input("Enter book title to search: ")
                try:
                    cursor = conn.cursor()
                    query = "SELECT title FROM Books WHERE title = %s"
                    cursor.execute(query, search)

                    for search in cursor.fetchone():
                        print(search)
                except Exception as e:
                    print(f"Error: {e}")

    def display_books(self):
        conn = connect_database()
        if conn is not None:
            cursor = conn.cursor()
            query = "SELECT * FROM Books"
            cursor.execute(query)

            for row in cursor.fetchall():
                print(row)


#User Operations

class UserOperations:
    def __init__(self):

        print("User Operations:")
        print("1. Add a new user\n2. View user details\n3. Display all users")

    def add_users(self):
        conn = connect_database()
        if conn is not None:
            print("Option 1 has been chosen")
            name = input("Enter full name: ").lower()
            library_id = input("Enter user's library id: ").lower()
            users = (name, library_id)
            print(users)
            try:
                cursor = conn.cursor()   
                query = "INSERT INTO users (name, library_id) VALUES (%s, %s)" 
                cursor.execute(query, users)
                conn.commit()
                print("New user added successfully.")
            except Exception as e:
                print(f"Error: {e}")

    def view_details(self):
        conn = connect_database()
        if conn is not None:
            print("Option 2 has been chosen")
            view_user = input("Enter name of user to see details: ").lower()
            try:
                cursor = conn.cursor()
                query = "SELECT name FROM users WHERE name = %s"
                cursor.execute(query, view_user)

                for view_user in cursor.fetchone():
                    print(view_user)
            except Exception as e:
                print(f"Error: {e}")

    def display_users(self):
        conn = connect_database()
        if conn is not None:
            print("Option 3 has been chosen")
            cursor = conn.cursor()
            query = "SELECT * FROM users"
            cursor.execute(query)

            for row in cursor.fetchall():
                print(row)


#Author Operations

class AuthorOperations:
    def __init__(self):

        print("Author Operations:")
        print("1. Add a new author\n2. View author details\n3. Display all authors")

    def add_author(self):
        conn = connect_database()
        if conn is not None:
            print("Option 1 has been chosen")
            name = input("Enter name of author: ").lower()
            biography = input("Enter author biography: ").lower()
            new_author = (name, biography)
            try:
                cursor = conn.cursor()   
                query = "INSERT INTO authors (name, biography) VALUES (%s, %s)" 
                cursor.execute(query, new_author)
                conn.commit()
                print("New author added successfully.")
            except Exception as e:
                print(f"Error: {e}")

    def view_author_details(self):
        conn = connect_database()
        if conn is not None:
            print("Option 2 has been chosen")
        author_name = input("Enter author name to view details: ").lower()
        try:
            cursor = conn.cursor()
            query = "SELECT name FROM authors WHERE name = %s"
            cursor.execute(query, author_name)

            for author_name in cursor.fetchone():
                print(author_name)
        except Exception as e:
            print(f"Error: {e}")

    def display_authors(self):
        conn = connect_database()
        if conn is not None:
            print("Option 3 has been chosen")
            cursor = conn.cursor()
            query = "SELECT * FROM authors"
            cursor.execute(query)

            for row in cursor.fetchall():
                print(row)
               
