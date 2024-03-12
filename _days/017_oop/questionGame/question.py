class Question:
    def __init__(self, question, answer) -> None:
        self.question = question
        self.answer = answer

    def getQuestion(self) -> str:
        return f"{self.question}"
    
    def getAnswer(self) -> str:
        return f"{self.answer}"
    
    def getQuestionAnswer(self) -> str:
        return f"{self.question} : {self.answer}"