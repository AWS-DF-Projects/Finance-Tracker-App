import sqlite3
def create_db():
    conn = sqlite3.connect("finance_tracker.db")
    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS accounts (
            first_name TEXT,
            last_name  TEXT,
            username   TEXT UNIQUE,
            password   TEXT,
            take_home  REAL
        )""")

    c.execute("""CREATE TABLE IF NOT EXISTS monthly_bills (
            user_id    REAL,
            bill_name  TEXT,
            bill_cost  REAL,
            bill_due_date  INTEGER,
            bill_tags  TEXT,
            is_active  TEXT,
            year       INTEGER
        )""")

    c.execute("""CREATE TABLE IF NOT EXISTS monthly_expenditures (
            user_id   TEXT,
            exp_name  TEXT,
            exp_cost  INTEGER,
            exp_tags  TEXT,
            exp_month INTEGER,
            exp_year  INTEGER
        )""")

    conn.commit()
    conn.close()