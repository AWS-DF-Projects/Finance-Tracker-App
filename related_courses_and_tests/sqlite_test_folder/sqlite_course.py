import sqlite3

conn = sqlite3.connect('customer.db')                      # create a db with name
c = conn.cursor()                                          # create a cursor for doing things

# created table
c.execute("""CREATE TABLE IF NOT EXISTS customers (                      
        first_name TEXT,
        last_name TEXT,
        email TEXT UNIQUE
    )""")



def delete_record(delete_id):
    c.execute("DELETE from customers WHERE rowid = ?", (delete_id,))
    conn.commit()
delete_record(2)

def update_records(field_1, change, value):
    c.execute(f"""UPDATE  customers SET {field_1} = ? 
            WHERE rowid = ?
        """, (change, value,))
    conn.commit()
update_records("first_name","test 2", 2)
update_records("first_name","John", 1)

def select_search(field, value):
    c.execute(f"SELECT rowid, * FROM customers WHERE {field} = ?", (value,))
    if field == "rowid":
        value = int(value)
    items = c.fetchall()
    if not items:
        print("No results returned!!")
    else:
        print("")
        print(f"Search of {field}: {value}")
        print(f"{'ID':<2} | {'First Name':<10} | {'Last Name':<10} | {'Email'}")
        print("-" * 40)
        for i in items:
            print(f"{i[0]:<2} | {i[1]:<10} | {i[2]:<10} | {i[3]}")
        print("")
# select_search("last_name", "Doe")
# select_search("first_name", "June")
# select_search("rowid", 6)

def prim_key():
    c.execute("SELECT rowid, * FROM customers")
    items = c.fetchall()
    print(items)
    print("")
    print(f"{'ID':<2} | {'First Name':<10} | {'Last Name':<10} | {'Email'}")
    print("-" * 40)
    for i in items:
        print(f"{i[0]:<2} | {i[1]:<10} | {i[2]:<10} | {i[3]}")
# prim_key()

def print_database(items=None):
    if items is None:
        c.execute("SELECT rowid, * FROM customers")
        items = c.fetchall()

    print("")
    print(f"{'ID':<2} | {'First Name':<10} | {'Last Name':<10} | {'Email'}")
    print("-" * 45)
    for i in items:
        print(f"{i[0]:<2} | {i[1]:<10} | {i[2]:<10} | {i[3]}")

# print_database()

def execute_many():
    list_of_names_1 = [
        ["John",  "Doe",     "test1@test.com"],
        ["Mary",  "Smith",   "test2@test.com"],
        ["Kane",  "Wacker",  "test3@test.com"],
        ["Steve", "McQueen", "test4@test.com"],
        ["Brock", "Knock",   "test5@test.com"],
        ["June",  "Season",  "test6@test.com"],
    ]
    # c.executemany("INSERT OR IGNORE INTO customers VALUES (?,?,?)", list_of_names_1)


def loop_through():
    list_of_names_2 = [
        ["John", "Doe",    "test1@test.com"],
        ["Mary", "Smith",  "test2@test.com"],
        ["Kane", "Wacker", "test3@test.com"],
    ]
    for name in list_of_names_2:
        print(name)
        fn, ln, em = name
        c.execute("INSERT OR IGNORE INTO customers (first_name, last_name, email) VALUES (?,?,?)", (fn,ln,em))
        print("")

def order_db(field, direction):
    c.execute(f"SELECT rowid, * FROM customers ORDER BY {field} {direction}")
    items = c.fetchall()
    print_database(items)
# order_db("rowid", "DESC")
order_db("first_name", "")

                       # commit our command
# execute_many()
conn.commit()                                             # commit our command
conn.close()                                              # close connection


#---------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------  CHEAT CODES   ---------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------
# SQLite Data Types:
#   NULL     - Missing or undefined value (can store None / True / False)
#   TEXT     - Any string (names, emails, etc.)
#   INTEGER  - Whole numbers (e.g. age, ID)
#   REAL     - Decimal/float numbers (e.g. price, weight)
#   BLOB     - Binary Large Object (e.g. images, audio, files)

# Constraints (not types but good to remember):
#   PRIMARY KEY - Uniquely identifies a row (often auto-incremented)
#   UNIQUE      - Ensures all values in the column are different (e.g. email)
#   NOT NULL    - Column must have a value (can't be empty)
#   DEFAULT     - Sets a default value if none is given
#   CHECK       - Validates data (e.g. CHECK (age > 18))

# c.execute("INSERT INTO customers VALUES ('John', 'Doe', 'test@test.com')")
#---------------------------------------------------------------------------------------------------------------------------
#     email TEXT UNIQUE     →      OR IGNORE prevents the crash
# c.execute("INSERT OR IGNORE INTO customers (first_name, last_name, email) VALUES (?,?,?)", (fn,ln,em))
#
#---------------------------------------------------------------------------------------------------------------------------
# c.executemany("INSERT OR IGNORE INTO customers VALUES (?,?,?)", list_of_names_1)
#               this can do a list of values
#---------------------------------------------------------------------------------------------------------------------------
# 📥 FETCHING DATA METHODS
# c.execute("SELECT FROM customers")
# c.fetchone()   → Fetches the next single row (as a tuple)
#                 Use when expecting just one result (or looping one-by-one)

# c.fetchmany(size) → Fetches the next 'size' number of rows
#                     Great for large datasets to avoid loading everything at once

# c.fetchall()   → Fetches all remaining rows from the result set
#                 Be careful! Can eat a lot of memory with big tables
# print(c.fetchone()[1])    can select a index within a list/tuple
#---------------------------------------------------------------------------------------------------------------------------
# c.execute(f"SELECT rowid, * FROM customers WHERE {field} = ?", (value,))   # how to use variables
# c.execute(f"SELECT rowid, * FROM customers WHERE age >= 21)                # check a from or below like age
# c.execute(f"SELECT rowid, * FROM customers WHERE LIKE 'br%')               # partial search
#---------------------------------------------------------------------------------------------------------------------------
# c.execute(f"SELECT rowid, * FROM customers LIMIT BY rowid DESC 2 ORDER")    # limit the returns
#---------------------------------------------------------------------------------------------------------------------------
# c.execute("DROP TABLE customers")     to remove a table say after account closed
# conn.commit()
#---------------------------------------------------------------------------------------------------------------------------
