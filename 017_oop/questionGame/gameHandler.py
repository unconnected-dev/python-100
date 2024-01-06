class GameHandler:

    def __init__(self, question_bank) -> None:
        self.question_number = 0
        self.question_bank = question_bank
        pass

    def getCurrentQuestion(self) -> str:
        return f"Q{self.question_number + 1}: {self.question_bank[self.question_number].getQuestion()} (True/False)?: "
    
    def askQuestion(self):
        input(self.getCurrentQuestion()).lower()
        self.question_number += 1
        
    def stillHasQuestions(self) -> bool:
        return self.question_number < len(self.question_bank)