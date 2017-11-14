from flask import Flask, render_template
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

app = Flask(__name__)

#english_bot = ChatBot("English Bot", storage_adapter="chatterbot.storage.SQLStorageAdapter")

#english_bot.set_trainer(ChatterBotCorpusTrainer)
#english_bot.train("chatterbot.corpus.english")

english_bot = ChatBot("Rao")
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

english_bot.set_trainer(ListTrainer)
english_bot.train(conversation)


@app.route("/")
def home():
    return render_template("chat_window.html")

@app.route("/get/<string:query>")
def get_raw_response(query):
    return str(english_bot.get_response(query))


if __name__ == "__main__":
    app.run(port=5002)
