import time
import nltk
from taskmanage import task
import requests
from nltk.tokenize import sent_tokenize
import yaml
import numpy
from functools import partial

def analysis(length):
    with open("books.yaml","r") as f:
        data=yaml.safe_load(f)
    for book in data["download"]:
        with requests.get(book["link"],stream=True) as res:
            f=open(book["filename"],"wb")
            for chunk in res.iter_content(chunk_size=8192):
                f.write(chunk)
            f.close()
        len_sent=[]
        with open(book["filename"],"r",encoding="UTF-8") as f:
            for st in f:
                tmp=sent_tokenize(st)
                for i in tmp:   
                    len_sent.append(len(i.split()))
        sum=0
        for i in len_sent:
            if length==i:
                sum+=1
        num_sent=sum
        str_max = max(len_sent)
        str_min = min(len_sent)
        sum=0
        for i in len_sent:
            sum+=i
        str_mid = int(sum/len(len_sent))
        b=[]
        with open(book["filename"],"r",encoding="UTF-8") as f:
            for line in f:
                nltk_tokens = nltk.word_tokenize(line)
                b.append((list(nltk.bigrams(nltk_tokens))))
        a=[]
        for i in b:
            for j in list(i):
                b=j[0]+ " "+ j[1]
                a.append(b)
        for i in a:
            i = i.translate({ord(j): None for j in '.'})
            i = i.translate({ord(j): None for j in '!'})
            i = i.translate({ord(j): None for j in '?'})
            i = i.translate({ord(j): None for j in ','})
            i = i.translate({ord(j): None for j in '-'})
        for i in a:
            if len(i.split())==1:
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
        resul=""
        for i in range(20):
            res = numpy.argmax(arr)
            resul+=(cleared_bigrams[res])+"\n"
            del arr[res]
        name_book=str(book["filename"])
        result={"Length of the longest sentence": str(str_max), "Average sentence length" : str(str_mid) , "The length of the shortest sentence": str(str_min),"Number of length sentences "+ str(length) :str(num_sent),"The 20 most frequent phrases:":resul}
        with open("sentence_analysis_"+ name_book+".yaml","w") as f:
            for key, value in result.items():
                f.write(f'{key}, {value}\n')

funk_without_arguments = partial(analysis,5)
task0 = task.Task("0")
task0.action=funk_without_arguments
task0.run()
