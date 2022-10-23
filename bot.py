# pip install virtualenv
# pip install aiogram
# source.\env\bin\activate.bat

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import wikipedia

wikipedia.set_lang("ru")

TOKEN = "5717924054:AAFsZYUZzD6fcz8kkiiUmfdBCCrEdycDozQ"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# обработчик текстовых сообщений, который будет обрабатывать входящие команды /start и /help
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(msg: types.Message):
    await msg.answer(f'Привет, {msg.from_user.first_name}! Почитаем? Выбери /random для поиска статьи дня')


@dp.message_handler(commands=['random', 'no'])
async def send_article(msg: types.Message):
    random_article = wikipedia.random()
    page = wikipedia.page(random_article)
    global url
    url = page.url
    await msg.answer(f"{random_article}")
    await msg.answer(f'{wikipedia.summary(random_article)}')
    await msg.answer("Вы хотели бы прочитать эту статью? Выберите /yes чтобы почитать "
                     "или /random для поиска новой статьи дня")

@dp.message_handler(commands=['yes'])
async def send_article(msg: types.Message):
    await msg.answer(f'{url}')


@dp.message_handler(content_types=['text'])
async def get_text_messages(msg: types.Message):
   if msg.text.lower() == 'привет':
       await msg.answer('Привет!')
   else:
       await msg.answer('Не понимаю, что это значит.')


if __name__ == '__main__':
   executor.start_polling(dp)

