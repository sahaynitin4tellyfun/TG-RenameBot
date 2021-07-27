'''
© Mrvishal2k2
RenameBot
This file is a part of mrvishal2k2 rename repo 
Dont kang !!!
© Mrvishal2k2
'''
import os 

class Config(object):
  APP_ID = int(os.environ.get("APP_ID", ""))
  API_HASH = os.environ.get("API_HASH", "")
  TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
  AUTH = list(set(int(x) for x in os.environ.get("AUTH", "1445283714").split()))
  #yyAUTH = [int(i) for i in os.environ.get('AUTH', '').split(' ')]
  DOWNLOAD_LOCATION = "./bot/DOWNLOADS"
  DB_URI = os.environ.get("DATABASE_URL", "")
  OWNER_ID = [int(i) for i in os.environ.get("OWNER_ID", "").split(" ")]
  OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "BotDunia")
  CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION",False)
  SESSION_NAME = os.environ.get("SESSION_NAME", "Rename-Bot")
  MONGODB_URI = os.environ.get("MONGODB_URI")
  DOWN_PATH = os.environ.get("DOWN_PATH", "./downloads")
