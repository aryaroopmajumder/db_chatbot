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
            stream = ollama.chat(
                model=model,
                messages=[{'role': 'user', 'content': 'Why is the sky blue?'}],
                stream=False,
            )

        except Exception as ex:
            logger.error(f"Error in LLamaModel: {ex.args}")

