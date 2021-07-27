
from root.config import Config
from ..database import Database

db = Database(Config.DB_URI, Config.SESSION_NAME)
