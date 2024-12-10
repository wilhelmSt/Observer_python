from notifier.observer import Observer

class User(Observer):
    def __init__(self, username):
        self.username = username

    def update(self, message):
        print(f"Usuário {self.username} recebeu a mensagem: {message}")
