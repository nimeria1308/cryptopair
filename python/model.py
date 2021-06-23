from database import connect_db

LIST_CURRENCIES_SQL = "SELECT * FROM `currencies`"

LIST_PAIRS_SQL = "SELECT * FROM `pairs`"

INSERT_BID_SQL = "INSERT INTO `bids` (`id`, `pair`, `timestamp`, `bid`) VALUES (NULL, '%d', %s, '%f')"

FIND_PAIR_SQL = """
SELECT `pairs`.`id`, `pairs`.`kraken` FROM `pairs`
INNER JOIN `currencies` AS c1 ON `pairs`.`base`=`c1`.`id`
INNER JOIN `currencies` AS c2 ON `pairs`.`quote`=`c2`.`id`
WHERE `c1`.`name` = '%s' AND `c2`.`name` = '%s'
"""


def _model_list(conn, sql):
    with conn.cursor() as cursor:
        cursor.execute(sql)
        return {c[0]: c[1:] for c in cursor}


def model_get_currencies(conn):
    return _model_list(conn, LIST_CURRENCIES_SQL)


def model_get_pairs(conn):
    return _model_list(conn, LIST_PAIRS_SQL)


def model_find_pair(conn, base_name, quote_name):
    with conn.cursor() as cursor:
        sql = FIND_PAIR_SQL % (base_name, quote_name)
        cursor.execute(sql)
        return [c for c in cursor][0]


def model_insert_bid(conn, pair_id, bid, timestamp="current_timestamp()"):
    with conn.cursor() as cursor:
        insert_sql = INSERT_BID_SQL % (pair_id, timestamp, bid)
        cursor.execute(insert_sql)
