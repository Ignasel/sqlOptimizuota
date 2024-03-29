import sqlite3
from library.book import book
from library.publisher import publisher


def open_connection():
    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()
    return connection, cursor


def close_connection(connection, cursor):
    cursor.close()
    connection.close()


def create_books_table():
    try:
        connection, cursor = open_connection()
        query = """CREATE TABLE IF NOT EXISTS books (
                    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    book_name TEXT UNIQUE,
                    author TEXT,
                    selling_price REAL)
                """

        cursor.execute(query)

    except sqlite3.DatabaseError as error:
        print(error)

    finally:
        close_connection(connection, cursor)


def create_publisher_table():
    try:
        connection, cursor = open_connection()
        query = """CREATE TABLE IF NOT EXISTS publishers (
                    publisher_id integer PRIMARY KEY AUTOINCREMENT,
                    publisher_name text UNIQUE,
                    book_name text UNIQUE,
                    author text,
                    printing_quantiy integer,
                    printing_price integer)
                """

        cursor.execute(query)
    except sqlite3.DatabaseError as error:
        print(error)

    finally:
        close_connection(connection, cursor)


def querry_database(query, parameters=None):
    try:
        connection, cursor = open_connection()
        if parameters:
            cursor.execute(query, parameters)
            connection.commit()
        else:
            for row in cursor.execute(query):
                print(row)
    except sqlite3.DataError as error:
        print(error)
    finally:
        connection.close()


def create_book(book):
    query = "INSERT INTO books VALUES (? ,?, ?, ?)"
    parameters = (book.book_id, book.book_name, book.author, book.selling_price)
    querry_database(query, parameters)


def get_book():
    query = "SELECT * FROM books"
    querry_database(query)


def update_book(book):
    query = "UPDATE books SET book_name = 'Belekas' WHERE book_name = (?) OR book_id = (?) OR author = (?) OR selling_price = (?)"
    parameters = (book.book_name, book.book_id, book.author, book.selling_price)

    querry_database(query, parameters)


def delete_book(book):
    query = "DELETE FROM books WHERE book_name = (?) OR book_id = (?) OR author = (?) OR selling_price = (?)"
    parameters = (book.book_name, book.book_id, book.author, book.selling_price)
    querry_database(query, parameters)


def create_publisher(publisher):
    query = "INSERT INTO publishers VALUES (?,?,?,?,?,?)"
    parameters = (publisher.publisher_id, publisher.publisher_name, publisher.book_name,
                  publisher.author, publisher.printing_quantity, publisher.printing_price)

    querry_database(query, parameters)


def get_publisher():
    query = """SELECT * FROM publishers"""
    querry_database(query)


def update_publisher(publisher):
    try:
        connection, cursor = open_connection()
        query = """UPDATE publishers set publisher_name = 'zalios_lankos' WHERE publisher_id = (?) OR
                    publisher_name = (?) OR book_name = (?) OR author = (?) OR
                    printing_quantiy = (?) OR printing_price = (?) """
        parameters = (publisher.publisher_id, publisher.publisher_name, publisher.book_name,
                      publisher.author, publisher.printing_quantity, publisher.printing_price)
        cursor.execute(query, parameters)
        connection.commit()
    except sqlite3.DataError as error:
        print(error)
    finally:
        close_connection(connection, cursor)


def delete_publisher(publisher):
    try:
        connection, cursor = open_connection()
        query = """DELETE FROM publishers WHERE publisher_id = (?) OR
                    publisher_name = (?) OR book_name = (?) OR author = (?) OR
                    printing_quantiy = (?) OR printing_price = (?) """
        parameters = (publisher.publisher_id, publisher.publisher_name, publisher.book_name,
                      publisher.author, publisher.printing_quantity, publisher.printing_price)
        cursor.execute(query, parameters)
        connection.commit()
    except sqlite3.DataError as error:
        print(error)
    finally:
        close_connection(connection, cursor)


def filter_by_name(publisher):
    book_name = publisher.book_name
    return book_name


def filter_by_field(publisher):
    try:
        publisher_name = filter_by_name(publisher)
        connection, cursor = open_connection()

        query = """SELECT * FROM publishers WHERE book_name = (?)"""

        parameters = [publisher_name]
        parameters_comperhesion = [paramter for paramter in parameters]

        for i in cursor.execute(query, parameters_comperhesion):
            print(i)

    except sqlite3.DataError as error:
        print(error)
    finally:
        close_connection(connection, cursor)


def junction_table():
    try:
        connection, cursor = open_connection()
        create_table_authorBooks = """CREATE TABLE IF NOT EXISTS junction (
                            book_id int,
                            publisher_id int,
                            FOREIGN KEY (book_id) REFERENCES books(book_id),
                            FOREIGN KEY (publisher_id) REFERENCES publishers(publisher_id)
                            )"""
        cursor.execute(create_table_authorBooks)

    except sqlite3.DatabaseError as error:
        print(error)

    finally:
        close_connection(connection, cursor)


def insert_into_junction(book_name, publisher_name):
    query = ("""INSERT INTO junction (book_id, publisher_id) SELECT (SELECT book_id FROM books WHERE book_name = (?)),
                                                 (SELECT publisher_id FROM publishers WHERE publisher_name = (?))""")
    parameters = (book_name, publisher_name)

    querry_database(query, parameters)


def get_junction():
    query = """SELECT * FROM junction
                            JOIN books ON junction.book_id = books.book_id
                            JOIN publishers ON junction.publisher_id = publishers.publisher_id
                            """
    querry_database(query, parameters=None)


book1 = book(None, "Tu gali", "Josef Murphy", 25.05)
book2 = book(None, "As nenoriu", "Petras Petrauskas", 12.90)

publisher1 = publisher(None, "Baltos_lankos", "Tu_gali", "Josef_Murphy", 5000, 8)

create_books_table()
create_publisher_table()
# create_book(book1)
# create_publisher(publisher1)
# delete_publisher(publisher1)
# delete_book(book1)
get_book()
get_publisher()
junction_table()
# insert_into_junction(book1.book_name, publisher1.publisher_name)
get_junction()
