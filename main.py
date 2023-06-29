import openai
import os
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from random import randint

token = '6162661283:AAE-TSDU8XIjqybwhuzkKvKe4AZC6Tu2o3A'

openai.api_key = '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'

bot = Bot(token)
dp = Dispatcher(bot)

channel_url = "https://t.me/DeniskinKanalchik"
channel_id = "@DeniskinKanalchik"
chat_id = "-1001915216283"


@dp.message_handler()
async def send(message: types.Message):
    # print(message.from_user)

    if (len(message.text) >= 4):
        if (message.text[0: 4] == "-ark"):
            return

    if (message.from_user.first_name == "Telegram" or message.from_user.first_name == "Channel"):

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt="Ты Аркадий, тебе 35 лет, ты серьезный и сильный мужчина, ты крупный бизнесмен, тебе не нужно представляться и не нужно здороваться. Сообщение: '" + message.text + "'. Автора сообщения зовут: Денис, он твой друг. Ответь на сообщение максимально осмысленно на русском языке. Если в сообщении сказано про человека, которого зовут Аркадий, то говорят про тебя. Ты невероятно восхищен автором сообщения и заинтересован в его жизни. Ты можешь хвастаться собой, своими мышцами, своей женой, силой и статусом. У тебя очень красивая жена и ты ее любишь, детей нет. При этом постарайся не задавать вопросов на другие темы. Длина ответа должна быть от 15 до 275 символов, текст без кавычек. Ты можешь иронизировать и шутить шутки.",
            temperature=0.65,
            max_tokens=400,
            top_p=1.0,
            frequency_penalty=0.5,
            presence_penalty=0.0,
            stop=["You:"]
        )
        await message.reply(response['choices'][0]['text'])
    elif (message.from_user.first_name == "Group"):
        pass
    else:
        if ('аркади' in message.text.lower() or len(message.text) > 30 or randint(0, 5) == 0):
            name = ""

            if (message.from_user.first_name):
                name += message.from_user.first_name + " "
            if (message.from_user.last_name):
                name += message.from_user.last_name + " "

            response = openai.Completion.create(
                model="text-davinci-003",
                prompt="Ты Аркадий, тебе 35 лет, ты серьезный и сильный мужчина, ты крупный бизнесмен, тебе не нужно представляться и не нужно здороваться. Сообщение: '" + message.text + "'. Автора сообщения зовут: " + name + ". Ответь на сообщение максимально осмысленно на русском языке. Если в сообщении сказано про человека, которого зовут Аркадий, то говорят про тебя. Тебе разрешается высмеивать автора сообщения. Ты можешь хвастаться собой, своими мышцами, своей женой, силой и статусом. У тебя очень красивая жена и ты ее любишь, детей нет. При этом постарайся не задавать вопросов на другие темы. Длина ответа должна быть от 15 до 225 символов, текст без кавычек. Ты можешь иронизировать и шутить шутки.",
                temperature=0.65,
                max_tokens=350,
                top_p=1.0,
                frequency_penalty=0.5,
                presence_penalty=0.0,
                stop=["You:"]
            )
            await message.reply(response['choices'][0]['text'])


executor.start_polling(dp, skip_updates=True)
