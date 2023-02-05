# Вспоминаем

# 1.min max функции мин макс
# 2.len count
# 3. random принимает старт стоп  и даёт число случайное


#print(max(1,2,3,4,5))
'''
def my_max(*args):
    max_number = 0
    for i in args:
        if type(i) == int and i > max_number:
            max_number = i
    return max_number
print(my_max(1, 2, 'g'))
'''


'''
def my_min(*args):
    max_number = 0
    for i in args:
        if i > max_number:
            max_number = i
        return max_number
    min_number = max_number
    for i in args:
        if i < min_number:
            max_namber = i
    return min_number
print(my_min(1, 2, 3, 4, 23))
'''


'''
def my_len(s):

    if type(s) == int:
        return TypeError
    else:
        count = 0
        for i in s:
            count += 1
        return count

print(my_len(123))
'''


'''
def my_count(s, char):
    count = 0
    for i in s:
        if i == char:
            count += 1
    return count
print(my_count('hello world', 'l'))
'''


'''
def my_randint(start, stop):
    my_set = set()
    for i in range(start, stop):
        my_set.add(str(i))
    my_list = []
    for i in my_set:
        my_list.append(int(i))
    return my_list[0]
print(my_randint(1, 100))
'''

'''
#певести в список а в списке мы можем получить индекс
#s = list('hello')
def my_count(s, char):
    index_list = []
    count = 0
    for i in s:
        if i == char:
            count += 1
            index_list.append(s.index(i))
    return count, index_list
print(my_count('hello world', 'l'))
'''
'''
from random import choice
my_alf = 'qwertyuiopasdfghjklzxcvbnm'
my_list = [choice(my_alf) for i in range(1, 101)]
print(my_list)
'''
s = 'hello world'
def my_count(s, char):
    index_list = []
    count_word = 0
    count = -1
    for i in s:
        if i == char:
            count_word += 1
            index_list.append(count)
    return count_word, index_list

print(my_count(s, 'l'))