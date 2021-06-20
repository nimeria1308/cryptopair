import datetime
import sys

from database import connect_db
from model import model_find_pair, model_insert_bid


def ohclvt_parse_file(filename):
    entries = []

    with open(filename) as f:
        for line in f:
            timestamp, value = line.strip().split(',')[:2]
            timestamp = datetime.datetime.fromtimestamp(int(timestamp))
            value = float(value)
            entries.append([timestamp, value])

    return entries


def ohclvt_insert_entries(conn, pair, entries):
    for timestamp, value in entries:
        model_insert_bid(conn, pair[0], value,
                         timestamp.strftime("'%Y-%m-%d %H:%M:%S'"))

    conn.commit()

def main():
    _, filename, base, quote = sys.argv

    entries = ohclvt_parse_file(filename)

    with connect_db() as conn:
        pair = model_find_pair(conn, base, quote)
        print("inserting %d entries into %s:%d" % (len(entries), pair[1], pair[0]))
        ohclvt_insert_entries(conn, pair, entries)

main()
