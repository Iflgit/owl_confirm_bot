TOKEN = "677446399:AAFIYvMCcDIWvDSSvbThFGTdQSNuoay6_Mk"

import telebot
import random
from PIL import Image

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message: telebot.types.Message):
    if "start" in message.text:
        bot.reply_to(message, "Go-go-go!")
    else:
        bot.reply_to(message, "I can't help you :(")

@bot.message_handler(content_types=['sticker'])
def echo_sticker(message):
    file_info = bot.get_file(message.sticker.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    src='./'+file_info.file_path;
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
    im = Image.open(src).convert("RGB")
    im.save(src[:-4]+'png', 'png')
    photo = open(src[:-4]+'png', 'rb')
    bot.send_photo(message.chat.id, photo)
    bot.send_photo(message.chat.id, "FILEID")

@bot.message_handler(func=lambda message: True)
def echo_all(message: telebot.types.Message):
    if "одтвер" in message.text.lower():
        if random.random() < 0.7:
            bot.reply_to(message, 'Подтверждаю!')
        else:
            bot.reply_to(message, 'угу')



bot.polling()

