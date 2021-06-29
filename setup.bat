@echo off

echo Installing Python modules
python -m pip --quiet install mysql-connector-python flask

echo Setting up database
python python\setup_database.py
