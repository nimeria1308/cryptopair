@echo off

echo Installing Python modules
python -m pip --quiet install --upgrade pip
python -m pip --quiet install --upgrade mysql-connector-python flask

echo Setting up database
python python\setup_database.py
