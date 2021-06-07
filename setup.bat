@echo off

python -m pip install -U pip
python -m pip install -U mysql-connector-python flask
python setup_database.py
