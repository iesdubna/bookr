import nltk
from functools import partial
from nltk.probability import FreqDist
import yaml
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from taskmanage.task import Task

def word_analysis(filename):
    clear_text = clean_text()
    # 20 самых частых слов
    fdist = FreqDist(clear_text)
    freq_words = fdist.most_common(20)

    # 20 самых редких слов
    freqdist = fdist.most_common()
    rare_words = []
    for i in range(1, 21):
        rare_words += freqdist[-i]

    # Лексическое разнообразие (отношения количества разных слов к общему количеству слов)
    lex_div = len(fdist)/len(clear_text)

    sum_word = 0
    # Процент 10 самых частых слов от общего количества слов
    for j in range(0, 10):
        sum_word += fdist[j][1]
    ten_most_frequent_words = (sum_word/len(clear_text))*100
    # Процент 20 самых частых слов от общего количества слов
    for j in range(0, 20):
        sum_word += fdist[j][1]
    twenty_most_frequent_words = (sum_word/len(clear_text))*100
    # Процент 30 самых частых слов от общего количества слов
    for j in range(0, 30):
        sum_word += fdist[j][1]
    thirty_most_frequent_words = (sum_word/len(clear_text))*100

    analysis_result = {"20 самых частых слов": freq_words, "20 самых редких слов": rare_words, "Лексическое разнообразие (отношения количества разных слов к общему количеству слов)":lex_div, "Процент 10 самых частых слов от общего количества слов":ten_most_frequent_words, "Процент 20 самых частых слов от общего количества слов)":twenty_most_frequent_words, "Процент 30 самых частых слов от общего количества слов": thirty_most_frequent_words}
    
    # Запись результата в yaml файл
    nazvanie = filename + ".yaml"
    with open (r"word_analysis\\" + nazvanie, 'w') as file:
        kek = yaml.dump(analysis_result, file)

# Функция для очистки исходного текста
def clean_text(f):
    clear_text = []
    big_text = ""
    for line in f:
        line = line.strip()
        if line == "":
            continue
        line = line.replace(':', '')
        line = line.replace('/', '')
        line = line.replace('!', '')
        line = line.replace(',', '')
        line = line.replace('_', '')
        line = line.replace('@', '')
        line = line.replace('.', '')
        line = line.replace('”', '')
        line = line.replace('“', '')
        line = line.replace('~', '')
        line = line.replace('*', '')
        line = line.replace('$', '')
        line = line.replace('#', '')
        line = line.replace('№', '')
        line = line.replace('%', '')
        line = line.replace('^', '')
        line = line.replace('&', '')
        line = line.replace('{', '')
        line = line.replace('}', '')
        line = line.replace('+', '')
        line = line.replace('=', '')
        line = line.replace('?', '')
        line = line.replace(')', '')
        line = line.replace('(', '')
        line = line.replace(';', '')
        line = line.replace('>', '')
        line = line.replace('<', '')
        line = line.replace('0', '')
        line = line.replace('1', '')
        line = line.replace('2', '')
        line = line.replace('3', '')
        line = line.replace('4', '')
        line = line.replace('5', '')
        line = line.replace('6', '')
        line = line.replace('7', '')
        line = line.replace('8', '')
        line = line.replace('9', '')
        big_text += line.lower()

        #Очистка от артиклей, предлогов и т.д.
        stopWords = set(stopwords.words('english')) 
        words = word_tokenize(big_text)
        text = []
        for w in words:
            if w not in stopWords:
                text.append(w) 

        #Выделение корней из слов
        stemmer = PorterStemmer()
        for j in text:
            clear_text.append(stemmer.stem(j))

    return clear_text

def create_tasks():
    tasks = []
    with open("books.yaml", "r") as f:
        data = yaml.safe_load(f)
        for item in data["books"]:
            task=Task(item["filename"])
            with open(item["filename"], "r", encoding="utf-8") as f:
                func_without_arguments=partial(word_analysis, item["filename"])
                task.set_action(func_without_arguments)
            tasks.append(task)
    return tasks