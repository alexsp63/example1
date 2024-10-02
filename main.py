# Контейнер расчета
# ИЗМЕНЕНО НА УСЛОВИЯ ВАРИАНТА 7

from sympy import *

k, T, C, L = symbols('k T C L')

# 1 (линейное)

C_ost = 70_000
Am_list = []
C_ost_list = []
age = 8

for i in range(age):
  Am = (C - L) / T
  sl = Am.subs({C: 70_000, T: age, L: 0})
  C_ost -= sl
  Am_list.append(round(sl, 2))
  C_ost_list.append(round(C_ost, 2))

print("Первый контейнер:")
print('Am_list: ', Am_list)
print('C_ost_list: ', C_ost_list)

# 2 (уменьшаемый остаток)

Aj = 0
C_ost = 70_000
Am_list_2 = []
C_ost_list_2 = []
k_val = 2

for i in range(age):
  Am = k * 1 / T * (C - Aj)
  sl = Am.subs({C: 70_000, T: age, k: k_val})
  C_ost -= sl
  Aj += Am
  Am_list_2.append(round(sl, 2))
  C_ost_list_2.append(round(C_ost, 2))

print('Am_list_2: ', Am_list_2)
print('C_ost_list_2: ', C_ost_list_2)
print()

# Контейнер табличного вывода

import pandas as pd

Y = range(1, age + 1)
table1 = list(zip(Y, C_ost_list, Am_list))
table2 = list(zip(Y, C_ost_list_2, Am_list_2))

tfame1 = pd.DataFrame(table1, columns=['Y', 'C_ost_list', 'Am_list'])
tfame2 = pd.DataFrame(table2, columns=['Y', 'C_ost_list_2', 'Am_list_2'])

print("Второй контейнер:")
print(tfame1)
print(tfame2)

# Контейнер визуализации

from matplotlib import pyplot as plt

plt.plot(Y, tfame1['C_ost_list'], label='C_ost_list')
plt.plot(Y, tfame2['C_ost_list_2'], label='C_ost_list_2')

plt.show()

# красивая круговая гистограмма для линейного

vals = Am_list
labels = list(range(1, age + 1))
explode = [0.1] * age
fig, ax = plt.subplots()
ax.pie(vals,
       labels=labels,
       explode=explode,
       autopct='%1.1f%%',
       shadow=True,
       wedgeprops={
           'lw': 1,
           'ls': '--',
           'edgecolor': 'k'
       },
       rotatelabels=True)

ax.axis('equal')
plt.show()

# красивая круговая гистограмма для нелинейного

vals = Am_list_2
labels = list(range(1, age + 1))
explode = [0.1] * age
fig, ax = plt.subplots()
ax.pie(vals,
       labels=labels,
       explode=explode,
       autopct='%1.1f%%',
       shadow=True,
       wedgeprops={
           'lw': 1,
           'ls': '--',
           'edgecolor': 'k'
       },
       rotatelabels=True)

ax.axis('equal')
plt.show()

# гистограммы

table1 = list(zip(Y, Am_list))
table2 = list(zip(Y, Am_list_2))

tfame1 = pd.DataFrame(table1, columns=['Y', 'Am_list'])
tfame2 = pd.DataFrame(table2, columns=['Y', 'Am_list_2'])
plt.bar(tfame1['Y'], tfame1['Am_list'])
plt.show()

# plt.bar(tfame1['Y'], tfame2['Am_list_2'])
# plt.show()

# # КОМАНДА №6

# # Контейнер расчета

# from sympy import *

# k, T, C, L = symbols('k T C L')

# print("КОМАНДНОЕ ЗАДАНИЕ (КОМАНДА №6)")

# # 1 (линейное)

# C_ost = 15_000
# Am_list = []
# C_ost_list = []
# age = 8

# for i in range(age):
#     Am = (C - L) / T
#     sl = Am.subs({C: 15_000, T: age, L: 0})
#     C_ost -= sl
#     Am_list.append(round(sl, 2))
#     C_ost_list.append(round(C_ost, 2))

# print("Первый контейнер:")
# print('Am_list: ', Am_list)
# print('C_ost_list: ', C_ost_list)

# # 2 (уменьшаемый остаток)

# Aj = 0
# C_ost = 15_000
# Am_list_2 = []
# C_ost_list_2 = []
# k_val = 2

# for i in range(age):
#     Am = k * 1 / T * (C - Aj)
#     sl = Am.subs({C: 15_000, T: age, k: k_val})
#     C_ost -= sl
#     Aj += Am
#     Am_list_2.append(round(sl, 2))
#     C_ost_list_2.append(round(C_ost, 2))

# print('Am_list_2: ', Am_list_2)
# print('C_ost_list_2: ', C_ost_list_2)
# print()

# # Контейнер табличного вывода

# import pandas as pd

# Y = range(1, age + 1)
# table1 = list(zip(Y, C_ost_list, Am_list))
# table2 = list(zip(Y, C_ost_list_2, Am_list_2))

# tfame1 = pd.DataFrame(table1, columns=['Y', 'C_ost_list', 'Am_list'])
# tfame2 = pd.DataFrame(table2, columns=['Y', 'C_ost_list_2', 'Am_list_2'])

# print("Второй контейнер:")
# print(tfame1)
# print(tfame2)

# # Контейнер визуализации

# from matplotlib import pyplot as plt

# plt.plot(Y, tfame1['C_ost_list'], label='C_ost_list')
# plt.plot(Y, tfame2['C_ost_list_2'], label='C_ost_list_2')

# plt.show()

# # красивая круговая гистограмма для линейного

# vals = Am_list
# labels = list(range(1, age + 1))
# explode = [0.1] * age
# fig, ax = plt.subplots()
# ax.pie(vals,
#        labels=labels,
#        explode=explode,
#        autopct='%1.1f%%',
#        shadow=True,
#        wedgeprops={
#            'lw': 1,
#            'ls': '--',
#            'edgecolor': 'k'
#        },
#        rotatelabels=True)

# ax.axis('equal')
# plt.show()

# # красивая круговая гистограмма для нелинейного

# vals = Am_list_2
# labels = list(range(1, age + 1))
# explode = [0.1] * age
# fig, ax = plt.subplots()
# ax.pie(vals,
#        labels=labels,
#        explode=explode,
#        autopct='%1.1f%%',
#        shadow=True,
#        wedgeprops={
#            'lw': 1,
#            'ls': '--',
#            'edgecolor': 'k'
#        },
#        rotatelabels=True)

# ax.axis('equal')
# plt.show()

# # гистограммы

# table1 = list(zip(Y, Am_list))
# table2 = list(zip(Y, Am_list_2))

# tfame1 = pd.DataFrame(table1, columns=['Y', 'Am_list'])
# tfame2 = pd.DataFrame(table2, columns=['Y', 'Am_list_2'])
# plt.bar(tfame1['Y'], tfame1['Am_list'])
# plt.show()

# # С НАПАРНИЦЕЙ СОВПАЛИ
# # plt.bar(tfame1['Y'], tfame2['Am_list_2'])
# # plt.show()

# # import os

# # my_secret = os.environ['MY_SECRET']
# # print(my_secret)
