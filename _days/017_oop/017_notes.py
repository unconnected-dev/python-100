#Basic Class
class User:
    
    def __init__(self, user_id, username) -> None:
        self.user_id = user_id
        self.username = username

    def details(self) -> str:
        return f"{self.user_id}, {self.username}"

newUser = User(1, "paul")
print(newUser.details())