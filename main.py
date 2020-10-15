from myClasses.Auto import Auto
from myModules.utils import majuscule, minuscule, capitalize, add_mult, replace
from myClasses.Auto import Auto
from myClasses.Moto import Moto
from myClasses.Duree import Duree
import os

# from myModules import utils

str1 = 'Hello World'
print('str :', str1)

# *********** functions
strMaj = majuscule(str1)
print('strMaj :', strMaj)

strMin = minuscule(str1)
print('strMin :', strMin)

strCap = capitalize(str1)
print('strMin :', strCap)

# *********** list
lst1 = ['aaa', 'abc', 'try', '123']
print('list1 type:', type(lst1))
for e in lst1:
    print(majuscule(e))

for i, e in enumerate(lst1):
    print(i, minuscule(e))

# *********** tuples
tpl = add_mult(4, 2)
print('tpl type :', type(tpl))
print('tpl :', tpl)
print('tpl[0] :', tpl[0])
print('tpl[1] :', tpl[1])

a, b = add_mult(8, 9)
print("a :", a, 'b :', b)

# *********** dict
dct1 = {
    'prenom': 'patrick',
    'nom': 'tarnaud',
    'age': 50
}
print('dct1 type :', type(dct1))
print("dct1['prenom'] :", dct1['prenom'])
print("dct1['nom'] :", dct1['nom'])
print("dct1['age'] :", dct1['age'])

print('keys')
for k in dct1.keys():
    print(type(k), k)
print('values')
for v in dct1.values():
    print(type(v), v)
print('items')
for e in dct1.items():
    print(type(e), e)

# *********** list manipulation
lst2 = ['aaa', 'abc', 'try', 123]
print([majuscule(c) for c in lst2 if isinstance(c, str)])
print([majuscule(c) for c in lst2 if type(c) == str])
print([capitalize(e) for e in [majuscule(c) for c in lst2 if type(c) == str]])

# *********** functions with default params
lst3 = ['aaa', 'Abc', 'atry', 123]
print(lst3)
print([replace(e) for e in lst3 if type(e) == str])
print([replace(e, 't', 'u') for e in lst3 if type(e) == str])

# *********** classes
a1 = Auto('VW', 1200, 'blue', 1200)
a2 = Auto('VW', 1200, 'red', 900)
print('a1', a1)
print('a2', a2)
print('a1==a2', a1 == a2)
m1 = Moto('BMW', 250, 310, 'orange')
print('m1', m1)
a2.nb_doors = 10
print('a2', a2)
print('a2=a1')
a2 = a1
a2.nb_doors = 8
print('a1', a1)
print('a2', a2)

print(os.getcwd())

# *********** property
a1 = Auto('VW', 1200, 'blue', 1200)
a2 = Auto('VW', 1200, 'red', 900)
print('a1', a1)
print('a2', a2)
print(a1.color)
print(a2.color)
a1.color = 'yellow'
a2.color = 'green'
print(a1.color)
print(a2.color)
print(a1._color)

# surcharges opérateurs
d1 = Duree(45, 20)
d2 = Duree(1, 20)
d = d1 + d2
print(d)
d3 = d + 20
print(d3)
d4 = 4 + d3
print(d4)
