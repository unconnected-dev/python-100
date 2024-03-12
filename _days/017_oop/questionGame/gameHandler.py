class GameHandler:

    def __init__(self, question_bank) -> None:
        self.question_number = 0
        self.question_bank = question_bank
        self.score = 0
        pass

    def getCurrentQuestion(self) -> str:
        return f"Q{self.question_number + 1}: {self.question_bank[self.question_number].getQuestion()} (True/False)?: "
    

    def checkAnswer(self, user_answer) -> bool:
        return self.question_bank[self.question_number].getAnswer().lower() == user_answer.lower()
    

    def askQuestion(self):
        user_answer = input(self.getCurrentQuestion()).lower()
        print(f"The correct answer was {self.question_bank[self.question_number].getAnswer()}")

        if self.checkAnswer(user_answer) == True:
            print("You were right")
            self.incrementScore()
        else:
            print("You were wrong")
        
        print(f"Current Score: {self.score}/{self.question_number + 1}")
        print("\n")

        if self.stillHasQuestions() == True:
            self.incrementQuestionNumber()


    def stillHasQuestions(self) -> bool:
        return self.question_number < len(self.question_bank)
    

    def incrementQuestionNumber(self) -> None:
        self.question_number += 1
    

    def incrementScore(self) -> None:
        self.score += 1


    def resetGame(self) -> None:
        self. score = 0
        self.question_number = 0


    def getFinalScore(self) -> str:
        return f"{self.score} / {self.question_number}"