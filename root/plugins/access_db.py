
from root.config import Config
from root.plugins.database import Database

db = Database(Config.DB_URI, Config.SESSION_NAME)
