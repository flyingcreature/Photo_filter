import os


def validate_path():
    path = input("Введите путь к файлу: ")
    while not os.path.exists(path):
        path = input("Файл не найден, попробуйте ещё раз: ")
    return path


def validate_value(message: str, valid_values: list[str]) -> str:
    value = input(message).lower()
    while value not in valid_values:
        value = input(f"Вы ввели неверное значение. Выберите из {valid_values}: ").lower()
    return value


def validate_file_name() -> str:
    while True:
        file_name = input("Куда сохранить: ")
        file_parts = file_name.split(".")
        if len(file_parts) >= 2 and file_parts[-1] in ["jpg", "png", "jpeg"]:
            return file_name
        else:
            print("Некорректное имя файла. Добавьте в конце формат .jpg или .png ,или .jpeg")
