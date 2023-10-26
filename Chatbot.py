from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chat bot named Charlie
chatbot = ChatBot('hi')

trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train(
    "chatterbot.corpus.english"
)






def vastus(vastus):
    response = chatbot.get_response(vastus)
    return response