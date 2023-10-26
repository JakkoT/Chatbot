from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chat bot named Charlie
chatbot = ChatBot('hi')

trainer = ListTrainer(chatbot)

trainer.train([

])

# Get a response to the input text 'I would like to book a flight.'
vastus = input()
response = chatbot.get_response(vastus)

print(response)