# tuples = ('Santhosh',24,'Male','Hobby: Gym','Loves: Coding')
# print(tuples)
# print(type(tuples[1]))
from operator import index

# lists = ['Santhosh',24,'Male']
# print(type(lists[1]))

# sets = {'Insta','whatsapp','facebook','facebook'}
# sets1 = {'Linkedin','Naukri','Indeed','facebook'}
# sets2 = {'Gmail','Outlook','Yahoo'}

# print(sets.intersection(sets1))

# dictionaries = {'Tamilnadu': 'Chennai',
#             'Kerala': 'Kochi',
#             'Karnataka': 'Bengaluru',
#             'Andhra' : 'Tirupati'}
#
# for a,b in dictionaries.items():
#     print(a, b)

# name = 'santhosh'
# if name[0].islower():
#     print(name.capitalize())

# def simpleinterest(principal,years,rate):
#     simple_interest = (principal * years * rate)/100
#     return  simple_interest
#
# x=simpleinterest(100,10,10)
# print(x)

# def product(*args):
#     prod = 1
#     for a in args:
#         prod *= a
#     return prod
#
#
# print(product(1, 2, 3, 4, 5))

# import random
#
# lists = ['get', 'a', 'high', 'paying', 'job']
# x = random.choice(lists)
#
# print(x)

# def simpleinterest(principal,years,rate):
#     simple_interest = (principal * years * rate)/100
#     return simple_interest
# try:
#     x = simpleinterest(100,10,10)
# except Exception as e:
#     print(e)
# else:
#     print(x)
# finally:
#     print('This block of try catch has been executed')

# import  os
# path = 'C:\\Users\\santhosh.loganathan\\Desktop\\Atlas\\APR'
#
# if os.path.exists(path):
#     print('This path exists')
#     if os.path.isdir(path):
#         print('This is a folder')
#     else:
#         print('This is not a folder')
# else:
#     print("This path doesn't exist")

# writes = '\nI am appending something'
# with open('test.txt', 'a') as file:
#     file.write(writes)

# import shutil
#
# shutil.copyfile('test.txt', 'copy.txt')

# import os
#
# source = 'test.txt'
# destination = "C:\\Users\\santhosh.loganathan\\Desktop\\move.text"
#
# try:
#     if os.path.exists(destination):
#         print('There is already a file present in the location')
#     else:
#         os.replace(source,destination)
#         print(source+' was moved')
# except Exception as e:
#     print(e)

# help('modules')

# import random
#
#
# while True:
#
#     choices = ['Rock', 'Paper', 'Scissors']
#
#     computer = random.choice(choices)
#     player = ''
#
#     while player not in choices:
#         player = input('Enter your choice : ').capitalize()
#
#     print('You : '+player)
#     print('Computer : '+computer)
#
#     if computer == player:
#         print('Tie!')
#
#     elif player == 'Rock':
#         if computer == 'Paper':
#             print('You Lose!')
#         elif computer == 'Scissors':
#             print('You win')
#
#     elif player == 'Scissors':
#         if computer == 'Paper':
#             print('You Win!')
#         elif computer == 'Rock':
#             print('You Lose')
#
#     elif player == 'Paper':
#         if computer == 'Scissors':
#             print('You Lose!')
#         elif computer == 'Rock':
#             print('You Lose')
#
#     player_choice = input('Do you want to play again (Y/N) : ').upper()
#     if player_choice != 'Y':
#         break
#
# print('Bubye')

