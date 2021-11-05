import time
import nltk
from taskmanage.task import Task
import requests
from nltk.tokenize import sent_tokenize
import yaml
import numpy
from functools import partial

# Отчёт о проделанной работе:
# в итоге наша функция принимает
# значения bookpath (путь к книге)
# и length (длина).
# С точки зрения создания
# списка задач все работает правильно.
# (при условии, что книжки загружены).
# Осталось разобраться с начинкой функции analysis
# Не надо трогать её интерфейс (то есть мы должны передавать туда
# bookpath и length)
# ТО, С ЧЕМ МНЕ СПРАВИТЬСЯ НЕ УДАЛОСЬ:
# bookpath - путь к какой-то книге в дирректории books.
# length - мы ищем длину какого-то пркдложения.
# Не получилось найти другой способ построчно считать файл
# зная только расположение файла.

def analysis(bookpath,length):
    #_____________Мы не должны открывать файл books.yaml и загружать все оттуда. Этим занимается другая команда.
    with open("books.yaml", "r") as f:
        data = yaml.safe_load(f)
    #___________________________________________________________________________________________________________

    #_____Тут аналогично_______________
    for book in data["books"]:
        with requests.get(book["link"], stream=True) as res:
            f = open(book["filename"], "wb")
            for chunk in res.iter_content(chunk_size=8192):
                f.write(chunk)
            f.close()
        len_sent = []
        with open(book["filename"], "r", encoding="UTF-8") as f:
            for st in f:
                tmp = sent_tokenize(st)
                for i in tmp:
                    len_sent.append(len(i.split()))
        #________________________________
        sum = 0
        for i in len_sent:
            if length == i:
                sum += 1
        num_sent = sum
        str_max = max(len_sent)
        str_min = min(len_sent)
        sum = 0
        for i in len_sent:
            sum += i
        str_mid = int(sum / len(len_sent))
        b = []
        with open(book["filename"], "r", encoding="UTF-8") as f:
            for line in f:
                nltk_tokens = nltk.word_tokenize(line)
                b.append((list(nltk.bigrams(nltk_tokens))))
        a = []
        for i in b:
            for j in list(i):
                b = j[0] + " " + j[1]
                a.append(b)
        for i in a:
            i = i.translate({ord(j): None for j in '.'})
            i = i.translate({ord(j): None for j in '!'})
            i = i.translate({ord(j): None for j in '?'})
            i = i.translate({ord(j): None for j in ','})
            i = i.translate({ord(j): None for j in '-'})
        for i in a:
            if len(i.split()) == 1:
                a.remove(i)
            else:
                pass
        cleared_bigrams = list(dict.fromkeys(a))
        sum = 0
        arr = []
        for i in cleared_bigrams:
            for j in a:
                if i == j:
                    sum += 1
            arr.append(sum)
            sum = 0
        resul = ""
        for i in range(20):
            res = numpy.argmax(arr)
            resul += (cleared_bigrams[res]) + "\n"
            del arr[res]
        name_book = str(book["filename"])
        result = {"Length of the longest sentence": str(str_max), "Average sentence length": str(str_mid),
                  "The length of the shortest sentence": str(str_min),
                  "Number of length sentences " + str(length): str(num_sent), "The 20 most frequent phrases:": resul}
        with open("sentence_analysis_" + name_book + ".yaml", "w") as f:
            yaml.dump(result, f, default_flow_style=False)

def create_tasks():
    with open("books.yaml", "r") as f:
        config = yaml.safe_load(f)
    tasks = []
    for book in config["books"]:
        path = "books/" + book["filename"]
        task = Task(path)
        funk_without_arguments = partial(analysis, path , 5) # Значение переменной length = 5.
        task.set_action(funk_without_arguments)
        tasks.append(task)
    return tasks

for t in create_tasks():
    t.run()

