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
        # Получаем дату из имени файла
        #date = filename.split(' ')[0]
        #letter = filename.split('.pdf')[0].split(' ')[-1]
        #date = filename.split(letter)[0].split(' ')[-2]
     
        date = filename.split('.pdf')[0].split(' ')[-1]
        #mounth = filename.split(' ')[1]
        # Получаем список имен для новых файлов
        #name_list = filename.split('.pdf')[0].split(date)[1].split(mounth)[1].split(',')
        #name_list = filename.split('.pdf')[0].split(date)[0].strip().split(',')
        name_list = filename.split(date)[0].strip().split(',')
        #name_list = filename.split('.pdf')[0].split(letter)[0].split(date)[0].split(',')
        #name_list = filename.split('.pdf')[0].split('(2)')[0].split(',')
        if len(name_list) > 1:
            name_list = [f"{name.strip()}" for name in name_list]
        else:
            #name_list = [filename.split('.pdf')[0].strip()]
            #name_list = [filename.split('.pdf')[0].split(date)[1].strip()]
            #name_list = [filename.split('.pdf')[0].split(date)[0].strip()]
            name_list = [filename.split(date)[0].strip()]
            #name_list = [filename.split('.pdf')[0].split(letter)[0].split(date)[0].strip()]
        # Проходим по всем страницам PDF файла
        for page_num in range(pdf_file.page_count):
            # Создаем новый PDF файл только с одной страницей
            new_pdf = fitz.open()
            new_pdf.insert_pdf(pdf_file, from_page=page_num, to_page=page_num)
            # Сохраняем новый PDF файл под соответствующим именем
            #new_filename = f"{os.path.splitext(filename)[0]} {page_num+1}.pdf"
            #new_filename = f"{name_list[page_num]} {date}{mounth}.pdf"
            new_filename = f"{name_list[page_num]}{date}.pdf"
            #new_filename = f"{name_list[page_num]}Б-О.pdf"
            # if os.path.exists(os.path.join(path_to_save, new_filename)):
            #     new_filename = f"{name_list[page_num]}О-Б.pdf"
            # try:
            #     #new_filename = f"{name_list[page_num]} {date}.pdf"
            #     new_filename = f"{name_list[page_num]}.pdf"
            #     if os.path.exists(os.path.join(path_to_save, new_filename)):
            #         new_filename = f"{name_list[page_num]}2.pdf"
            # except IndexError:
            #     new_filename = f"page{page_num+1}.pdf"
            #     if os.path.exists(os.path.join(path_to_save, new_filename)):
            #         new_filename = f"page{page_num+1}2.pdf"
            new_pdf.save(os.path.join(path_to_save, new_filename))
            new_pdf.close()

        pdf_file.close()