# -------------------------
# def new_game():
# 
#     guesses = []
#     correct_guesses = 0
#     question_num = 1
# 
#     for key in questions:
#         print("-------------------------")
#         print(key)
#         for i in options[question_num-1]:
#             print(i)
#         guess = input("Enter (A, B, C, or D): ")
#         guess = guess.upper()
#         guesses.append(guess)
# 
#         correct_guesses += check_answer(questions.get(key), guess)
#         question_num += 1
# 
#     display_score(correct_guesses, guesses)
# 
# # -------------------------
# def check_answer(answer, guess):
# 
#     if answer == guess:
#         print("CORRECT!")
#         return 1
#     else:
#         print("WRONG!")
#         return 0
# 
# # -------------------------
# def display_score(correct_guesses, guesses):
#     print("-------------------------")
#     print("RESULTS")
#     print("-------------------------")
# 
#     print("Answers: ", end="")
#     for i in questions:
#         print(questions.get(i), end=" ")
#     print()
# 
#     print("Guesses: ", end="")
#     for i in guesses:
#         print(i, end=" ")
#     print()
# 
#     score = int((correct_guesses/len(questions))*100)
#     print("Your score is: "+str(score)+"%")
# 
# # -------------------------
# def play_again():
# 
#     response = input("Do you want to play again? (yes or no): ")
#     response = response.upper()
# 
#     if response == "YES":
#         return True
#     else:
#         return False
# # -------------------------
# 
# 
# questions = {
#  "Who created Python?: ": "A",
#  "What year was Python created?: ": "B",
#  "Python is tributed to which comedy group?: ": "C",
#  "Is the Earth round?: ": "A"
# }
# 
# options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
#           ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
#           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
#           ["A. True","B. False", "C. sometimes", "D. What's Earth?"]]
# 
# new_game()
# 
# while play_again():
#     new_game()
# 
# print("Byeeeeee!")
# 
# # -------------------------
# from main import Car
#
# c1 = Car('minicooper','1970','MX1')
#
# print(c1)

# from main import Prey,Predator,Rabbit
#
# rabbit = Rabbit()
# rabbit.flees()
#
# obj = Prey()
# obj.flees()

# class Quad:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
# class Square(Quad):
#
#     def __init__(self, length, width):
#         super().__init__(length, width)
#
#     def area(self):
#         return self.length * self.width
#
# class Cube(Quad):
#
#     def __init__(self, length, width, height):
#         super().__init__(length, width)
#         self.height = height
#
#     def area(self):
#         return self.length * self.width * self.height
#
# square = Square(3,3)
# cube = Cube(3,3,3)
#
# print(square.area())
# print(cube.area())
# foods = list()
# while (food := input('Enter some food you like: ')) != 'quit':
#     foods.append(food)
# print(foods)

# sum = lambda a, b: a + b
# print(sum(5, 5))

# store = [('Shirt', 20.00),
#          ('Pant', 30.00),
#          ('Tshirt', 15.00)]
#
# provision = [('Biscuits', 5),
#              ('Chocolates', 10)]
#
# convertion = lambda data : (data[0], data[1]*1)
#
# print(convertion())

# store_converted = map(convertion, provision)
# for i in store_converted:
#     print(i)

# friends = [(1, 'Saranya', 18), (2, 'Surya', 16), (3, 'Manu', 20), (4, 'Reshmi', 12)]
#
# ages = lambda a: a[2] >= 18
#
# filtered_age = filter(ages, friends)
#
# for i in filtered_age:
#     print(i)

# import functools
#
# summa = ['I','am','gonna','fucking','get','that','job']
# summa1 = functools.reduce(lambda a,b:a+' '+b,summa)
# print(summa1)

# user_input = int(input('Enter a number to find the factorial: '))
# # lists = list()
# factorial = 1
# for i in range(1, user_input+1):
#     factorial *= i
# #     lists.append(i)
# # factorial = functools.reduce(lambda a, b: a*b, lists)
# print(factorial)

# friends = {'Santhosh': 24, 'Bharathi': 23, 'Tarun': 17, 'Keerthu': 20}
#
# adult = {key: 'adult' if value > 18 else 'teen' for (key, value) in friends.items()}
#
# print(adult)

# import time
#
# print(time.ctime(0))
# print(time.time())
# print(time.ctime(time.time()))

