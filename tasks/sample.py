import time
from taskmanage import task
import requests
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
import string 

def fake_action_0():
    with requests.get('https://www.gutenberg.org/cache/epub/910/pg910-images.html',stream=True) as res:
        f=open("book.txt","wb")
        for chunk in res.iter_content(chunk_size=8192):
            f.write(chunk)
        f.close()

def fake_action_1():
    mas_text=[]
    f=open("book.txt","rb")
    mas_byte=f.readlines()
    for i in range(len(mas_byte)):
        soup = BeautifulSoup(mas_byte[i], 'html.parser')
        mas_text.append(soup.get_text())
    f.close()
    f=open("book.txt","w",encoding="utf-8")
    for i in range(len(mas_text)):
        f.write(mas_text[i])
    f.close()

def fake_action_2():
    mass_text=[]
    f=open("book.txt","r",encoding="utf-8")
    text=f.readlines()
    for i in range(115,1264):
        mass_text.append(text[i])
    for i in range(len(mass_text)):
        for p in string.punctuation:
            if p in mass_text[i]:
                mass_text[i] = mass_text[i].replace(p, '')         
    mas_text=['.']
    for line in mass_text:
        if (len(line.strip())):
            mas_text.append([line]) 
    mas_word_2 = []
    for i in range(len(mas_text)):
        mas_word_2.append([y for y in str(mas_text[i]).lower().split()])
    mas_word_1=sum(mas_word_2, [])
    mas_u_word=[]
    for item in mas_word_1: 
        if item not in mas_u_word: 
            mas_u_word.append(item)
    res=[]
    for i in range(len(mas_u_word)):
        res.append(int(0))
    for i in range(len(mas_u_word)):
        for j in mas_word_1:
            if j==mas_u_word[i]:
                res[i]+=1
    for i in range(10):
        print(mas_u_word[res.index(max(res))])
        del mas_u_word[res.index(max(res))]
    print('----')
    print('----')
    print('----')
    print('----')
    print('----')
    for i in range(10):
        print(mas_u_word[res.index(min(res))])
        del mas_u_word[res.index(min(res))]

task0 = task.Task("0")
task0.set_action(fake_action_0)

task1 = task.Task("1")
task1.set_action(fake_action_1)

task2 = task.Task("2")
task2.set_action(fake_action_2)
task1.depends_on(task0)
task2.depends_on(task0)
taskgraph = task.Taskgraph()

taskgraph.append_task(task0)
taskgraph.append_task(task1)
taskgraph.append_task(task2)
taskgraph.run_correct_order()
