from database import connect_db, execute_sql


def _model_list(conn, sql):
    return {c[0]: c[1:] for c in execute_sql(conn, sql)}


def model_get_currencies(conn):
    return _model_list(conn, "SELECT * FROM `currencies`")


def model_get_pairs(conn):
    return _model_list(conn, "SELECT * FROM `pairs`")


def model_find_pair(conn, base_name, quote_name):
    sql = """
        SELECT `pairs`.`id`, `pairs`.`kraken` FROM `pairs`
        INNER JOIN `currencies` AS c1 ON `pairs`.`base`=`c1`.`id`
        INNER JOIN `currencies` AS c2 ON `pairs`.`quote`=`c2`.`id`
        WHERE `c1`.`name` = '%s' AND `c2`.`name` = '%s';
    """ % (base_name, quote_name)
    result = execute_sql(conn, sql)
    return [c for c in result][0]


def model_insert_bid(conn, pair_id, bid, timestamp="current_timestamp()"):
    sql = """
        INSERT INTO `bids` (`id`, `pair`, `timestamp`, `bid`)
        VALUES (NULL, '%d', %s, '%f');
    """ % (pair_id, timestamp, bid)
    execute_sql(conn, sql, True)
