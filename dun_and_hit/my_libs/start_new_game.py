import time


def new_game(player):
    print("Выбери уровень сложность:")
    time.sleep(0.5)
    print("Легкий")
    time.sleep(0.5)
    print("или")
    time.sleep(0.5)
    print("Сложный")
    time.sleep(0.5)
    print("?")
    time.sleep(0.5)
    choice = input("Что выберем: ").upper()
    if choice == "ЛЕГКИЙ":
        print("\nОк, тебе зачислиться + 10 монет в начале игры :)")
        player.money += 10
    elif choice == "СЛОЖНЫЙ":
        print("\nОк, ты начнешь игру с 0 балансом.")
    else:
        print("\nКх, мне все-таки пришлось добавить 2 строчки кода для тебя, мой друг 🤮🤮🤮")
        player.money -= 100
        player.health -= 2
        player.damage -= 1
