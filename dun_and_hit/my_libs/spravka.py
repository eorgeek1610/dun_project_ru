from colorama import Fore, Style


def spravka(player, enemy):
    print("1. Информация о игре")
    print("2. Информация о мечах")
    choice = int(input("Выберите: "))
    if choice == "1":
        print("\nПривет! Сейчас я быстро расскажу, что к чему.")
        print("Информация о героях: тут ты можешь узнать актуальную статистику твоего персонажа.")
        print("Начать игру: начинает игру. Потом расскажу подробней.")
        print("Магазин: тут ты можешь купить улучшения для героя или попытать удачу в кейсах.")
        print("Магазин: Улучшения и способности: тут ты можешь прикупить как и понятно из названия улучшения и способности.")
        print("Магазин: Кейсы и мечи: тут ты можешь попробывать выбить редкие мечи или коллекционировать менее редкие мечи.")
        print("Справочник: ты тут...")
        print("Инвентарь: тут ты можешь одеть, переплавить или удалить меч.")
        print("Инвентарь: Экипировка: что бы одеть меч выбери из списка твоего рюкзака его номер.")
        print("Инвентарь: Удаление: аналогично как и выше, только удаляет меч. ")
        print("Инвентарь: Переплавка: с каким-то шансом, ты можешь переплавить свой меч, и выбить меч лучше чем он (при переплавки меч удаляеться)")
        print("Остальное советую посмотреть самому :)")
    elif choice == "2":
        print(f"\n{Fore.BLUE}Меч война (Урон: 0.5){Style.RESET_ALL}")
        print(f'{Fore.GREEN}Ржавый меч (Урон: 1){Style.RESET_ALL}')
        print(f"{Fore.BLUE}Меч война (Урон: 1.5){Style.RESET_ALL}")
        print(f"{Fore.BLUE}Меч героя (Урон: 1; Здоровья: 1){Style.RESET_ALL}")
        print(f"{Fore.BLUE}Меч Тото (Здоровья: 4){Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}Меч Лолога (Урон: 1.5; Здоровья: 1) (Навсегда увеличивает прибыль после победы на 5){Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}Меч Грека (Урон: 0.5; Здоровья: 2){Style.RESET_ALL}")
        print(f'{Fore.MAGENTA}Меч Тутта (Урон: 2) (Навсегда увеличивает вместимость инвентаря на 2){Style.RESET_ALL}')
        print(f"{Fore.RED}АСТРО-МЕЧ (Урон: 3; Здоровья: 5){Style.RESET_ALL}")
        print(f"{Fore.YELLOW}ТОМЛИБ-МЕЧ (Урон: 2; Здоровья: 6){Style.RESET_ALL}")