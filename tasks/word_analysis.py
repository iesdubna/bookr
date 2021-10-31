import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import yaml
from pprint import pprint
import collections
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from taskmanage.task import Task

def twenty_freq_words(clear_text):
    fdist = FreqDist(clear_text)
    freq_words = fdist.most_common(20)
    return freq_words

def twenty_rare_words(clear_text):
    fdist = FreqDist(clear_text)
    fdist = fdist.most_common()
    rare_words = []
    for i in range(1, 21):
        rare_words += fdist[-i]
    return rare_words

def lexical_diversity(clear_text):
    fdist = FreqDist(clear_text)
    lex_div = len(fdist)/len(clear_text)
    return lex_div

def percent_total(clear_text):
    fdist = FreqDist(clear_text)
    sum_word = 0
    for j in range(0, 10):
        sum_word += fdist[j][1]
    ten_most_frequent_words = (sum_word/len(clear_text))*100

    for j in range(0, 20):
        sum_word += fdist[j][1]
    twenty_most_frequent_words = (sum_word/len(clear_text))*100

    for j in range(0, 30):
        sum_word += fdist[j][1]
    thirty_most_frequent_words = (sum_word/len(clear_text))*100
    # list = {"Отношение количества 10 самых частых слов от общего числа слов: ": ten_most_frequent_words, "Отношение количества 20 самых частых слов от общего числа слов: ": twenty_most_frequent_words, "Отношение количества 30 самых частых слов от общего числа слов: ": thirty_most_frequent_words}
    return ten_most_frequent_words



with open("books.yaml", "r") as f:
    data = yaml.safe_load(f)
    print(len(data["books"]))
    clear_text = ""
    for item in data["books"]:
        # print(item["filename"])
        word_counter = collections.defaultdict(int)
        with open(item["filename"], "r", encoding="utf-8") as f:
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
            text = ""
            for w in words:
                if w not in stopWords:
                    text += w
                    text += ' '

            #Выделение корней из слов
            stemmer = PorterStemmer()
            qwer = ""
            drow = text.split(" ")
            for j in drow:
                qwer += stemmer.stem(j)
                qwer += ' '
              # print(qwer)
                # qwerty = word_tokenize(qwer)
            clear_text = qwer.split(" ")
            # print(clear_text)
            # print(len(clear_text))
                # print(qwerty)
                # assa = []
            
            fdist = FreqDist(clear_text)
            # print(len(fdist))
            # fdist.most_common(20)
            # print(fdist.most_common(20))
            fdist = fdist.most_common()
            assa = []
            for i in range(1, 21):
                assa += fdist[-i]

            # print(assa)

            # lexical_diversity = len(fdist)/len(clear_text)
            # print(lexical_diversity)

            sum_word = 0
            for j in range(0, 10):
                sum_word += fdist[j][1]
            ten_most_frequent_words = (sum_word/len(clear_text))*100
            # print(ten_most_frequent_words)

            for j in range(0, 20):
                sum_word += fdist[j][1]
            twenty_most_frequent_words = (sum_word/len(clear_text))*100
            # print(twenty_most_frequent_words)

            for j in range(0, 30):
                sum_word += fdist[j][1]
            thirty_most_frequent_words = (sum_word/len(clear_text))*100
            # print(thirty_most_frequent_words)


                # #Подсчет одинаковых корней-слов
                # for word in clear_text:
                #     word_counter[word] += 1
                
            # sorted_dict = {}
            # sorted_keys = sorted(word_counter, key=word_counter.get, reverse=True)

            # for w in sorted_keys:
            #     sorted_dict[w] = word_counter[w]
            
            # print(sorted_dict)
    print(len(data))      
    
    for i in range(1,5):
        nazvanie = item["filename"]+"_"+ str(i)  + ".yaml"

        # func = [twenty_freq_words(clear_text), twenty_rare_words(clear_text), lexical_diversity(clear_text), percent_total(clear_text)]
        output_1 = twenty_freq_words(clear_text)
        with open (r"word_analysis\\" + nazvanie, 'w') as file:
                kek = yaml.dump(output_1, file)
        output_2 = twenty_rare_words(clear_text)
        with open (r"word_analysis\\" + nazvanie, 'w') as file:
                kek = yaml.dump(output_2, file)
        output_3 = lexical_diversity(clear_text)
        with open (r"word_analysis\\" + nazvanie, 'w') as file:
                kek = yaml.dump(output_3, file)
        output_4 = percent_total(clear_text)
        with open (r"word_analysis\\" + nazvanie, 'w') as file:
                kek = yaml.dump(output_4, file)
