import datetime
import json
import time
import urllib.request

from database import connect_db
from model import model_get_pairs, model_insert_bid

UPDATE_INTERVAL_SECONDS = 15

URL = "https://api.kraken.com/0/public/Ticker?pair="


def fetch_data(pairs):
    url = URL + ",".join(pairs.values())
    # print(url)
    with urllib.request.urlopen(url) as response:
        json_response = json.load(response)
        error = json_response["error"]
        if error:
            raise Exception("Bad response: %s" % error)

        return json_response["result"]


def update_data(conn, pairs):
    data = fetch_data(pairs)

    for id, pair in pairs.items():
        #  'XXRPXXBT': {'a': ['0.000025600', '6969', '6969.000'],
        #               'b': ['0.000025590', '38954', '38954.000'],
        bid = data[pair]["b"][0]
        bid = float(bid)
        model_insert_bid(conn, id, bid)

    conn.commit()


def update_db():
    with connect_db() as conn:
        pairs = {}
        for key, value in model_get_pairs(conn).items():
            pairs[key] = value[2]  # pair ID -> kraken string

        update_data(conn, pairs)


print("Updating every %s s" % UPDATE_INTERVAL_SECONDS)

while True:
    print("Fetching new data at %s" % datetime.datetime.now().time())
    try:
        update_db()
    except Exception as e:
        print("Warning: %s" % e)

    time.sleep(UPDATE_INTERVAL_SECONDS)
