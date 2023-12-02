from filters import filters
from PIL import Image
from validators import validate_path, validate_value, validate_file_name

menu = "Меню фильтров:\n"  # Сборка меню.
for filter in filters:
    menu += f"{filter}: {filters[filter]['name']}\n"
menu += "0: Выход"

print("Добро пожаловать в консольный фоторедактор\n")


finish = False
while not finish:
    path = validate_path()  # Ввод пользователя пути файла.
    img = Image.open(path).convert("RGB")  # Открытие файла

    print("\n" + menu + "\n")

    choice = int(validate_value("Выберите фильтр: ", ["0", "1", "2", "3", "4"]))  # Выбор фильтра
    if choice == 0:  # Выход из программы
        print("\nДо свидания!")
        finish = True

    else:  # Вывод описание фильтра
        print("\n" + filters[choice]["name"])
        print(filters[choice]["Description"])

        choice_2 = validate_value("\nПрименить фильтр к картинке? (Да/Нет): ",
                                  ["да", "нет"])  # Выбор пользователя применять ли фильтр
        if choice_2 == "да":
            filter = filters[choice]["class"]  # Изменение файла
            img = filter.apply_to_image(img)

            save_path = validate_file_name()

            img.save(save_path)  # Сохранение файла

            choice_3 = validate_value("\nЕщё раз? (Да/Нет): ", ["да", "нет"])  # Выбор пользователя о продолжении.
            if choice_3 == "нет":
                print("\nДо свидания!")
                finish = True