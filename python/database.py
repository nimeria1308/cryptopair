import mysql.connector

HOST = "localhost"
USER = "root"
PASSWORD = ""
DATABASE = "cryptopair"
DATABASE_INIT = "cryptopair.sql"

# https://stackoverflow.com/questions/29772337/python-mysql-connector-unread-result-found-when-using-fetchone


def connect_db(database=DATABASE):
    return mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=database,
        buffered=True)


def execute_sql(conn, sql, skip_result=False):
    with conn.cursor() as cursor:
        cursor.execute(sql)
        if not skip_result:
            return cursor.fetchall()


def __db_exists(conn):
    result = execute_sql(conn, "SHOW DATABASES")
    return (DATABASE,) in result


def create_db():
    with connect_db(None) as conn:
        if not __db_exists(conn):
            with open(DATABASE_INIT) as f:
                init_sql = f.read()

            with conn.cursor() as cursor:
                res = cursor.execute(init_sql, multi=True)
                # run through the queries
                for q in res:
                    pass

            conn.commit()

            return False

    return True


def delete_db():
    with connect_db(None) as conn:
        if __db_exists(conn):
            execute_sql(conn, "DROP DATABASE %s" % DATABASE, True)