# import threading
# import time
#
# def eating():
#     time.sleep(3)
#     print('I am eating')
#
# def reading():
#     time.sleep(4)
#     print('I am reading')
#
# def drinking():
#     time.sleep(5)
#     print('I am drinking coffee')
# start = time.perf_counter()
# x = threading.Thread(target=eating, args=())
# x.start()
# y = threading.Thread(target=reading, args=())
# y.start()
# z = threading.Thread(target=drinking, args=())
# z.start()
# x.join()
# y.join()
# z.join()
#
# print(threading.active_count())
# print(threading.enumerate())
# print(time.perf_counter() - start)


# import time
# from multiprocessing import Process, cpu_count
#
#
# start = time.perf_counter()
# def counter(num):
#     count = 0
#     while count < num:
#         count += 1
#     return count
#
# def main():
#     a = Process(target=counter, args=(125000000,))
#     b = Process(target=counter, args=(125000000,))
#     c = Process(target=counter, args=(125000000,))
#     d = Process(target=counter, args=(125000000,))
#     e = Process(target=counter, args=(125000000,))
#     f = Process(target=counter, args=(125000000,))
#     g = Process(target=counter, args=(125000000,))
#     h = Process(target=counter, args=(125000000,))
#
#     a.start()
#     b.start()
#     c.start()
#     d.start()
#     e.start()
#     f.start()
#     g.start()
#     h.start()
#
#     a.join()
#     b.join()
#     c.join()
#     d.join()
#     e.join()
#     f.join()
#     g.join()
#     h.join()
#
#     # print(counter(10000000000))
#     print(cpu_count())
#     print(time.perf_counter() - start)  #50
#
# if __name__ == '__main__':
#     main()
# import time
# import math
#
# start = time.perf_counter()
#
#
# def prime(n):
#     count = 0
#     for i in range(1, n):
#         if (n % i) == 0:
#             count += 1
#     if count > 1:
#         print('Not Prime')
#
#     else:
#         print('Prime')
#
#
# prime(100000000)
# print(time.perf_counter() - start)
#
# start2 = time.perf_counter()
#
#
# def prime2(n):
#     count = 0
#     n2 = round(math.sqrt(n))
#     for i in range(2, n2):
#         if n % i == 0:
#             count += 1
#     if count == 0:
#         print('Prime')
#     else:
#         prime('Not Prime')
#
#
# prime2(100000000)
# print(time.perf_counter() - start2)

# 3,2,4,6,8

# def two_sum(nums, target):
#     prev = {}
#     for i, n in enumerate(nums):
#         print(n, i)
#         diff = target - n
#         if diff in prev:
#             return [prev[diff], i]
#         prev[n] = i
#         print(prev)
#     return
#
#
# print(two_sum([3,2,4,6,8], 7))

# def my_sqrt(n: int):
#     start = 1
#     for i in range(start, n+1):
#         if round(int((n/2) * (n/2))) == n:
#             return n
#         elif round(int(n/2 * n/2)) < n:
#             start = (n/2) + 1
#         elif round(int(n/2 * n/2)) > n:
#             n = (n/2) - 1
#
# print(my_sqrt(100))

# i = 0
# n = int(input("Enter some number: "))
#
# for i in range(1, 11):
#     for j in range(1, n+1):
#         i += 1
#     print(i)


# mylist = ['san','bhar','tar']
#
# join = '+'
#
# print(join.join(mylist))


# s1 = 'anagram'
# s2 = 'nagaram'
#
# counts1, counts2 = {}, {}
#
# for i in range(len(s1)):
#     counts1[s1[i]] = 1 + counts1.get(s1[i], 0)
#
# print(counts1)

# orulist = [2,4,5,7,9,8,1,0,4,8,9]
# orumap = {}
# key = 0
# for i in range(len(orulist)):
#     orumap[orulist[i]] = key
#     key+=1
#
# print(orumap)
# print(orumap[2])

# orulist = [2, 4, 9, 3, 1, 5, 9, 6, 1, 3]


# def two_sum(sum):
#     for i in range(len(orulist)):
#         for j in range(i+1, len(orulist)):
#             if sum == (orulist[i]+orulist[j]):
#                 return i, j
#     return False
#
# print(two_sum(3))

