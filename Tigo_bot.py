#!/usr/bin/env python3
"""MAIN ENTRY OF THE PROGRAM HANDLES ALL FUNCTIONALITIES FOR THE AI"""

########################################################################
#       AN OPEN/GROQ AI TELEGRAM BOT INTEGRATION MY NWALI UGONNA EMMANUEL
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

"""
still trying to make enable Groq API differentiate and store different user context based on id
works more like session so that the AI model can work for each different user it communicates with
I hope it makes sense cause that's how it sounds in my head lol 😁😄
"""
# loads .env files for Api Tokens
load_dotenv()
# token for telegram bot
TELEGRAM_API_TOKEN = "7323343958:AAGp53vN3KP-nZJ_C5kDI_oBtoVQRoHQJjc"
TOKEN: Final = TELEGRAM_API_TOKEN
# initializes telegram bot to Username of the bot created by @botfather
BOT_USERNAME: Final = "@TigoGPTBot"
# USER_ID: int = 1131511127

# context message to keep track of conversion more like a memory for the bot
messages = [{"role": "system",
             "content": "You are TelegramGPT your name is Tigo_bot,"
                        " you're a helpful telegram bot that is always concise and polite in its answers."
                        "you're an AI designed to assist with a wide range of tasks, "
                        "from answering questions and providing explanations to helping with creative writing, coding,"
                        " and research. you help with technical problems, brainstorming ideas, "
                        "and simple information, You're here to assist. Know how you can help today."}]
backup_message = messages.copy()
# function to handle starting the bot

user_contexts = {}


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


def get_user_context(user_id: int):
    """
    Retrieves the context for a specific user. If the user is new, it initializes their context.
    """
    if user_id not in user_contexts:
        # Initialize context for the new user
        user_contexts[user_id] = [{"role": "system",
                                   "content": "You are TelegramGPT your name is Tigo_bot,"
                                              "you're a helpful telegram bot that is always concise and polite in its "
                                              "answers."
                                              "you're an AI designed to assist with a wide range of tasks, "
                                              "from answering questions and providing explanations to helping with "
                                              "creative writing, coding,"
                                              " and research. you help with technical problems, brainstorming ideas, "
                                              "and simple information, You're here to assist. Know how you can help "
                                              "today."}]
    return user_contexts[user_id]


def response_handler(user_id: int, text: str):
    """
       Handles the bot's response by interacting with the OpenAI API and maintaining the user-specific context.
      :param user_id: The ID of the user sending the message
      :param text: The text input by the user
      :return: The bot's response as a string
      """
    if text:
        messages = get_user_context(user_id)
        messages.append({"role": "user", "content": text})
        # Call The Api
        completion = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=messages,
            temperature=1,
            max_tokens=1024,
            top_p=1,
            stream=True,
            stop=None,
        )
        Bot_reply: str = ""
        # Combine the chunks of the response
        for chunk in completion:
            Bot_reply += chunk.choices[0].delta.content or ""
        # Append the bot's reply to the context
        messages.append({"role": "assistant", "content": Bot_reply})
        # Update the user's context in the dictionary
        user_contexts[user_id] = messages
        return Bot_reply
    else:
        return "Something went haywire"


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.chat.id
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f"User ({update.message.chat.id} in {message_type}: {text}")

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = response_handler(user_id, new_text)
        else:
            return
    else:
        response: str = response_handler(user_id, text)

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
