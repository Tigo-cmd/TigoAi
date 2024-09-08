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
from typing import Final
from TigoAi import client
from TigoAi import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# loads .env files for Api Tokens
load_dotenv()
# initializes telegram bot
BOT_USERNAME: Final = "@TigoGPTBot"

# context message to keep track of converstion more like a memory for the bot
messages = [{"role": "system",
             "content": "You are TelegramGPT your name is Tigo_bot,"
                        " a helpful telegram bot that is always concise and polite in its answers."
                        "you're an AI designed to assist with a wide range of tasks, "
                        "from answering questions and providing explanations to helping with creative writing, coding,"
                        " and research. you help with technical problems, brainstorming ideas, "
                        "and simple information, You're here to assist. Know how you can help today."}]

# function to handle starting the bot
async def Start_command(update: Update, Context: ContextTypes.DEFAULT_TYPE):
    await Update.message.reply_text("Hello! I'm Tigo_Bot, an AI designed to assist with a wide range of tasks,"
                                    "from answering questions and providing explanations to helping with creative "
                                    "writing,"
                                    "coding, and research. Whether you're looking for help with technical problems, "
                                    "brainstorming ideas,"
                                    " or simply need information, I'm here to assist. How can I help you today?")

# function to handle the Help response and command
async def Help_command(update: Update, Context: ContextTypes.DEFAULT_TYPE):
    await Update.message.reply_text("How can I help you today?")


# function to handle the custom reply
async def Custom_command(update: Update, Context: ContextTypes.DEFAULT_TYPE)
    await Update.message.reply_text("I'm Here To Help")


def response_handler(text: str) -> str:
    return

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
