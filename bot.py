import telebot
from telebot import types
import parser



my_bot_token="1986132658:AAHwJAeYJv1IgD7_rN-4Dps9LPN0rAzh1LE"
bot=telebot.TeleBot(my_bot_token)
@bot.message_handler(commands=['c_sharp'])
def sharp_handler(message):
    sh_markup=types.ReplyKeyboardMarkup()
    button1=types.KeyboardButton('Основы')
    button2=types.KeyboardButton('ADO.NET')
    button3=types.KeyboardButton('ASP.NET')
    button4=types.KeyboardButton('Другое')

    sh_markup.add(button1,button2,button3,button4)
    bot.send_message(message.chat.id,"Что именно вы хотите изучать на C#?",reply_markup=sh_markup)
    bot.register_next_step_handler(message,send_materials)

def send_materials(message):
    main_materials_markup=types.InlineKeyboardMarkup()
    butt1=types.InlineKeyboardButton(text="Для чего нужен Шарп",url="https://habr.com/ru/company/vdsina/blog/522934/")
    main_materials_markup.add(butt1)
    if message.text=="Основы":
        bot.send_message(message.chat.id,"Приятного изучения!", reply_markup=main_materials_markup)


bot.polling()
# def get_text_messages(message):
#     if message.text=="C#":
#         bot.send_message(message.from_user.id,"Материалы по С#")
#     elif message.text=="Python":
#         bot.send_message(message.from_user.id,"Материалы по Python")
#     else:
#         bot.send_message(message.from_user.id,"Непонятно, что вы хотите")

#bot.polling(none_stop=True, interval=0)
