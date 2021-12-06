import string
from functools import partial

from nltk.probability import FreqDist
import yaml
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

from bookr.taskmanage import task
from bookr import cfg


STOP_WORDS = set(stopwords.words('english'))
STOP_WORDS.add("gutenberg")


def word_analysis(bookpath, resultpath):
    with open(bookpath, encoding="utf-8") as f:
        text = f.read()

    text = text.translate(dict.fromkeys(string.punctuation))
    tokenizer = RegexpTokenizer(r'\w+')
    words = tokenizer.tokenize(text)

    stemmer = PorterStemmer()

    words2 = []
    for word in words:
        if word.lower() not in STOP_WORDS:
            words2.append(stemmer.stem(word))

    # 20 самых частых слов
    fdist = FreqDist(words2)

    # Лексическое разнообразие (отношения количества разных слов к общему количеству слов)
    lex_div = len(fdist) / len(words2)

    # Процент 10 самых частых слов от общего количества слов
    ten_most_frequent_words = (sum(i[1] for i in fdist.most_common(10)) / len(words2)) * 100
    # Процент 20 самых частых слов от общего количества слов
    twenty_most_frequent_words = (sum(i[1] for i in fdist.most_common(20)) / len(words2)) * 100
    # Процент 30 самых частых слов от общего количества слов
    thirty_most_frequent_words = (sum(i[1] for i in fdist.most_common(30)) / len(words2)) * 100

    analysis_result = {
        "most_frequent": list(dict(fdist.most_common(20))),
        "most_rare": list(FreqDist(dict(fdist.most_common()[-20:]))),
        "lexical_diversity": lex_div,
        "percentile_10": ten_most_frequent_words,
        "percentile_20": twenty_most_frequent_words,
        "percentile_30": thirty_most_frequent_words,
    }
    
    # Запись результата в yaml файл
    with open (resultpath, 'w') as file:
        yaml.safe_dump(analysis_result, file)


def create_tasks():
    tasks = []
    for item in cfg.CONF["books"]:
        t = task.Task(item["word_analysis_file"])
        bookpath = cfg.datapath(item["txt_file"])
        resultpath = cfg.datapath(item["word_analysis_file"])
        func_without_arguments = partial(word_analysis, bookpath, resultpath)
        t.set_action(func_without_arguments)
        tasks.append(t)
    return tasks