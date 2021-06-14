from database import connect_db

LIST_CURRENCIES_SQL = r"SELECT * FROM `currencies`"

LIST_PAIRS_SQL = r"SELECT * FROM `pairs`"

INSERT_BID_SQL = r"INSERT INTO `bids` (`id`, `pair`, `timestamp`, `bid`) VALUES (NULL, '%d', current_timestamp(), '%f')"


def _model_list(conn, sql):
    with conn.cursor() as cursor:
        cursor.execute(sql)
        return {c[0]: c[1:] for c in cursor}


def model_get_currencies(conn):
    return _model_list(conn, LIST_CURRENCIES_SQL)


def model_get_pairs(conn):
    return _model_list(conn, LIST_PAIRS_SQL)


def model_insert_bid(conn, pair_id, bid):
    with conn.cursor() as cursor:
        insert_sql = INSERT_BID_SQL % (pair_id, bid)
        cursor.execute(insert_sql)
