import sqlite3

def connect_crate(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn

def crate_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)
    return conn

def crate_new_students(conn, student):
    try:
        new_student = """INSERT INTO student (full_name, mark, hobby, is_merried ) VALUES (?, ?, ?, ?)"""
        cursor = conn.cursor()
        cursor.execute(new_student, student)
        conn.commit()
    except sqlite3.Error as e:
        print(e)
    return conn

def select_all_students(conn):
    try:
        all_stidents = """SELECT * FROM student"""
        cursor = conn.cursor()
        cursor.execute(all_stidents)
        row = cursor.fetchall()
        for rows in row:
            print(rows)
    except sqlite3.Error as e:
        print(e)

def select_students_by_mark(conn, limit):
    try:
        students_select_by_mark = ("""SELECT * FROM student WHERE mark >= ?""")
        cursor = conn.cursor()
        cursor.execute(students_select_by_mark, (limit,))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


def update_table_students(conn, students):
    try:
        update_student = """UPDATE student SET mark = ?, is_merried = ? WHERE id = ? """
        cursor = conn.cursor()
        cursor.execute(update_student, students)
        conn.commit()
    except sqlite3.Error as e:
        print(e)
    return conn

def delete_students(conn, id):
    try:
        delete_students = """DELETE FROM student WHERE id = ? """
        cursor = conn.cursor()
        cursor.execute(delete_students, (id,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)
    return conn




name_file_db = r'students.db'
crate_student_table = ("""
CREATE TABLE student (
id INTEGER PRIMARY KEY AUTOINCREMENT,
full_name VARCHAR(200) NOT NULL,
mark DOUBLE(10, 2) NOT NULL DEFAULT 0.00,
hobby TEXT DEFAULT NULL,
is_merried BOOLEAN DEFAULT FALSE
)
""")

connect = connect_crate(name_file_db)
if connect is not None:
    print('connected successfully!')
    # crate_table(connect, crate_student_table)
    # crate_new_students(connect, ('arman armanov', 99.18, 'run', True))
    # crate_new_students(connect, ('adel jakypov', 49.12, 'it', False))
    # crate_new_students(connect, ('brus li', 72.32, 'leg', True))
    # crate_new_students(connect, ('ip man', 12.75, 'fiqh', True))
    # crate_new_students(connect, ('joni dep', 65.19, 'kino', False))
    select_all_students(connect)
    # # select_students_by_mark(connect, 50)
    # update_table_students(connect, (11.18, False, 2))
    delete_students(connect, 3)
    print('___________')
    select_all_students(connect)
    print('done')
