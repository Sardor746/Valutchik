from aiogram import Bot, Dispatcher, types, executor
import requests
import json

btn = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btn.add("USD-UZS", "RUB-UZS", "EURO-UZS", "CNY-UZS", "WON-UZS", "DINOR-UZS")

token = "Bot_token"
bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def first(message: types.Message):
    p = open("images/pht.jpg", "rb")
    await bot.send_photo(message.chat.id, p, caption="<b>Assalomu-alaykum, ValyutaBotga Hush Kelibsiz!</b>", reply_markup=btn, parse_mode="HTML")


@dp.message_handler(content_types=["text"])
async def second(message: types.Message):
    global inputs, outputs, result, photo, caps
    text = message.text
    if text == "USD-UZS":
        inputs = "USD"
        outputs = "UZS"
        photo = open("images/USD-UZS.jpg", "rb")
        caps = "Dollorning Sumdagi qiymati 👇"
    if text == "RUB-UZS":
        inputs = "RUB"
        outputs = "UZS"
        photo = open("images/RUB-UZS.jpg", "rb")
        caps = "Rublning Sumdagi qiymati 👇"
    if text == "EURO-UZS":
        inputs = "EUR"
        outputs = "UZS"
        photo = open("images/EUR-UZS.jpg", "rb")
        caps = "Euorning Sumdagi qiymati 👇"
    if text == "CNY-UZS":
        inputs = "CNY"
        outputs = "UZS"
        photo = open("images/CNY-UZS.jpg", "rb")
        caps = "Yenaning Sumdagi qiymati 👇"
    if text == "DINOR-UZS":
        inputs = "KWD"
        outputs = "UZS"
        photo = open("images/DINOR-UZS.jpg", "rb")
        caps = "Dinorning Sumdagi qiymati 👇"
    if text == "WON-UZS":
        inputs = "KRW"
        outputs = "UZS"
        photo = open("images/WON-UZS.jpg", "rb")
        caps = "Vonning Sumdagi qiymati 👇"

    url = "https://v6.exchangerate-api.com/v6/5f6d43916b52307ea4aed1f3/latest/" + inputs
    responses = requests.get(url)
    rest = json.loads(responses.text)
    result = rest["conversion_rates"]["UZS"]
    if message.text.isdigit():
        can = int(message.text) * result
        await bot.send_photo(message.chat.id, photo, caption=caps)
        await bot.send_message(message.chat.id, round(can, 4))


if __name__ == '__main__':
    executor.start_polling(dp)
