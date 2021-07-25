'''
RenameBot
Thanks to Spechide Unkle as always for the concept  ♥️
This file is a part of mrvishal2k2 rename repo 
Dont kang !!!
© Mrvishal2k2
'''
import os
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log = logging.getLogger(__name__)

from pyrogram import Client,filters
from pyrogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from root.config import Config
from root.messages import Translation
import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

START_BUTTONS = InlineKeyboardMarkup(
  [[
    InlineKeyboardButton("🆘 Help", callback_data="help"),
    InlineKeyboardButton("📝 About", callback_data="about"),
    InlineKeyboardButton("🔐 Close", callback_data="close")
   ]])

HELP_BUTTONS = InlineKeyboardMarkup(
  [[
    InlineKeyboardButton("🏡 Home", callback_data="home"),
    InlineKeyboardButton("📝 About", callback_data="about"),
    InlineKeyboardButton("🔐 Close", callback_data="close")
   ]])

ABOUT_BUTTONS = InlineKeyboardMarkup(
  [[
    InlineKeyboardButton("😎 Developer 😎", url="https://t.me/Animesh941")
   ],[
    InlineKeyboardButton("🏡 Home", callback_data="home"),
    InlineKeyboardButton("🔐 Close", callback_data="close")
   ]])

@Client.on_callback_query()
async def cb_handler(bot, update):
  if update.data == "home":
    await update.message.edit_text(
      text=Translation.START_TEXT.format(update.from_user.mention),
      reply_markup=START_BUTTONS,
      disable_web_page_preview=True
    )
  elif update.data == "help":
    await update.message.edit_text(
      text=Translation.HELP_USER,
      reply_markup=HELP_BUTTONS,
      disable_web_page_preview=True
    )
  elif update.data == "about":
    await update.message.edit_text(
      text=Translation.ABOUT_USER,
      reply_markup=ABOUT_BUTTONS,
      disable_web_page_preview=True
    )
  elif update.data == "close":
    await update.message.delete()
    await update.message.reply_to_message.delete()
    
@Client.on_message(filters.command("help"))
async def help_user(c,m):
  await m.reply_text(Translation.HELP_USER, reply_markup=HELP_BUTTONS, disable_web_page_preview=True, quote=True)
  
@Client.on_message(filters.command("about"))
async def about_user(c,m):
  await m.reply_text(Translation.ABOUT_USER, reply_markup=ABOUT_BUTTONS, disable_web_page_preview=True, quote=True)
  
@Client.on_message(filters.command("start"))
async def start_msg(c,m):
  await m.reply_text(Translation.START_TEXT.format(m.from_user.mention), quote=True, reply_markup=START_BUTTONS, disable_web_page_preview=True)
  
@Client.on_message(filters.command("logs") & filters.private & filters.user(Config.OWNER_ID))
async def log_msg(c,m):
  z =await m.reply_text("**👀 Processing...**", True)
  if os.path.exists("Log.txt"):
     await m.reply_document("Log.txt", True)
     await z.delete()
  else:
    await z.edit_text("**👀 Log file not found..!**")
