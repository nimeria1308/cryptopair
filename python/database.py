import mysql.connector

HOST = "localhost"
USER = "root"
PASSWORD = ""
DATABASE = "cryptopair"
DATABASE_INIT = "cryptopair.sql"

# https://stackoverflow.com/questions/29772337/python-mysql-connector-unread-result-found-when-using-fetchone


def connect(database=DATABASE):
    return mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=database,
        buffered=True)


def __db_exists(conn):
    with conn.cursor() as cursor:
        cursor.execute("SHOW DATABASES")
        return (DATABASE,) in cursor


def create_db():
    with connect(None) as conn:
        if not __db_exists(conn):
            with open(DATABASE_INIT) as f:
                init_sql = f.read()

            with conn.cursor() as cursor:
                res = cursor.execute(init_sql, multi=True)
                # run through the queries
                for q in res:
                    pass

            conn.commit()


def delete_db():
    with connect(None) as conn:
        if __db_exists(conn):
            with conn.cursor() as cursor:
                cursor.execute("DROP DATABASE %s" % DATABASE)
