
from root.config import Config
from root.plugins.database import Database

db = Database(Config.MONGODB_URI, Config.SESSION_NAME)
