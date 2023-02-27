#import 
from random import choice
from logging import basicConfig, INFO 

from aiogram import Bot, Dispatcher, types, executor

from db.creare_list_facts import all_f as facts
from .config import TOKEN


#loging 
basicConfig(level=INFO)

#API 
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


#start and help
@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    #Добавляем кнопку
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Факт")
    markup.add(item1)
    await message.reply('Нажми:\nФакт\nдля получения факта о маме',  reply_markup=markup)


@dp.message_handler(commands=["help"])
async def start(message: types.Message):
    await message.reply('Я могу отпралять факты о маме')


#admin
@dp.message_handler(commands=["admin"])
async def test_commands(message: types.Message): 
    admin_button = types.InlineKeyboardButton(text="admin", url="http://127.0.0.1:8000/home")
    add_adm_btt = types.InlineKeyboardMarkup().add(admin_button)
    await message.answer('Нажми на кнопку для перехода', reply_markup=add_adm_btt)


#body
@dp.message_handler(content_types=["text"])
async def handle_text(message: types.Message):
    if message.text.strip() == 'Факт':
        await message.reply(choice(facts)[1], reply=False)

    else:
        await message.reply('Такой команды нет', reply=False)

    


