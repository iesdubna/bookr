import re
import string
import time
import json
import requests
from taskmanage import task

# Домашнее задание. Загрузить книгу из интернета. Тут я загружал книгу "Война и мир" Л.Н. Толстого
def download_book_action():
    # Открытие конфигурационного файла json
    with open('url_of_book_and_filename.json') as file_1:
        configuration = json.load(file_1)
    file_1.close()

    # Присваивание значений переменным url и filename и  нашего файла
    url = configuration["book_url"]
    filename = configuration["book_filename"]

    # Используя библиотеку requests, делаем запрос и загружаем наш файл в локальную директорию
    with requests.get(url, stream = True) as response:
        with open(filename, "wb") as file_2:
            for chunk in response.iter_content():
                file_2.write(chunk)
    file_2.close()
    print("Книга загружена")

def analysis_book():
    # Поиск файла книги
    with open('url_of_book_and_filename.json') as file_1:
        configuration = json.load(file_1)
    file_1.close()
    filename = configuration["book_filename"]

    # Задача: Рассчитать частоту появления слов английского языка в книге
    # Решение:
    print("Пока в разработке")
    frequency = {}
    document_text = open(filename, 'r')
    text_string = document_text.read().lower()
    match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)

    for word in match_pattern:
        count = frequency.get(word, 0)
        frequency[word] = count + 1

    frequency_list = frequency.keys()

    for words in frequency_list:
        print(words, frequency[words])




def fake_action_0():
    print("Start action 0")
    time.sleep(1)
    print("Stop action 0")

def fake_action_1():
    print("Start action 1")
    time.sleep(10)
    print("Stop action 1")

def fake_action_2():
    print("Start action 2")
    time.sleep(1)
    print("Stop action 2")

def fake_action_3():
    print("Start action 3")
    time.sleep(3)
    print("Stop action 3")

def fake_action_4():
    print("Start action 4")
    time.sleep(1)
    print("Stop action 4")


task0 = task.Task("0")
task0.set_action(download_book_action)

task1 = task.Task("1")
task1.set_action(analysis_book)



# Создание зависимостей
task1.depends_on(task0)



taskgraph = task.Taskgraph()
taskgraph.append_task(task0)
taskgraph.append_task(task1)



taskgraph.run_in_threads()
