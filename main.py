from notifier.observable import Observable
from subscribers.user import User

def main():
    news_channel = Observable()

    user1 = User("João")
    user2 = User("Maria")
    user3 = User("Pedro")

    news_channel.add_observer(user1)
    news_channel.add_observer(user2)
    news_channel.add_observer(user3)

    news_channel.notify_observers("Nova notícia: Padrão de Observador implementado!")

    news_channel.remove_observer(user1)
    news_channel.notify_observers("Nova notícia: Apenas os inscritos ativos recebem notificações.")

if __name__ == "__main__":
    main()
