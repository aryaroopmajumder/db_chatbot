"""llama_model.py: service init """

__author__ = "Aryaroop Majumder"

import os
import logging
from dotenv import load_dotenv
import ollama

load_dotenv()


class LlamaModel:
    def __init__(self):
        try:
            logging.debug("Entering LlamaModel")
            model = os.getenv("OLLAMA_MODEL")
            logging.debug(os.getenv("OLLAMA_MODEL"))
            print(os.getenv("OLLAMA_MODEL"))
            ollama.chat()
        except ollama.ResponseError as e:
            print('Error:', e.error)
            if e.status_code == 404:
                logging.error("Error as there is no model within")
                # ollama.pull(model)
