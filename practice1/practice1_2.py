#Тема “Работа с данными в Pandas”


import pandas as pd
import numpy as np

"""
Импортируйте библиотеку Pandas и дайте ей псевдоним pd. 
Создайте датафрейм authors со столбцами author_id и author_name, 
в которых соответственно содержатся данные: [1, 2, 3] и ['Тургенев', 'Чехов', 'Островский'].
Затем создайте датафрейм book cо столбцами author_id, book_title и price, в которых соответственно содержатся данные:  
[1, 1, 1, 2, 2, 3, 3],
['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
[450, 300, 350, 500, 450, 370, 290].

"""

authors = pd.DataFrame({'author_name': ['Тургенев', 'Чехов', 'Островский'],
                        'author_id': [1, 2, 3]})


book = pd.DataFrame({'author_id': [1, 1, 1, 2, 2, 3, 3],
                     'book_title': ['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
                     'price': [450, 300, 350, 500, 450, 370, 290]})


print(authors)

print(book)

"""
Задание 2
Получите датафрейм authors_price, соединив датафреймы authors и books по полю author_id.

"""

authors_price = pd.merge(authors, book, on='author_id', how='outer')

print(authors_price, '\n')

"""
Задание 3
Создайте датафрейм top5, в котором содержатся строки из authors_price с пятью самыми дорогими книгами.

"""

top5 = authors_price.sort_values(by='price', ascending=False)[:5]

print(top5, '\n')

"""
Задание 4
Создайте датафрейм authors_stat на основе информации из authors_price. 
В датафрейме authors_stat должны быть четыре столбца:
author_name, min_price, max_price и mean_price,
в которых должны содержаться соответственно имя автора, минимальная, максимальная и средняя цена на книги этого автора.

"""


authors_stat = authors_price.groupby('author_name').agg(min_price=('price', 'min'),
                                                        max_price=('price', 'max'),
                                                        mean_price=('price', 'mean'))

print(authors_stat, '\n')


"""
Задание 5**

Создайте новый столбец в датафрейме authors_price под названием cover, в нем будут располагаться данные о том, 
какая обложка у данной книги - твердая или мягкая. В этот столбец поместите данные из следующего списка:
['твердая', 'мягкая', 'мягкая', 'твердая', 'твердая', 'мягкая', 'мягкая'].
Просмотрите документацию по функции pd.pivot_table с помощью вопросительного знака.
Для каждого автора посчитайте суммарную стоимость книг в твердой и мягкой обложке. 
Используйте для этого функцию pd.pivot_table. При этом столбцы должны называться "твердая" и "мягкая", а 
индексами должны быть фамилии авторов. Пропущенные значения стоимостей заполните нулями, при необходимости загрузите библиотеку Numpy.
Назовите полученный датасет book_info и сохраните его в формат pickle под названием "book_
info.pkl". Затем загрузите из этого файла датафрейм и назовите его book_info2. 
Удостоверьтесь, что датафреймы book_info и book_info2 идентичны.

"""

authors_price['cover'] = ['твердая', 'мягкая', 'мягкая', 'твердая', 'твердая', 'мягкая', 'мягкая']

print(authors_price)

#help(pd.pivot_table)

book_info = pd.pivot_table(authors_price,
                           values='price',
                           index=['author_name'],
                           columns=['cover'],
                           aggfunc=np.sum)

book_info = book_info.fillna(0)

print(book_info)

name = 'book_info.pkl'

book_info.to_pickle(name)

book_info2 = pd.read_pickle(name)

print(book_info2 == book_info)


