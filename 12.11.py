is_running = True

while is_running:
    raw = input("Программа для проверки ZeroDivisionError. Выход или Продолжить?\n")

    if raw == "Выход":
        is_running = False
        print("Программа завершила работу.")

    elif raw == "Продолжить":
        x = int(input("Делимое: "))
        y = int(input("Делитель: "))
        z = 0

        try:
            z = x/y
            print("Программа работает штатно:", z)
            
        except ZeroDivisionError:
            z = 0
            print("Исклюение: деление на 0! То есть будет:", z)

    else:
        print("Неизвестная команда.")