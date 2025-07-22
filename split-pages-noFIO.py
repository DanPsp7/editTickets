import os
import fitz  # PyMuPDF

def split_pdf_pages(input_folder='new1', output_folder='new2'):
    """
    Разбивает все PDF-файлы в папке на отдельные страницы.
    Каждая страница сохраняется как отдельный PDF-файл с понятным именем.
    
    :param input_folder: Путь к папке с исходными PDF-файлами
    :param output_folder: Путь к папке для сохранения результатов
    """
    # Создаем папку для результатов, если ее нет
    os.makedirs(output_folder, exist_ok=True)
    
    # Проходим по всем файлам в указанной папке
    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.pdf'):
            input_path = os.path.join(input_folder, filename)
            
            try:
                # Открываем PDF файл
                with fitz.open(input_path) as pdf_file:
                    # Получаем базовое имя файла без расширения
                    base_name = os.path.splitext(filename)[0]
                    
                    for page_num in range(len(pdf_file)):
                        # Создаем новый PDF файл только с одной страницей
                        new_pdf = fitz.open()
                        new_pdf.insert_pdf(pdf_file, from_page=page_num, to_page=page_num)
                        
                        # Формируем имя файла: оригинальное_имя_страницаN.pdf
                        new_filename = f"{base_name}_страница{page_num + 1}.pdf"
                        output_path = os.path.join(output_folder, new_filename)
                        
                        # Сохраняем новый PDF-файл
                        new_pdf.save(output_path)
                        new_pdf.close()
                        
                        print(f"Создан файл: {new_filename}")
                        
            except Exception as e:
                print(f"Ошибка при обработке файла {filename}: {str(e)}")

if __name__ == "__main__":
    split_pdf_pages()
