import sys

from database import create_db, delete_db

if "delete" in sys.argv:
    delete_db()
else:
    create_db()
