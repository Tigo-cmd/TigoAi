#!/usr/bin/env python3
"""MAIN ENTRY OF THE PROGRAM HANDLES ALL FUNCTIONALITIES FOR THE AI"""

########################################################################
#       AN OPEN AI INTEGRATION MY NWALI UGONNA EMMANUEL
#       GITHUB: https://github.com/Tigo-cmd/TigoAi
#       All contributions are welcome!!!
#       yea lets do some coding!!!!!!!!!!!!
#########################################################################
"""
####################################################################################################################
Copyright (c) 2024 Emmanuel Tigo, All Rights Reserved
Originally By Nwali Ugonna Emmanuel (Emmanuel Tigo)
###################################################################################################################
"""

from TigoAi import client
from telegram.ext import Updater, MessageHandler, Filters
import telegram

openai.api_key = "<YOUR_OPENAI_API_KEY>"
TELEGRAM_API_TOKEN = "<YOUR_TELEGRAM_BOT_TOKEN>"

messages = [{"role": "system", "content": "You are TelegramGPT, a helpful telegram bot that is always concise and polite in its answers."}]


def text_message(update, context):
    messages.append({"role": "user", "content": update.message.text})
    response = client.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    update.message.reply_text(text=f"*[Bot]:* {ChatGPT_reply}", parse_mode=telegram.ParseMode.MARKDOWN)
    messages.append({"role": "assistant", "content": ChatGPT_reply})


updater = Updater(TELEGRAM_API_TOKEN, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), text_message))
updater.start_polling()
updater.idle()


