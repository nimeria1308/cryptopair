import datetime
import json
import time
import urllib.request

from database import connect

UPDATE_INTERVAL_SECONDS = 15

URL = "https://api.kraken.com/0/public/Ticker?pair="

LIST_PAIRS = r"SELECT `id`, `kraken` FROM `pairs`"
INSERT_PAIR = r"""
INSERT INTO `bids` (`id`, `pair`, `timestamp`, `bid`) VALUES (NULL, '%d', current_timestamp(), '%f')
"""


def get_pairs(conn):
    with conn.cursor() as cursor:
        cursor.execute(LIST_PAIRS)
        return {c[0]: c[1] for c in cursor}


def fetch_data(conn, pairs):
    url = URL + ",".join(pairs.values())
    with urllib.request.urlopen(url) as response:
        json_response = json.load(response)
        error = json_response["error"]
        if error:
            raise Exception("Bad response: %s" % error)

        return json_response["result"]


def update_data(conn, pairs):
    data = fetch_data(conn, pairs)
    for id, pair in pairs.items():
        #  'XXRPXXBT': {'a': ['0.000025600', '6969', '6969.000'],
        #               'b': ['0.000025590', '38954', '38954.000'],
        bid = data[pair]["b"][0]
        bid = float(bid)
        with conn.cursor() as cursor:
            insert_sql = INSERT_PAIR % (id, bid)
            cursor.execute(insert_sql)
    conn.commit()


def update_db():
    with connect() as conn:
        pairs = get_pairs(conn)
        update_data(conn, pairs)


while True:
    print("Updating every %s s" % UPDATE_INTERVAL_SECONDS)

    print("Fetching new data at %s" % datetime.datetime.now().time())
    try:
        update_db()
    except Exception as e:
        print("Warning: %s" % e)

    time.sleep(UPDATE_INTERVAL_SECONDS)
