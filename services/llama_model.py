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
            logger.debug("Entering LlamaModel")
            logger.debug(f"Model selected is : {os.getenv('OLLAMA_MODEL')}")
            ollama.chat()
        except ollama.ResponseError as e:
            # print('Error:', e.error)
            if e.status_code == 404:
                logger.error("Error as there is no model within")
                ollama.pull(model)
