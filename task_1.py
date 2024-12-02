import os
import sys
import shutil
import argparse

def recursive_copy(source_dir, dest_dir):
    """
    Рекурсивно копіює файли з вихідної директорії до директорії призначення,
    сортуючи їх за розширеннями.
    
    """
    try:
        # Перевіряємо, чи існує директорія призначення
        os.makedirs(dest_dir, exist_ok=True)
        
        # Проходимо по всіх елементах у вихідній директорії
        for item in os.listdir(source_dir):
            source_path = os.path.join(source_dir, item)
            
            # Якщо елемент є директорією - рекурсивний виклик
            if os.path.isdir(source_path):
                recursive_copy(source_path, dest_dir)
            
            # Якщо елемент є файлом
            elif os.path.isfile(source_path):
                # Отримуємо розширення файлу
                file_ext = os.path.splitext(item)[1][1:] or 'no_extension'
                
                # Створюємо піддиректорію за розширенням
                ext_dir = os.path.join(dest_dir, file_ext)
                os.makedirs(ext_dir, exist_ok=True)
                
                # Шлях для нового файлу
                dest_path = os.path.join(ext_dir, item)
                
                # Копіюємо файл
                try:
                    shutil.copy2(source_path, dest_path)
                    print(f'Copied: {source_path} -> {dest_path}')
                except PermissionError:
                    print(f'Помилка доступу: {source_path}')
                except Exception as e:
                    print(f'Помилка копіювання {source_path}: {e}')
    
    except PermissionError:
        print(f'Немає дозволу на доступ до директорії: {source_dir}')
    except FileNotFoundError:
        print(f'Директорія не знайдена: {source_dir}')
    except Exception as e:
        print(f'Невідома помилка: {e}')

def main():
    # Парсинг аргументів командного рядка
    parser = argparse.ArgumentParser(description='Рекурсивне копіювання файлів')
    parser.add_argument('source', help='Шлях до вихідної директорії')
    parser.add_argument('-d', '--dest', default='dist', 
                        help='Шлях до директорії призначення (за замовчуванням: dist)')
    
    args = parser.parse_args()
    
    # Повний шлях для вихідної та цільової директорій
    source_dir = os.path.abspath(args.source)
    dest_dir = os.path.abspath(args.dest)
    
    print(f'Копіювання з {source_dir} до {dest_dir}')
    recursive_copy(source_dir, dest_dir)
    print('Копіювання завершено')

if __name__ == '__main__':
    main()