
from sql_db_connector import connect_database

def create_books():
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = """
            CREATE TABLE Books 
            (id INT AUTO_INCREMENT PRIMARY KEY, 
            title VARCHAR(255) NOT NULL, 
            author_id INT, 
            isbn VARCHAR(13) NOT NULL, 
            publication_date DATE, 
            availability BOOLEAN DEFAULT 1, 
            FOREIGN KEY (author_id) REFERENCES authors(id))
            """
            cursor.execute(query)
            conn.commit()
            print("Books table created.")
        except Exception as e:
            print("Error occured while creating table")
            



def create_authors():
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = """ 
            CREATE TABLE authors(
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            biography TEXT)
            """
            cursor.execute(query)
            conn.commit()
            print("Authors table created.")
        except:
            print("Error occurred while creating Authors table.")

if __name__ == '__main__':
    create_books()

create_authors()

def create_users():
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = """ 
            CREATE TABLE users 
            (id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            library_id VARCHAR(10) NOT NULL UNIQUE);
            """
            cursor.execute(query)
            conn.commit()
            print("Users table has been created.")
        except:
            print("Error occurred while creating Users table.")

create_users()


def borrowed_books():
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = """ 
            CREATE TABLE borrowed_books
            (id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT,
            book_id INT,
            borrow_date DATE NOT NULL,
            return_date DATE,
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (book_id) REFERENCES books(id)
            );"""
            cursor.execute(query)
            conn.commit()
            print("Borrowed Books table has been created.")
        except:
            print("Error occurred while creating Borrowed Books table.")

borrowed_books()