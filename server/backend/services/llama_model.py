"""llama_model.py: service init """

__author__ = "Aryaroop Majumder"

import os
import logging
from dotenv import load_dotenv
from langchain_community.llms import Ollama

load_dotenv()

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class LlamaModel:

    def __init__(self):
        model = os.getenv("OLLAMA_MODEL")
        try:
            logger.debug("Loading Llama")
            llm = Ollama(model=model)
            llm.invoke("Tell me a joke")

        except Exception as ex:
            logger.error(f"Error in LLamaModel: {ex.args}")

