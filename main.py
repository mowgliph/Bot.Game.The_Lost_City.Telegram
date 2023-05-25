# API Telegram Bot 5994663798:AAG71TpWfx-jM4aFTJG1U97rURALLNOrnDA
# Api OPEN AI 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

import os
import openai
import aiogram
import keep_alive as alive

alive.keep_alive()

print("Loading The Lost City")

openai.api_key = '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'

response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Escribe el codigo en python de una calculadora",
    temperature=0.5,
    max_tokens=1024,
    top_p=1,
    frequency_penalty=0.0,
    presense_penalty=0.0
)

print(response.choise[0].text)