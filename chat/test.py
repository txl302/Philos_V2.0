from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot("Philos")
chatbot.set_trainer(ChatterBotCorpusTrainer)

# Train based on the english corpus
chatbot.train("chatterbot.corpus.english")

# Get a response to an input statement
chatbot.get_response("Hello, how are you today?")

while True:
	ask = raw_input()
	response  =  chatbot.get_response(ask)
	print response
	