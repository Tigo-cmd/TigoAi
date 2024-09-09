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
# token for telegram bot
TELEGRAM_API_TOKEN = "7323343958:AAGp53vN3KP-nZJ_C5kDI_oBtoVQRoHQJjc"
TOKEN: Final = TELEGRAM_API_TOKEN
# initializes telegram bot to Username of the bot created by @botfather
BOT_USERNAME: Final = "@TigoGPTBot"

# context message to keep track of conversion more like a memory for the bot
messages = [{"role": "system",
             "content": "You are TelegramGPT your name is Tigo_bot,"
                        " a helpful telegram bot that is always concise and polite in its answers."
                        "you're an AI designed to assist with a wide range of tasks, "
                        "from answering questions and providing explanations to helping with creative writing, coding,"
                        " and research. you help with technical problems, brainstorming ideas, "
                        "and simple information, You're here to assist. Know how you can help today."}]


# function to handle starting the bot
async def Start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm Tigo_Bot, an AI designed to assist with a wide range of tasks,"
                                    "from answering questions and providing explanations to helping with creative "
                                    "writing,"
                                    "coding, and research. Whether you're looking for help with technical problems, "
                                    "brainstorming ideas,"
                                    " or simply need information, I'm here to assist. How can I help you today?")


# function to handle the Help response and command
async def Help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("How can I help you today?")


# function to handle the custom reply
async def Custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I'm Here To Help")


def response_handler(text: str):
    # if text:
    #     messages.append({"role": "user", "content": text})
    #     completion = client.chat.completions.create(
    #         model="llama3-70b-8192",
    #         messages=messages,
    #         temperature=1,
    #         max_tokens=1024,
    #         top_p=1,
    #         stream=False,
    #         stop=None,
    #     )
    #     Bot_reply: str = completion["choices"][0]["message"]["content"]
    #     messages.append({"role": "assistant", "content": Bot_reply})
    #     return Bot_reply
    if "hello" in text:
        return "Im good!!"
    else:
        return "Something went haywire"


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f"User ({update.message.chat.id} in {message_type}: {text}")

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = response_handler(new_text)
        else:
            return
    else:
        response: str = response_handler(text)

    print('Bot:', response)
    await update.message.reply_text(response)


async def error(update: Update, Context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {Context.error}")


# def text_message(update, context):
#     response = client.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=messages
#     )
#     ChatGPT_reply = response["choices"][0]["message"]["content"]
#     update.message.reply_text(text=f"*[Bot]:* {ChatGPT_reply}", parse_mode=telegram.ParseMode.MARKDOWN)


if __name__ == '__main__':
    print('Starting Bot......')
    app = Application.builder().token(TOKEN).build()

    # default commands
    app.add_handler(CommandHandler('start', Start_command))
    app.add_handler(CommandHandler('help', Help_command))
    app.add_handler(CommandHandler('Custom', Custom_command))

    # message commands
    app.add_handler(MessageHandler(filters.TEXT, message_handler))

    # Errors
    app.add_error_handler(error)

    # bot Polling
    print('Polling......')
    app.run_polling(poll_interval=3)
