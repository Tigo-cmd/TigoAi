#!/usr/bin/env python3
########################################################################
#       AN OPEN/GROQ AI CLI INTEGRATION MY NWALI UGONNA EMMANUEL
#       GITHUB: https://github.com/Tigo-cmd/TigoAi
#       All contributions are welcome!!!
#       yea lets do some coding!!!!!!!!!!!!
#########################################################################
"""Source classes to handle all GroqAPI functionalities and trained models
                        BY Nwali Ugonna Emmanuel
 """

from __future__ import annotations
from groq import Groq
import subprocess
import os
import requests
from dotenv import load_dotenv


class TigoGroq:
    """this handles Api tokens and requests
    this class clones the GROQ init function and re-initializes the arguments
    so that when the class is called it set every functionality needed for the model to run
    """
    client = None
    _Apikey = os.getenv("GROQ_API_KEY")
    context: list[dict[str, str]] = [
        {"role": "system", "content": "You are CLI Assistant your name is Tigo,"
                                      "you're a helpful Bot that is always concise and polite in its "
                                      "answers."
                                      "you're an AI designed to assist with a wide range of tasks, "
                                      "from answering questions and providing explanations to "
                                      "creative writing, coding, debug files, create files, find solution with"
                                      " and research. you help with technical problems, brainstorming ideas, "
                                      "and simple information, You're here to assist. you will help this user"}
    ]

    def __init__(
            self,
    ) -> None:
        """Constructor initialized at first call"""
        if self._Apikey is None:
            """
            checks if the apikey is present in the environment variable
             else loads from env file using python-loadenv
            """
            load_dotenv()
        self.client = Groq()

    def get_context(self, context: str):
        """

        :param context: tracks conversations and context with users
        :return: nothing
        """
        pass

    async def get_response_from_ai(self, message: str):
        """returns response from the AI and messages to print to standard output"""
        self.context.append({"role": "user", "content": message})
        completion = self.client.chat.completions.create(
            model="llama3-70b-8192",
            messages=self.context,
            temperature=1,
            max_tokens=1024,
            top_p=1,
            stream=True,
            stop=None,
        )
        reply: str = ""
        for chunk in completion:
            reply += chunk.choices[0].delta.content or ""
        self.context.append({"role": "assistant", "content": reply})
        return reply

    def store_retrive_context(self, filename: str):
        """

        :param filename:
        :return:
        """
        pass
