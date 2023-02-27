from aiogram import executor
from uvicorn import run 


from mommy_bot.mommy_bot import dp
from admin.admin import app



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    run("main:app", port=8000, log_level="info")