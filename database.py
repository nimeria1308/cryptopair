import mysql.connector

HOST = "localhost"
USER = "root"
PASSWORD = ""
DATABASE = "cryptopair"

# https://stackoverflow.com/questions/29772337/python-mysql-connector-unread-result-found-when-using-fetchone

# currency names are max 6 chars according to data from kraken
CREATE_TABLE = r"""
CREATE TABLE `%s`.`cryptopairs` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `from` CHAR(6) CHARACTER SET armscii8 COLLATE armscii8_general_ci NOT NULL,
    `to` CHAR(6) CHARACTER SET armscii8 COLLATE armscii8_general_ci NOT NULL,
    `timestamp` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `bid` DECIMAL(10.10) NOT NULL,
    PRIMARY KEY (`id`)
)
""" % DATABASE


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
            with conn.cursor() as cursor:
                cursor.execute("CREATE DATABASE %s" % DATABASE)
            with conn.cursor() as cursor:
                cursor.execute(CREATE_TABLE)


def delete_db():
    with connect(None) as conn:
        if __db_exists(conn):
            with conn.cursor() as cursor:
                cursor.execute("DROP DATABASE %s" % DATABASE)

# test


with connect(None) as db:
    print("connected")
    print(db)

delete_db()
delete_db()
create_db()
create_db()
