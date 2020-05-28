#from chatterbot.corpus import Corpus
#from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot 
from chatterbot.comparisons import levenshtein_distance
from chatterbot.response_selection import get_first_response 
from chatterbot.trainers import ChatterBotCorpusTrainer

logic_adapters = [
  'chatterbot.logic.MathematicalEvaluation',
  #'chatterbot.logic.TimeLogicAdapter',
  {
    "import_path": "chatterbot.logic.BestMatch",
    "statement_comparison_function": levenshtein_distance,
    "response_selection_method": get_first_response
  }
]

bot=ChatBot(
  'meuChat',
  #logic_adapters=logic_adapters
)


bot.set_trainer(ChatterBotCorpusTrainer)
bot.train("chatterbot.corpus.portuguese")

while True:
  quest = input('Você:')
  response = bot.get_response(quest)

  print('Bot:',response)