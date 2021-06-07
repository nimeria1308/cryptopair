from database import connect_db

LIST_PAIRS_SQL = r"SELECT `id`, `kraken` FROM `pairs`"

INSERT_BID_SQL = r"INSERT INTO `bids` (`id`, `pair`, `timestamp`, `bid`) VALUES (NULL, '%d', current_timestamp(), '%f')"


def model_get_pairs(conn):
    with conn.cursor() as cursor:
        cursor.execute(LIST_PAIRS_SQL)
        return {c[0]: c[1] for c in cursor}


def model_insert_bid(conn, pair_id, bid):
    with conn.cursor() as cursor:
        insert_sql = INSERT_BID_SQL % (pair_id, bid)
        cursor.execute(insert_sql)
