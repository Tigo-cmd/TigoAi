#!/usr/bin/env python3
########################################################################
#       AN OPEN/GROQ AI INTEGRATION MY NWALI UGONNA EMMANUEL
#       GITHUB: https://github.com/Tigo-cmd/TigoAi
#       All contributions are welcome!!!
#       yea lets do some coding!!!!!!!!!!!!
#########################################################################
"""Source classes to handle all OpenAi functionalities and trained models
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
    Apikey  = os.getenv("API_KEY")
    content: str = ""
    context = [
        {"role": f"{...}", "message": f"{content}"}
    ]
    def __init__(
            self,
            *,
            api_key,
            base_url,
            timeout,
            max_retries,
            default_headers,
            default_query,
            http_client,
            _strict_response_validation: bool = False,
    ) -> None:
        """Constructor initialized at first call"""
        if TigoGroq.Apikey is None:
            load_dotenv()
        else:
            self.GROQ_API_KEY = TigoGroq.Apikey
        self.apikey = api_key
        self.base_url = base_url
        self.timeout = timeout
        self.default_headers = default_headers
        self.max_retries = max_retries
        self.default_query = default_query
        self.http_client = http_client
        self.client = Groq(TigoGroq.Apikey)
    def get_response_from_ai(self, message, temp=1, max_token=1024, Top_p=1, Stream=True, stopper=None ):
        """gets response from the AI and messages to print to standard output"""
        self.completion = self.client.chat.completions.create(
            model="llama3-70b-8192",
            messages= [
                {
                    "role": f"{...}",
                    "message": f"{message}"
                }
            ]

            self.temperature=temp,
            self.max_tokens=max_token,
            self.top_p=Top_p,
            self.stream=Stream,
            self.stop = stopper
        )
        return [chunck.choices[0].delta.content for chunck in self.completion]
