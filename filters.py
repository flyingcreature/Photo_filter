from PIL import Image, ImageFilter


class Filter:
    """Базовый класс для создания фильтров"""

    def apply_to_pixel(self, r: int, g: int, b: int) -> tuple[int, int, int]:
        """
        Применяет фильтр пикселя
        :param r,g,b: цвет пикселя
        :return: новый цвет пикселя
        """
        raise NotImplementedError()
    def apply_stock(self):
        """Применяет встроенный фильтр к изображению."""
        raise NotImplementedError()


    def apply_to_image(self, img: Image.Image) -> Image.Image:
        """
        Применяет фильтр к изображению
        :param img:  исходное изображение
        :return: новое изображение
        """
        try:
            for i in range(img.width):
                for j in range(img.height):
                    r, g, b = img.getpixel((i, j))
                    new_pixel = self.apply_to_pixel(r, g, b)
                    img.putpixel((i, j), new_pixel)
            return img
        except NotImplementedError:
            img = img.filter(self.apply_stock())
            return img


class BlueFilter(Filter):
    """Фильтр, который накладывает на изображение синий цвет."""

    def apply_to_pixel(self, r: int, g: int, b: int) -> tuple[int, int, int]:
        r = 0
        g = 0
        b = min(255, int(b * 1))
        return r, g, b


class DarkFilter(Filter):
    """Фильтр, который делает изображение темнее"""

    def apply_to_pixel(self, r: int, g: int, b: int) -> tuple[int, int, int]:
        r = max(r - 100, 0 - 255)
        g = max(g - 100, 0 - 255)
        b = max(b - 100, 0 - 255)
        return r, g, b


class InverseFilter(Filter):
    """Фильтр, который инверсирует цвета изображения"""

    def apply_to_pixel(self, r: int, g: int, b: int) -> tuple[int, int, int]:
        r = 255 - r
        g = 255 - g
        b = 255 - b
        return r, g, b

class BlurringFilter(Filter):
    """Фильтр, который размывает изображение"""
    def apply_stock(self):
        return ImageFilter.GaussianBlur(20)


filters = {
    1: {
        "name": "Синий фильтр.",
        "Description": "Накладывает на твоё изображение синий цвет.",
        "class": BlueFilter()
    },
    2: {
        "name": "Тёмный фильтр.",
        "Description": "Фильтр который делает изображение темнее.",
        "class": DarkFilter()
    },
    3: {
        "name": "Инверсионный фильтр.",
        "Description": "Заменяет цвета на противоположные. Пример(белый-чёрный).",
        "class": InverseFilter()
    },
    4: {
        "name": "Размывающий фильтр.",
        "Description": "Размытие изображения, повышение резкости и сглаживание.",
        "class":  BlurringFilter()
    }
}