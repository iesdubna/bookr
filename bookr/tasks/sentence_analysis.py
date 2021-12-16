from bookr.taskmanage.task import Task
from nltk.tokenize import word_tokenize
import yaml
from nltk import FreqDist
from nltk import sent_tokenize
from nltk import bigrams
from functools import partial
from bookr import cfg


def analysis(bookpath, resultpath):

    with open(bookpath, "r", encoding="UTF-8") as f:
        text = f.read()

    fdist = FreqDist()
    for sentence in sent_tokenize(text):
        words = word_tokenize(sentence)
        fdist[len(words)] += 1

    # calculate maximum sentence length
    max_length = 0
    for l in fdist.keys():
        if l > max_length:
            max_length = l

    # calculate minimum sentence length
    min_length = max_length
    for l in fdist.keys():
        if l < min_length:
            min_length = l

    # calculate mean sentence length
    total_length = 0
    total_num = 0
    for l, n in fdist.items():
        total_length += l * n
        total_num += n
    average_length = int(total_length / total_num)

    # calculate bigrams
    bgms_fdist = FreqDist()
    for sentence in sent_tokenize(text):
        for b in bigrams(word_tokenize(sentence)):
            bgms_fdist[b] += 1

    # remove bigrams where first or second words starts with one of wrong symbols
    wrong_symbols = ['*','.',',','?','!','-',':',';',"'",'"','`']
    for bgm in list(bgms_fdist.keys()):
        for s in wrong_symbols:
            if bgm[0].startswith(s) or bgm[1].startswith(s):
                del bgms_fdist[bgm]

    result = {
        "sentence_length_max": max_length,
        "sentence_length_average": average_length,
        "sentence_length_min": min_length,
        "most_frequent_sentence_lengths": {l: n for l, n in fdist.most_common(20)},
        "most_frequent_bigrams": {"_".join(b): n for b, n in bgms_fdist.most_common(20)},
    }
    with open(resultpath, "w") as f:
        yaml.dump(result, f, default_flow_style=False)


def create_tasks():
    tasks = []
    for book in cfg.CONF["books"]:
        task = Task(book["name"])
        bookpath = cfg.datapath(book["txt_file"])
        resultpath = cfg.datapath(book["sentence_analysis_file"])
        func_without_arguments = partial(analysis, bookpath, resultpath)
        task.set_action(func_without_arguments)
        tasks.append(task)
    return tasks