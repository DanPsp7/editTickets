import os
import fitz

# Указываем путь к папке с PDF файлами
path = 'new1'
path_to_save = 'new2'

# Проходим по всем файлам в указанной папке
for filename in os.listdir(path):
    if filename.endswith('.pdf'):
        # Открываем PDF файл
        pdf_file = fitz.open(os.path.join(path, filename))
        # Проходим по всем страницам PDF файла
        for page_num in range(pdf_file.page_count):
            # Создаем новый PDF файл только с одной страницей
            new_pdf = fitz.open()
            new_pdf.insert_pdf(pdf_file, from_page=0, to_page=0)
            # Сохраняем новый PDF файл под соответствующим именем
            new_filename = f"{filename.split('.')[0]}.pdf"
            new_pdf.save(os.path.join(path_to_save, new_filename))
            new_pdf.close()

        pdf_file.close()