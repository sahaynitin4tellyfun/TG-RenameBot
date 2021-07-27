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

import numpy
import pyrogram
import os
from PIL import Image
import time
from pyrogram import Client,filters
from ..ffmpeg import generate_screen_shots, cult_small_video
from ..access_db import db
from pyrogram.types import InlineKeyboardMarkup,InlineKeyboardButton, Message 
from root.config import Config
from root.messages import Translation
from root.utils.database import *
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
  elif update.data == "show":
    thumb_image_path = Config.DOWNLOAD_LOCATION + "/thumb/" + str(update.from_user.id) + ".jpg"
    msgg = await bot.send_message("**👀 Getting Your Thumbnail...**",True)
    if not os.path.exists(thumb_image_path):
        mes = await thumb(update.from_user.id)
        if mes is not None:
            msgg = await bot.get_messages(update.chat.id, mes.msg_id)
            await msgg.download(file_name=thumb_image_path)
            thumb_image_path = thumb_image_path
        else:
            thumb_image_path = None

    if thumb_image_path is None:
        try:
            await msgg.edit_text("**😰 Oops... No Thumbnail found for you in Database...!**")
        except:
              pass               
    else:
        try:
           await msgg.delete()

        except:
            pass
        await bot.send_photo(
        photo=thumb_image_path,
        caption="__**👀 Your Permanent Thumbnail... 👆🏻**__",
        reply_markup=InlineKeyboardMarkup([[
          InlineKeyboardButton("🗑️ Delete Thumbnail..!", callback_data="delete")]])
    )
  elif update.data == "delete":
    download_location = Config.DOWNLOAD_LOCATION + "/thumb/" + str(update.from_user.id)
    try:
        os.remove(download_location + ".jpg")
        await del_thumb(update.from_user.id)
    except:
        pass
    await update.answer("🗑️ Custom Thumbnail Deleted Successfully...!", show_alert=True)
    await update.message.delete()
  elif update.data == "close":
    await update.message.delete()
    await update.message.reply_to_message.delete()
    
@Client.on_message(filters.command("help") & filters.private  & filters.user(Config.AUTH)) 
async def help_user(c,m, cb=False):
  if not cb:
    s=await m.reply_text("**__👀 Processing...__**", True)
  await s.edit(Translation.HELP_USER, reply_markup=HELP_BUTTONS, disable_web_page_preview=True)
  if cb:
    return await m.message.edit(Translation.HELP_USER, reply_markup=HELP_BUTTONS, disable_web_page_preview=True)
    
@Client.on_message(filters.command("about") & filters.private  & filters.user(Config.AUTH))
async def about_user(c,m, cb=False):
  if not cb:
    s=await m.reply_text("**__👀 Processing...__**", True)
  await s.edit(Translation.ABOUT_USER, reply_markup=ABOUT_BUTTONS, disable_web_page_preview=True)
  if cb:
    return await m.message.edit(Translation.ABOUT_USER, reply_markup=ABOUT_BUTTONS, disable_web_page_preview=True)
    
@Client.on_message(filters.command("start") & filters.private & filters.user(Config.AUTH))
async def start_msg(c,m, cb=False):
    if not cb:
      s=await m.reply_text("**__👀 Processing...__**", True)
    await s.edit(Translation.START_TEXT.format(m.from_user.mention), reply_markup=START_BUTTONS, disable_web_page_preview=True)
    if cb:
      return await m.message.edit(Translation.START_TEXT.format(m.from_user.mention), reply_markup=START_BUTTONS, disable_web_page_preview=True)
    
##else:
    ##s=await m.reply_text("**__👀 Processing...__**", True)
    ##await s.edit_text(text="**Sorry {}, I'm a File Renamer Bot but you can't access me....! Only [Ravi Teja](https://t.me/MeRaviTeja) can access me... \n\n__😏 You can too create your personal bots, Contact [Here](https://t.me/Animesh941)\n🤖 Coded By [Animesh Verma](https://t.me/Animesh941)__**".format(m.from_user.mention), 
                      ##reply_markup=InlineKeyboardMarkup([[
                        ##InlineKeyboardButton("⚙ Create Your Bot 🤖", url="https://t.me/Animesh941")]]), disable_web_page_preview=True)

    
@Client.on_message(filters.command(["generate_ss", "screenshot"]) & filters.private)
async def screenshot(c,m):
  caption = f"**__© Coded By @AVBotz ❤️__**"
  await m.message.edit("**📝 Okay..! Generating Screenshots...**")
  generate_ss_dir = f"{Config.DOWN_PATH}/{str(m.from_user.id)}"
  list_images = await generate_screen_shots(path, generate_ss_dir, 9, duration)
  if list_images is None:
    await m.message.edit("**Failed to get Screenshots!**")
    await asyncio.sleep(0)
  else:
    await m.message.edit("**Generated Screenshots Successfully!**\n**Now Uploading them...**")
    photo_album = list()
    
  if list_images is not None:
    i = 0
    for image in list_images:
      if os.path.exists(str(image)):
        if i == 0:
          photo_album.append(InputMediaPhoto(media=str(image), caption=caption))
        else:
          photo_album.append(InputMediaPhoto(media=str(image)))
          i += 1
          print(photo_album)
          await bot.send_media_group(
            chat_id=m.from_user.id,
            media=photo_album
          )
          
@Client.on_message(filters.command(["generate_sample", "sample"]) & filters.private)
async def sample(c,m):
  if duration >= 15:
    await m.message.edit("**Now Generating Sample Video...**")
    sample_vid_dir = f"{Config.DOWN_PATH}/{m.from_user.id}/"
    ttl = int(duration*10 / 100)
    sample_video = await cult_small_video(
      video_file=path,
      output_directory=sample_vid_dir,
      start_time=ttl,
      end_time=(ttl + 10),
      format_=FormtDB.get(m.from_user.id)
            )
    if sample_video is None:
      await m.message.edit("**Failed to Generate Sample Video!**")
      await asyncio.sleep(0)
    else:
      await m.message.edit("**Successfully Generated Sample Video!**\n**Now Uploading it...**")
      sam_vid_duration = 5
      sam_vid_width = 100
      sam_vid_height = 100
      try:
        metadata = extractMetadata(createParser(sample_video))
        if metadata.has("duration"):
          sam_vid_duration = metadata.get('duration').seconds
        if metadata.has("width"):
          sam_vid_width = metadata.get("width")
        if metadata.has("height"):
          sam_vid_height = metadata.get("height")
      except:
        await m.message.edit("**☹️ Sample Video File Corrupted!**")
        await asyncio.sleep(0)
        try:
          c_time = time.time()
          await c.send_video(
            chat_id=m.message.chat.id,
            video=sample_video,
            thumb=video_thumbnail,
            width=sam_vid_width,
            height=sam_vid_height,
            duration=sam_vid_duration,
            caption=caption,
            progress=progress_for_pyrogram,
            progress_args=("**Uploading Sample Video...**", m.message, c_time)
          )
        except Exception as sam_vid_err:
          print(f"Got Error While Trying to Upload Sample File:\n{sam_vid_err}")
          try:
            await m.message.edit("**Failed to Upload Sample Video!**")
            await asyncio.sleep(0)
          except:
            pass
    await m.message.delete(True)
        
@Client.on_message(filters.command("logs") & filters.private & filters.user(Config.AUTH))
async def log_msg(c,m):
  z =await m.reply_text("**👀 Processing...**", True)
  if os.path.exists("Log.txt"):
     await m.reply_document("Log.txt", True)
     await z.delete()
  else:
    await z.edit_text("**👀 Log file not found..!**")
