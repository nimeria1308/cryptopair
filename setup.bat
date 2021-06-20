@echo off

echo Installing Python modules
python -m pip --quiet install --upgrade pip
python -m pip --quiet install --upgrade mysql-connector-python flask

echo Setting up database
python python\setup_database.py

echo Inserting historical entries
python python\ohlcvt.py "ohlcvt\ETHAUD_1440.csv"    eth     aud
python python\ohlcvt.py "ohlcvt\ETHCAD_1440.csv"    eth     cad
python python\ohlcvt.py "ohlcvt\ETHCHF_1440.csv"    eth     chf
python python\ohlcvt.py "ohlcvt\ETHEUR_1440.csv"    eth     eur
python python\ohlcvt.py "ohlcvt\ETHGBP_1440.csv"    eth     gbp
python python\ohlcvt.py "ohlcvt\ETHJPY_1440.csv"    eth     jpy
python python\ohlcvt.py "ohlcvt\ETHUSDT_1440.csv"   eth     usdt
python python\ohlcvt.py "ohlcvt\ETHUSD_1440.csv"    eth     usd
python python\ohlcvt.py "ohlcvt\ETHXBT_1440.csv"    eth     btc
python python\ohlcvt.py "ohlcvt\USDTAUD_1440.csv"   usdt    aud
python python\ohlcvt.py "ohlcvt\USDTCAD_1440.csv"   usdt    cad
python python\ohlcvt.py "ohlcvt\USDTCHF_1440.csv"   usdt    chf
python python\ohlcvt.py "ohlcvt\USDTEUR_1440.csv"   usdt    eur
python python\ohlcvt.py "ohlcvt\USDTGBP_1440.csv"   usdt    gbp
python python\ohlcvt.py "ohlcvt\USDTJPY_1440.csv"   usdt    jpy
python python\ohlcvt.py "ohlcvt\USDTUSD_1440.csv"   usdt    usd
python python\ohlcvt.py "ohlcvt\XBTAUD_1440.csv"    btc     aud
python python\ohlcvt.py "ohlcvt\XBTCAD_1440.csv"    btc     cad
python python\ohlcvt.py "ohlcvt\XBTCHF_1440.csv"    btc     chf
python python\ohlcvt.py "ohlcvt\XBTEUR_1440.csv"    btc     eur
python python\ohlcvt.py "ohlcvt\XBTGBP_1440.csv"    btc     gbp
python python\ohlcvt.py "ohlcvt\XBTJPY_1440.csv"    btc     jpy
python python\ohlcvt.py "ohlcvt\XBTUSDT_1440.csv"   btc     usdt
python python\ohlcvt.py "ohlcvt\XBTUSD_1440.csv"    btc     usd
python python\ohlcvt.py "ohlcvt\XRPAUD_1440.csv"    xrp     aud
python python\ohlcvt.py "ohlcvt\XRPCAD_1440.csv"    xrp     cad
python python\ohlcvt.py "ohlcvt\XRPETH_1440.csv"    xrp     eth
python python\ohlcvt.py "ohlcvt\XRPEUR_1440.csv"    xrp     eur
python python\ohlcvt.py "ohlcvt\XRPGBP_1440.csv"    xrp     gbp
python python\ohlcvt.py "ohlcvt\XRPJPY_1440.csv"    xrp     jpy
python python\ohlcvt.py "ohlcvt\XRPUSDT_1440.csv"   xrp     usdt
python python\ohlcvt.py "ohlcvt\XRPUSD_1440.csv"    xrp     usd
python python\ohlcvt.py "ohlcvt\XRPXBT_1440.csv"    xrp     btc
