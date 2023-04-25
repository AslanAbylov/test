import sqlite3

def connect_sql(file_name):
    db = None
    try:
        db = sqlite3.connect(file_name)
    except sqlite3.Error as e:
        print(e)
    return db


def crate_table(db, subd_name):
    try:
        cursor = db.cursor()
        cursor.execute(subd_name)
    except sqlite3.Error as e:
        print(e)
    return db



def crate_new_product(db, product):
    new_product = """INSERT INTO product (product_title, price, quantity) VALUES (?, ?, ?)"""
    try:
        cursor = db.cursor()
        cursor.execute(new_product, product)
        db.commit()
    except sqlite3.Error as e:
        print(e)
    return db

def update_product_by_id(db, id):
    try:
        update_product = """UPDATE product SET quantity = ? WHERE id = ?"""
        cursor = db.cursor()
        cursor.execute(update_product, id)
        db.commit()
    except sqlite3.Error as e:
        print(e)
    return db

def delete_product(db, id):
    try:
        delete_product = """DELETE FROM product WHERE id = ?"""
        cursor = db.cursor()
        cursor.execute(delete_product, (id,))
        db.commit()
    except sqlite3.Error as e:
        print(e)
    return db

def select_product(db):
    try:
        select_product = """SELECT * FROM product"""
        cursor = db.cursor()
        cursor.execute(select_product)
        catch = cursor.fetchall()
        for row in catch:
            print(row)
    except sqlite3.Error  as e:
        print(e)
    return db

def select_by_price_and_quantity(db):
    try:
        select_product = """SELECT * FROM product WHERE price > 200 and quantity < 2"""
        cursor = db.cursor()
        cursor.execute(select_product)
        row = cursor.fetchall()
        for rows in row:
            print(rows)
        db.commit()
    except sqlite3.Error as e:
        print(e)
    return db


name_file_db = r'hv.db'
crate_products_table = """CREATE TABLE product 
(id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR(200) NOT NULL,
price DOUBLE(8,2) NOT NULL DEFAULT 0.00,
quantity INTEGER NOT NULL DEFAULT 0
)"""

connect = connect_sql(name_file_db)
if connect is not None:
    print('connected successfully!')
    # crate_table(connect, crate_products_table)
    # crate_new_product(connect, ('Красное яблоко', 100.32, 1))
    # crate_new_product(connect, ('Зеленное яблоко', 160.80, 2))
    # crate_new_product(connect, ('Желтое яблоко', 240.50, 3))
    # update_product_by_id(connect, (1000, 1))
    # delete_product(connect, 1)
    # select_product(connect)
    select_by_price_and_quantity(connect)
    print('Done')
