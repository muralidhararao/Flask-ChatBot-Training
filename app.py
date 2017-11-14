from flask import Flask, render_template
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

app = Flask(__name__)

#Chatbot object creation
english_bot = ChatBot("Rao")

#Custom conversation list
conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome.",
    "do you have boyfriend",
    "yes",
    "what is gold plan?",
    "lets explain about the gold plan.. are you clear about this?"
]

#set the type of trainer to chatbot
english_bot.set_trainer(ListTrainer)
#set the list for train
english_bot.train(conversation)

#Flask root
@app.route("/")
def home():
    return render_template("chat_window.html")

#Flask plan GET end point
@app.route("/get/<string:query>")
def get_raw_response(query):
    return str(english_bot.get_response(query))

#Application running port
if __name__ == "__main__":
    app.run(port=5002)
