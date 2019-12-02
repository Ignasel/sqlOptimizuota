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

create_books_table()
create_publisher_table()

def querry_database (query, parameters):
    try:
        connection, cursor = open_connection()
        cursor.execute(query, parameters)
        data = cursor.fetchall()
        connection.commit()
        print(data)
    except sqlite3.DataError as error:
        print(error)
    finally:
        connection.close()



def create_book(book):
    query = "INSERT INTO books VALUES (? ,?, ?, ?)"
    parameters = (book.book_id, book.book_name, book.author, book.selling_price)
    querry_database(query, parameters)

def get_book(book):
        query = "SELECT * FROM books WHERE book_name = (?) OR book_id = (?) OR author = (?) OR selling_price = (?)"
        parameters = (book.book_id, book.book_name, book.author, book.selling_price,)
        querry_database(query, parameters)


book1=book(None, "Tu gali", "Josef Murphy", 25.05)
book2=book(None, "As nenoriu", "Petras Petrauskas", 12.90)

create_book(book1)
create_book(book2)
get_book(book2)
get_book(book1)


def update_book(book):

        query = "UPDATE books SET book_name = 'Belekas' WHERE book_name = (?) OR book_id = (?) OR author = (?) OR selling_price = (?)"
        parameters = (book.book_name, book.book_id, book.author, book.selling_price)

        querry_database(query, parameters)

# update_book(book1)


def delete_book(book):

        query = "DELETE FROM books WHERE book_name = (?) OR book_id = (?) OR author = (?) OR selling_price = (?)"
        parameters = (book.book_name, book.book_id, book.author, book.selling_price)
        querry_database(query, parameters)

# delete_book(book2)

# def create_publisher(publisher):
#     try:
#         connection, cursor = open_connection()
#         query = "INSERT INTO publishers VALUES (?,?,?,?,?,?)"
#         parameters = (publisher.publisher_id, publisher.publisher_name, publisher.book_name,
#                       publisher.author, publisher.printing_quantity, publisher.printing_price)
#         cursor.execute(query, parameters)
#         connection.commit()
#     except sqlite3.DataError as error:
#         print(error)
#     finally:
#         close_connection(connection, cursor)
# publisher1 = publisher(None, "Baltos_lankos", "Tu_gali", "Josef_Murphy", 5000, 8)
# # create_publisher(publisher1)


#
#
# def get_publisher(publisher):
#     try:
#         connection, cursor = open_connection()
#         query = """SELECT * FROM publishers WHERE publisher_id = (?) OR publisher_name = (?) OR book_name = (?) OR author = (?) OR
#                     printing_quantiy = (?) OR printing_price = (?)"""
#         parameters = (publisher.publisher_id, publisher.publisher_name, publisher.book_name,
#                       publisher.author, publisher.printing_quantity, publisher.printing_price)
#
#         for row in cursor.execute(query, parameters):
#             print(row)
#
#     except sqlite3.DataError as error:
#         print(error)
#     finally:
#         close_connection(connection, cursor)
# # get_publisher(publisher1)
#
#
#
# def update_publisher(publisher):
#     try:
#         connection, cursor = open_connection()
#         query = """UPDATE publishers set publisher_name = 'zalios_lankos' WHERE publisher_id = (?) OR
#                     publisher_name = (?) OR book_name = (?) OR author = (?) OR
#                     printing_quantiy = (?) OR printing_price = (?) """
#         parameters = (publisher.publisher_id, publisher.publisher_name, publisher.book_name,
#                       publisher.author, publisher.printing_quantity, publisher.printing_price)
#         cursor.execute(query, parameters)
#         connection.commit()
#     except sqlite3.DataError as error:
#         print(error)
#     finally:
#         close_connection(connection, cursor)
#
# # update_publisher(publisher1)
# # get_publisher(publisher1)

#
# def delete_publisher(publisher):
#     try:
#         connection, cursor = open_connection()
#         query = """DELETE FROM publishers WHERE publisher_id = (?) OR
#                     publisher_name = (?) OR book_name = (?) OR author = (?) OR
#                     printing_quantiy = (?) OR printing_price = (?) """
#         parameters = (publisher.publisher_id, publisher.publisher_name, publisher.book_name,
#                       publisher.author, publisher.printing_quantity, publisher.printing_price)
#         cursor.execute(query, parameters)
#         connection.commit()
#     except sqlite3.DataError as error:
#         print(error)
#     finally:
#         close_connection(connection, cursor)
#
# # delete_publisher(publisher1)
# # get_publisher(publisher1)
#
# # filter by single field
# def filter_by_name(publisher):
#     book_name = publisher.book_name
#     return book_name

# def filter_by_field(publisher):
#     try:
#         publisher_name = filter_by_name(publisher)
#         connection, cursor = open_connection()
#
#         query = """SELECT * FROM publishers WHERE book_name = (?)"""
#
#         parameters = [publisher_name]
#         parameters_comperhesion = [paramter for paramter in parameters]
#
#         for i in cursor.execute(query, parameters_comperhesion):
#             print(i)
#
#     except sqlite3.DataError as error:
#         print(error)
#     finally:
#         close_connection(connection, cursor)
#
# filter_by_field(publisher1)