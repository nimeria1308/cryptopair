from database import execute_sql


def _model_list(conn, sql):
    result = {}

    sql_result = execute_sql(conn, sql)
    # print(sql)
    # print(sql_result)

    for item in sql_result:
        key = item[0]
        values = item[1:]
        result[key] = values

    # print(result)
    return result


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
    return result[0]


def model_insert_bid(conn, pair_id, bid, timestamp="current_timestamp()"):
    sql = """
        INSERT INTO `bids` (`id`, `pair`, `timestamp`, `bid`)
        VALUES (NULL, '%d', %s, '%f');
    """ % (pair_id, timestamp, bid)
    execute_sql(conn, sql, True)


def model_get_bids_by_year(conn, pair_id):
    sql = """
        SELECT AVG(bid) as bid, YEAR(`timestamp`) as year
        FROM cryptopair.bids
        WHERE pair = %d
        GROUP BY `year`
        ORDER BY `year`;
    """ % pair_id
    return execute_sql(conn, sql)


def model_get_bids_by_month(conn, pair_id, year):
    sql = """
        SELECT AVG(bid) as bid, MONTH(`timestamp`) as month
        FROM cryptopair.bids
        WHERE YEAR(`timestamp`) BETWEEN %d AND %d AND pair = %d
        GROUP BY `month`
        ORDER BY `month`;
    """ % (year, year+1, pair_id)
    return execute_sql(conn, sql)


def model_get_bids_by_day(conn, pair_id, year, month):
    sql = """
        SELECT AVG(bid) as bid, DAY(`timestamp`) as day
        FROM cryptopair.bids
        WHERE timestamp BETWEEN '%d-%d-01' AND DATE_ADD('%d-%d-01', interval 1 month) AND pair = %s
        GROUP BY `day`
        ORDER BY `day`;
    """ % (year, month, year, month, pair_id)
    return execute_sql(conn, sql)


def model_get_bids_realtime(conn, pair_id):
    sql = """
        SELECT bid, UNIX_TIMESTAMP(`timestamp`)
        FROM cryptopair.bids
        WHERE timestamp BETWEEN DATE_SUB(now(), interval 1 day) AND now() AND pair = %s
        ORDER BY timestamp;
    """ % (pair_id)
    return execute_sql(conn, sql)