# def reverse(orulist):
#     increment = 1
#     decrement = -1
#     temp = ''
#     for i in range(0, len(orulist)//2):
#         temp = orulist[i]
#         orulist[i] = orulist[decrement]
#         orulist[decrement] = temp
#         decrement -= 1
#
#     return orulist
#
# print(reverse(orulist))

# def clockwise(orulist, k): #[2,4,9,3,1,5,9,6,1,3] Clockwise
#     for i in range(1, k+1):
#         temp = orulist[-1]
#
#         for j in range(len(orulist)-2, -1, -1):
#             orulist[j+1] = orulist[j]
#         orulist[0] = temp
#     return orulist
#
# print(clockwise(orulist, 7))

# def rangesum(orulist):
#     print(f'The given list is {orulist}')
#     s = int(input('Enter start index: '))
#     e = int(input('Enter end index: '))
#     sum = 0
#     for i in range(s, e + 1):
#         sum += orulist[i]
#     return sum
#
#
# print(rangesum(orulist))

# def prefixsum(orulist): #[2,4,9,3,1,5,9,6,1,3]
#     sum = 0
#     for i in range(1, len(orulist)):
#         orulist[i] += orulist[i-1]
#     return orulist
#
# print(prefixsum(orulist))

# inorulist = [-7, 1, 5, 2, -4, 3, 0] #[1,2,3,4,8,10]
#
# def equiinndex(inorulist):
#     sum = 0
#     result = []
#     for i in range(0, len(inorulist)):
#         if i == 0:
#             result.append(inorulist[i])
#         else:
#             result.append(inorulist[i] + result[i-1])
#
#     print(result)
#
#     for i in range(1, len(result)):
#         if result[i-1] == (result[-1] - result[i]):
#             return True, i
#     else:
#         return False
#
# print(equiinndex(inorulist))

# import pyautogui
# import time
# time.sleep(4)
# count = 0
# while count<=10:
#     pyautogui.typewrite('Good Night')
#     pyautogui.press('Enter')
#     count+=1

# summa = {}
#
# summa['Santhosh'] = 1
#
# print(summa)
# print(summa['Santhosh'])
#
# for i, j in summa.items():
#     print(j)

# try:
#     division = 2/0
#     print(division)
# except:
#         print('Divide by zero')
#         raise

# Vector = list[float]
#
# def scale(scalar: float, vector: Vector) -> Vector:
#     return [scalar * num for num in vector]
#
# # passes type checking; a list of floats qualifies as a Vector.
# new_vector = scale(2, [1.0, -4.2, 5.4])
# print(new_vector)
# aNumber = 124
#
# print(bin(124))

# myname = 'santhosh'
# print(123.isdigit())

# dogs_weight = (('Pug', 20), ('Lab', 30), ('Golden', 25))
#
# for i, (dog, weight) in enumerate(dogs_weight):
#     print(i, dog, weight)

# myrange = range(10, 1, -2)
# print(myrange)
# print(list(myrange))

# ls1 = [1,2,3,4,5,6,7,8,9,0]
#
# print(ls1[1:8:2])

# ls2 = []
# for i in range(100, 301):
#     str1 = str(i)
#
#     fn = int(str1[0])
#     sn = int(str1[1])
#     tn = int(str1[2])
#
#     if ((fn % 2 == 0) and (sn%2==0) and (tn%2==0)):
#         ls2.append(str1)
# print(ls2)

# for i in range(1, 12):
#     for j in range(1, 11):
#         print('{:3d}'.format(i*j), end=' ')
#     print()
ls3 = [['volks', 'Honda', 'Hyundai'], ['Maruti', 'Tata', 'Mahindra']]
# for i in ls3:
#     for j in i:
#         print(j)
# for i in range(2000, 3000):
#     if i % 4 == 0:
#         print(i, 'is a leap year')
#     else:
#         print(i, 'is not a leap year')

