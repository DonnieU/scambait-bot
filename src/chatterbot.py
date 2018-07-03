!pip install chatterbot

# -*- coding: utf-8 -*-
from chatterbot import ChatBot
#from settings import TWITTER
import logging


'''
This example demonstrates how you can train your chat bot
using data from Twitter.

To use this example, create a new file called settings.py.
In settings.py define the following:

TWITTER = {
    "CONSUMER_KEY": "my-twitter-consumer-key",
    "CONSUMER_SECRET": "my-twitter-consumer-secret",
    "ACCESS_TOKEN": "my-access-token",
    "ACCESS_TOKEN_SECRET": "my-access-token-secret"
}
'''

# Comment out the following line to disable verbose logging
logging.basicConfig(level=logging.INFO)


chatbot = ChatBot(
    "TwitterBot",
    logic_adapters=[
        "chatterbot.logic.BestMatch"],
    #input_adapter="chatterbot.input.TerminalAdapter",
    input_adapter="chatterbot.input.VariableInputTypeAdapter",
    output_adapter="chatterbot.output.TerminalAdapter",
    database="./twitter-database.db",
    twitter_consumer_key="",
    twitter_consumer_secret="",
    twitter_access_token_key="",
    twitter_access_token_secret="",
    trainer= 'chatterbot.trainers.TwitterTrainer', random_seed_word="india"
)



output=chatbot.train()

chatbot.logger.info('Trained database generated successfully!')


# Get a response to an input statement
chatbot.get_response("india")