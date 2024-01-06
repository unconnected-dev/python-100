from question import Question
from gameData import question_data
from gameHandler import GameHandler

question_bank = []

for i in range(len(question_data)):
    question_dict = question_data[i]
    question_bank.append(Question(question_dict["text"], question_dict["answer"]))

gameHandler = GameHandler(question_bank)

while gameHandler.stillHasQuestions():
    gameHandler.askQuestion()