# for i in range(3):
#     inputs = input('Enter your Password: ')
#     if inputs == 'secret':
#         print('Correct')
#         break
# else:
#     print('3 Wrong attempts')

# import mysql.connector
#
# # Create the connection object
# myconn = mysql.connector.connect(host="127.0.0.1", user="root", passwd="root")
#
# # printing the connection object
# print(myconn)
#
# cur = myconn.cursor()
# print(cur)
# dbs = cur.execute('show databases')
# for i in dbs:
#     print(cur)


# import mysql.connector
#
# # Create the connection object
# myconn = mysql.connector.connect(host="localhost", user="root", passwd="root")
#
# # creating the cursor object
# cur = myconn.cursor()
#
# try:
#     # creating a new database
#     cur.execute("create database PythonDB2")
#
#     # getting the list of all the databases which will now include the new database PythonDB
#     dbs = cur.execute("show databases")
#
# except:
#     myconn.rollback()
#
# for x in cur:
#     print(x)
#
# myconn.close()


import pyodbc


# ls1 = ['santhosh', 'bharathi', 'tarun']
# ls2 = ['25','24','18']
# newdict = dict()
# for i, j in zip(ls1, ls2):
#     newdict.update({i:j})
# print(newdict)

# for i in range(315):
#     if not((i % 7) == 0):
#         print(i)

# list1 = [i**3 for i in range(20) if i % 3 == 0]
# print

# import pyautogui
# import time
#
# count=0
# time.sleep(5)
# while count<=50:
#     pyautogui.typewrite('Jinjuruki')
#     pyautogui.press('Enter')
#     time.sleep(10)
#     count+=1

# def students(college, city, *students):
#     print(college, city)
#     print(students)
#
# ls4 = ['Santhosh','Bhar', 'Tarun']
# students('SRM', 'Chennai', *ls4)

# strs = ["eat","tea","tan","ate","nat","bat"]
# def group_anagrams(strs):
#     result = dict()
#
#     for word in strs:
#         sorted_word = ''.join(sorted(word))
#         if sorted_word not in result:
#             result[sorted_word] = []
#             result[sorted_word].append(word)
#         else:
#             result[sorted_word].append(word)
#     return result
#
# print(group_anagrams(strs))

# ls5 = [1,2,3,4,6]

# def prod_except(ls5):
#     alistu = []
#     for i in range(len(ls5)):
#         prod = 1
#         temp = ls5.copy()
#         temp.remove(temp[i])
#         for j in temp:
#             prod = prod * j
#         alistu.append(prod)
#     return alistu
#
# print(prod_except(ls5))

# dic = {3: '1',
#        2: '4',
#        5: 11}
# print(dic.get(10, 0))

# dic1 = (san: 'Sandy')
# print(dic1)

# class Employee:
#        def __init__(self, empId, empName, empDesignation):
#               self.empId = empId
#               self.empName = empName
#               self.empDesignation = empDesignation
#
#
#        def printEmpDetails(self):
#               print(self.empId, self.empName, self.empDesignation)
#
# employee1 = Employee(1, 'Santhosh', 'SE')
# employee1.printEmpDetails()

# a = [2, 3, 4, 5, 5, 5, 0, 1]
# b = set(a)
# pivot = max(b)
# first_pivot = a.index(pivot)
# while a[first_pivot] == a[first_pivot+1]:
#     if a[first_pivot] == a[first_pivot+1]:
#         first_pivot+=1
# print(first_pivot)

# a = [1, 2, 3, 4, None]
# n = 0
# while a[n]:
#     print(a[n])
#     n += 1

