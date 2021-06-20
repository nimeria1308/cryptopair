import sys

from database import create_db, delete_db, connect_db
from ohlcvt import ohclvt_parse_file, ohclvt_insert_entries
from model import model_find_pair

csv_tables = [
    ("ohlcvt/ETHAUD_1440.csv",    "eth",     "aud"),
    ("ohlcvt/ETHCAD_1440.csv",    "eth",     "cad"),
    ("ohlcvt/ETHCHF_1440.csv",    "eth",     "chf"),
    ("ohlcvt/ETHEUR_1440.csv",    "eth",     "eur"),
    ("ohlcvt/ETHGBP_1440.csv",    "eth",     "gbp"),
    ("ohlcvt/ETHJPY_1440.csv",    "eth",     "jpy"),
    ("ohlcvt/ETHUSDT_1440.csv",   "eth",     "usdt"),
    ("ohlcvt/ETHUSD_1440.csv",    "eth",     "usd"),
    ("ohlcvt/ETHXBT_1440.csv",    "eth",     "btc"),
    ("ohlcvt/USDTAUD_1440.csv",   "usdt",    "aud"),
    ("ohlcvt/USDTCAD_1440.csv",   "usdt",    "cad"),
    ("ohlcvt/USDTCHF_1440.csv",   "usdt",    "chf"),
    ("ohlcvt/USDTEUR_1440.csv",   "usdt",    "eur"),
    ("ohlcvt/USDTGBP_1440.csv",   "usdt",    "gbp"),
    ("ohlcvt/USDTJPY_1440.csv",   "usdt",    "jpy"),
    ("ohlcvt/USDTUSD_1440.csv",   "usdt",    "usd"),
    ("ohlcvt/XBTAUD_1440.csv",    "btc",     "aud"),
    ("ohlcvt/XBTCAD_1440.csv",    "btc",     "cad"),
    ("ohlcvt/XBTCHF_1440.csv",    "btc",     "chf"),
    ("ohlcvt/XBTEUR_1440.csv",    "btc",     "eur"),
    ("ohlcvt/XBTGBP_1440.csv",    "btc",     "gbp"),
    ("ohlcvt/XBTJPY_1440.csv",    "btc",     "jpy"),
    ("ohlcvt/XBTUSDT_1440.csv",   "btc",     "usdt"),
    ("ohlcvt/XBTUSD_1440.csv",    "btc",     "usd"),
    ("ohlcvt/XRPAUD_1440.csv",    "xrp",     "aud"),
    ("ohlcvt/XRPCAD_1440.csv",    "xrp",     "cad"),
    ("ohlcvt/XRPETH_1440.csv",    "xrp",     "eth"),
    ("ohlcvt/XRPEUR_1440.csv",    "xrp",     "eur"),
    ("ohlcvt/XRPGBP_1440.csv",    "xrp",     "gbp"),
    ("ohlcvt/XRPJPY_1440.csv",    "xrp",     "jpy"),
    ("ohlcvt/XRPUSDT_1440.csv",   "xrp",     "usdt"),
    ("ohlcvt/XRPUSD_1440.csv",    "xrp",     "usd"),
    ("ohlcvt/XRPXBT_1440.csv",    "xrp",     "btc"),
]

if "delete" in sys.argv:
    delete_db()
else:
    existed_before = create_db()

    if not existed_before:
        # insert data into newly created database
        with connect_db() as conn:
            for csv in csv_tables:
                filename, base, quote = csv
                pair = model_find_pair(conn, base, quote)
                entries = ohclvt_parse_file(filename)
                print("Inserting %d entries into %s:%d" %
                      (len(entries), pair[1], pair[0]))
                ohclvt_insert_entries(conn, pair, entries)
