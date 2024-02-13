"""llama_model.py: service init """

__author__ = "Aryaroop Majumder"

import os
import logging
from dotenv import load_dotenv
import ollama

load_dotenv()

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class LlamaModel:

    def __init__(self):
        model = os.getenv("OLLAMA_MODEL")
        try:
            logger.debug("Loading Llama")
            question = input("Enter question: ")
            stream = ollama.chat(
                model=model,
                messages=[{'role': 'user', 'content': question}],
                stream=True,
            )
            for chunk in stream:
                print(chunk['message']['content'], end='', flush=True)

        except Exception as ex:
            logger.error(f"Error in LLamaModel: {ex.args}")