# import pyttsx3
#
# def text_to_speech(text):
#     engine = pyttsx3.init()
#     engine.say(text)
#     engine.runAndWait()
#
# text_to_speech("Hello, how are you?")
# from gensim import summarize
#
# def summarize_paragraph(paragraph):
#     summary = (paragraph)
#     return summary
#
# paragraph = """
#     Machine learning is a form of artificial intelligence based on algorithms that are trained on data. These algorithms can detect patterns and learn how to make predictions and recommendations by processing data and experiences, rather than by receiving explicit programming instruction. The algorithms also adapt in response to new data and experiences to improve their efficacy over time. The volume and complexity of data that is now being generated, too vast for humans to reasonably reckon with, has increased the potential of machine learning, as well as the need for it. In the years since its widespread deployment, which began in the 1970s, machine learning has had impact in a number of industries, including achievements in medical-imaging analysis and high-resolution weather forecasting.
#     """
#
# summary = summarize_paragraph(paragraph)
# print(summary)
# from sumy.parsers.plaintext import PlaintextParser
# from sumy.nlp.tokenizers import Tokenizer
# from sumy.summarizers.lsa import LsaSummarizer
#
# def summarize_paragraph(paragraph, num_sentences=3):
#     parser = PlaintextParser.from_string(paragraph, Tokenizer("english"))
#     summarizer = LsaSummarizer()
#     summary = summarizer(parser.document, num_sentences)
#     summarized_text = " ".join(str(sentence) for sentence in summary)
#     return summarized_text
#
# paragraph = """
#     Machine learning is a form of artificial intelligence based on algorithms that are trained on data. These algorithms can detect patterns and learn how to make predictions and recommendations by processing data and experiences, rather than by receiving explicit programming instruction. The algorithms also adapt in response to new data and experiences to improve their efficacy over time. The volume and complexity of data that is now being generated, too vast for humans to reasonably reckon with, has increased the potential of machine learning, as well as the need for it. In the years since its widespread deployment, which began in the 1970s, machine learning has had impact in a number of industries, including achievements in medical-imaging analysis and high-resolution weather forecasting.
#     """
#
# summary = summarize_paragraph(paragraph)
# print(summary)

from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx


def read_article(content):
    sentences = content.split(". ")
    sentences.pop()
    return sentences


def sentence_similarity(sent1, sent2, stopwords=None):
    if stopwords is None:
        stopwords = []

    sent1 = [w.lower() for w in sent1]
    sent2 = [w.lower() for w in sent2]

    all_words = list(set(sent1 + sent2))

    vector1 = [0] * len(all_words)
    vector2 = [0] * len(all_words)

    for w in sent1:
        if w in stopwords:
            continue
        vector1[all_words.index(w)] += 1

    for w in sent2:
        if w in stopwords:
            continue
        vector2[all_words.index(w)] += 1

    return 1 - cosine_distance(vector1, vector2)


def build_similarity_matrix(sentences, stopwords):
    similarity_matrix = np.zeros((len(sentences), len(sentences)))

    for i in range(len(sentences)):
        for j in range(len(sentences)):
            if i == j:
                continue
            similarity_matrix[i][j] = sentence_similarity(sentences[i], sentences[j], stopwords)

    return similarity_matrix


def generate_summary(content, top_n=5):
    stop_words = stopwords.words('english')
    summarize_text = []

    sentences = read_article(content)
    sentence_similarity_matrix = build_similarity_matrix(sentences, stop_words)
    sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_matrix)
    scores = nx.pagerank(sentence_similarity_graph)
    ranked_sentences = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)

    for i in range(top_n):
        summarize_text.append(ranked_sentences[i][1])

    return ". ".join(summarize_text)


# Example usage
content = """Artificial intelligence is used in many different ways. One way it is used is in self-driving cars. The car uses sensors to gather information about its surroundings and then uses artificial intelligence to process that information and make decisions. This helps the car to avoid accidents and make driving more efficient. Artificial intelligence is also used in medical diagnosis, pattern recognition, and weather forecasting. Despite the many concerns that have been raised about artificial intelligence, it is clear that this technology can be used to benefit humanity in a number of ways.
From improving our understanding of the universe to creating more efficient systems and processes, artificial intelligence has the potential to change the world as we know it. As we continue to develop this technology, it is important that we do so with caution and care, ensuring that we are always aware of the risks involved. With responsible development, artificial intelligence could help us achieve great things."""
summary = generate_summary(content, top_n=3)
print(summary)



