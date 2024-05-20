from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN

bot = Bot(token= TELEGRAM_TOKEN)
dp = Dispatcher(bot)

async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command='/start', description='Команда для того, чтобы запустить бота'),
        types.BotCommand(command='/help', description='Команда для того, чтобы узнать, с чем может помочь наш бот'),
        types.BotCommand(command='/kirill', description='Команда для того, чтобы узнать полное имя Кирилла'),
        types.BotCommand(command='/denis', description='Команда для того, чтобы узнать полное имя Дениса'),
        types.BotCommand(command='/igor', description='Команда для того, чтобы узнать полное имя Игоря')
    ]

    await bot.set_my_commands(commands)

@dp.message_handler(commands= 'start')
async def start(message: types.Message):
    await message.answer('Привет, я твой первый ЭХО бот')

@dp.message_handler(commands= 'help')
async def start(message: types.Message):
    await message.reply('Я могу помочь тебе с .....')

@dp.message_handler(commands= 'kirill')
async def start(message: types.Message):
    await message.answer('Полное имя Хайруллин Кирилл Михайлович')

@dp.message_handler(commands= 'denis')
async def start(message: types.Message):
    await message.answer('Полное имя Копылов Денис Иванович')

@dp.message_handler(commands= 'igor')
async def start(message: types.Message):
    await message.answer('Полное имя Верзаков Игорь Иванович')

@dp.message_handler()
async def start(message: types.Message):
    await message.answer(message.text)

async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True, on_startup = on_startup)
