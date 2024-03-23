import os
import sys
import time
import telebot
from telebot import types
from config import BOT_TOKEN, CHANNEL_ID, ADMIN_ID, MEDIA_FOLDER

bot = telebot.TeleBot(BOT_TOKEN)

def exception_message(message):
    markup = types.InlineKeyboardMarkup()
    stop_button = types.InlineKeyboardButton("Stop", callback_data='stop')
    markup.add(stop_button)
    bot.send_message(ADMIN_ID, message, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def stop_callback(call):
    bot.send_message(ADMIN_ID, "Stopped")
    sys.exit()

def new_post(artist):
  try:
      print('posting...')
      for filename in os.listdir(MEDIA_FOLDER):
          if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
              filepath = os.path.join(MEDIA_FOLDER, filename)
              with open(filepath, 'rb') as photo:
                  bot.send_photo(CHANNEL_ID, photo, caption=f'#{artist}')

              os.remove(filepath)
              break

  except Exception as e:
      exception_message(e)