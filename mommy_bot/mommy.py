#import 
import asyncio
import logging
import config
from aiogram import Bot, Dispatcher, types, executor
from random import choice

#loging 
logging.basicConfig(level=logging.INFO)


#unpacking file and path to file
path_facts = r"C:\mom\my_mommy.txt"

facts_open = open(path_facts, 'r', encoding='UTF-8')
facts = facts_open.read().split('\n')
facts_open.close()


#API 
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)


#start and help
@dp.message_handler(commands=["start"])
async def start(message, res=False):
        #Добавляем кнопку
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Факт")
        markup.add(item1)
        await message.answer('Нажми:\nФакт\nдля получения факта о маме',  reply_markup=markup)


@dp.message_handler(commands=["help"])
def start(messange):
        messange.answer('Я могу отпралять: \n факты о маме')


#body
@dp.message_handler(content_types=["text"])
async def handle_text(message):
    if message.text.strip() == 'Факт' :
            response = choice(facts)
    else: 
        response = 'Такой команды нет'
    # Отсылаем юзеру сообщение в его чат
    await message.answer(response)

    
# Запускаем бота
if __name__ == '__main__':
    executor.start_polling(dp)

