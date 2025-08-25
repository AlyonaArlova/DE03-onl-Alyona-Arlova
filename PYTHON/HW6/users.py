def register_user(name, age):
    if age.isdigit():
        age = int(age)
        if age < 18:
            print("Доступ ограничен")
        else:
            print(f"Добро пожаловать, {name}!")
    else:
        print("Возраст должен быть числом")
