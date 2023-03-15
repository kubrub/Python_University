from PIL import Image

# Відкриття першого зображення
image1 = Image.open("image1.jpg")

# Відкриття другого зображення
image2 = Image.open("image2.jpg")

# Перевірка чи розміри зображень співпадають
if image1.size != image2.size:
    raise ValueError("Зображення мають різні розміри")

# Режим зображення "RGB" або "CMYK"
mode = image1.mode

# Масив з пікселями першого зображення
pixels1 = image1.load()

# Масив з пікселями другого зображення
pixels2 = image2.load()

# Віднімання зображення для всіх кольорів разом
for y in range(image1.size[1]):
    for x in range(image1.size[0]):
        # Отримати значення кольорів кожного пікселя
        r1, g1, b1 = pixels1[x, y]
        r2, g2, b2 = pixels2[x, y]

        # Відняти значення кольорів другого зображення від першого зображення
        pixels1[x, y] = (r1 - r2, g1 - g2, b1 - b2) if mode == "RGB" else (0, 0, 0, 0)

# Збереження результуючого зображення
image1.save("result.jpg")
