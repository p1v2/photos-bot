import os

from pony.orm import *


# Establishes connection with DB
db = Database()
db.bind('postgres', os.environ["DATABASE_URL"])
