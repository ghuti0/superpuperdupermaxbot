import telebot
import random
token='5993447180:AAHcumKRv5U-zFIpDIPy-zRKm6zF3q5NLjk'
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"Привет!")
@bot.message_handler(commands=['questions'])
def questions_message(message):
  ans = ["Да", "Нет","Скорее всего да", "Скорее всего нет", "Не знаю"]
  x = random.randint(0,4)
  bot.send_message(message.chat.id, ans[x])
@bot.message_handler(commands=["menu"])
def button_message(message):
  markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True)
  item1 = telebot.types.KeyboardButton("Шар Судьбы")
  item2 = telebot.types.KeyboardButton("Котbки^^")
  markup.add(item1)
  markup.add(item2)
  bot.send_message(message.chat.id,"Выбери функцию:",reply_markup = markup)
@bot.message_handler(content_types='text')
def message_reply(message):
  if message.text=="Шар Судьбы":
    ans = ["Да", "Нет","Скорее всего да", "Скорее всего нет", "Не знаю"]
    x = random.randint(0,4)
    bot.send_message(message.chat.id, ans[x])
  if message.text == "Котbки^^":
    ans_stickers = ["CAACAgQAAxkBAAEI31tkVh-Hw9cEJc-i_jVlroumeANpNwAClwADzjkIDUAhLnyAYFYaLwQ", "CAACAgIAAxkBAAEI32JkVh_wPPM8CU3Ig-49pmn2fDDiQQACPRAAAqmeKUiw5wO1UgkLji8E","CAACAgQAAxkBAAEI32RkViAQygGL1gNv7ZucU2REl2LMswACOgADzjkIDWhSWwg2l986LwQ","CAACAgQAAxkBAAEI32ZkViIr0Lukq3mVfTBhWDMhSXxihQACsAADzjkIDRihrUgMN9XlLwQ","CAACAgQAAxkBAAEI32hkViIz06wP4NU4PfTu1OtfH2rTzAACigADzjkIDSRnEt5eoqsbLwQ","CAACAgQAAxkBAAEI32pkViJQUqOo1d90-cBGNEfTwtiIYgACPgADzjkIDT-gI_pS25AvLwQ","CAACAgQAAxkBAAEI32xkViJSaaDNWBiJUvhsoBBevLBXQQACPwADzjkIDcCW5JwCleAGLwQ","CAACAgQAAxkBAAEI325kViJm_FFAUGw3s-BTnTufzGm2cQACzQADzjkIDbRxz_ThOczfLwQ","CAACAgQAAxkBAAEI33BkViJoRp2_0a2NfL3kpiGk_azAmQACngADzjkIDU-BtaoXSL-RLwQ", "CAACAgQAAxkBAAEI33JkViJ0ISSzQJAMUC6OvTYpFIbrTQACMgADzjkIDTESJa2euMyOLwQ","CAACAgQAAxkBAAEI33RkViKDFj-lFuUWDDV6nH1caylAhwACkgADzjkIDSZ--VFHU0GtLwQ","CAACAgQAAxkBAAEI33ZkViKGFqk4IiQj3sBCwQ4W5YL-zAACjgADzjkIDZHmq1EAAeXnmy8E"]
    x2 = random.randint(0,11)
    bot.send_sticker(message.chat.id, ans_stickers[x2])
bot.infinity_polling()
