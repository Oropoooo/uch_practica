from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from keboard.keyboards import get_keyboard_1, get_keyboard_2, get_keyboard_3

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
    await message.answer('Привет, я твой первый ЭХО бот', reply_markup=get_keyboard_1())

@dp.message_handler(lambda message: message.text == 'Отправь фото кота')
async def button_1_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://avatars.mds.yandex.net/i?id=f5a0b9cde48e6bbc1a325bfe54df2551ddfc772a-5242334-images-thumbs&n=13', caption='Вот тебе кот')

@dp.message_handler(lambda message: message.text == 'Перейти на 2 клавиатуру')
async def button_2_click(message: types.Message):
    await message.answer('Здесь ты можешь попросить бота отправить фото собаки', reply_markup=get_keyboard_2())

@dp.message_handler(lambda message: message.text == 'Перейти на 3 клавиатуру')
async def button_2_click(message: types.Message):
    await message.answer('Здесь ты можешь попросить бота отправить фото капибары', reply_markup=get_keyboard_3())

@dp.message_handler(lambda message: message.text == 'Отправь фото собаки')
async def button_3_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://avatars.mds.yandex.net/i?id=da13ba9a33b19f613bd68bb3fdfaba08e83c017b-3922135-images-thumbs&n=13', caption='Вот тебе собака')

@dp.message_handler(lambda message: message.text == 'Перейти на 1 клавиатуру')
async def button_4_click(message: types.Message):
    await message.answer('Здесь ты можешь попросить бота отправить фото кота', reply_markup=get_keyboard_1())

@dp.message_handler(lambda message: message.text == 'Перейти на 3 клавиатуру')
async def button_2_click(message: types.Message):
    await message.answer('Здесь ты можешь попросить бота отправить фото капибары', reply_markup=get_keyboard_3())

@dp.message_handler(lambda message: message.text == 'Отправь фото капибары')
async def button_3_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://avatars.mds.yandex.net/get-entity_search/2389743/727454491/SUx182_2x', caption='Вот тебе капибара')

@dp.message_handler(lambda message: message.text == 'Перейти на 1 клавиатуру')
async def button_4_click(message: types.Message):
    await message.answer('Здесь ты можешь попросить бота отправить фото кота', reply_markup=get_keyboard_1())

@dp.message_handler(lambda message: message.text == 'Перейти на 2 клавиатуру')
async def button_2_click(message: types.Message):
    await message.answer('Здесь ты можешь попросить бота отправить фото собаки', reply_markup=get_keyboard_2())

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
