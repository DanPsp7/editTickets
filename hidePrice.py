import fitz
import os

path = "new1"
path_to_save = "new2"

for file in os.listdir(path):
    if not file.endswith(".pdf"):
        continue

    doc = fitz.open(os.path.join(path, file))
    file_name = file.split('.pdf')[0]

    for page in doc:
        # Ищем текст, после которого нужно вставить прямоугольник
        text_to_find = "ПЕРЕДАТ"
        text_instances = page.search_for(text_to_find)

        if text_instances:  # Если текст найден
            # Берем координаты последнего вхождения (если их несколько)
            rect = text_instances[-1]
            y_start = rect.y0  # Нижняя граница найденного текста
            y_end = page.rect.y1 - 50  # До нижнего края страницы (с отступом)
            x_start = 15
            x_end = 580

            page.draw_rect([x_start, y_start, x_end, y_end], color=(1, 1, 1), fill=(1, 1, 1))
        else:
            # Если текст не найден, можно использовать дефолтные координаты или пропустить
            print(f"Текст '{text_to_find}' не найден в файле {file}")

    doc.save(os.path.join(path_to_save, file_name + "M.pdf"))