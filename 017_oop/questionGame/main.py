from question import Question
from gameData import question_data

question_bank = []

for i in range(len(question_data)):
    question_dict = question_data[i]
    question_bank.append(Question(question_dict["text"], question_dict["answer"]))
