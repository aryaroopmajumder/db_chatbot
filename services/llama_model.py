"""llama_model.py: service init """

__author__ = "Aryaroop Majumder"

import os
from dotenv import load_dotenv
import ollama

load_dotenv()



class LlamaModel:
    def __init__(self):
        try:
            model = os.getenv("OLLAMA_MODEL")
            ollama.chat()
        except ollama.ResponseError as e:
            print('Error:', e.error)
            if e.status_code == 404:
                # ollama.pull(model)
