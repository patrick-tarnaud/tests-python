from myClasses.Auto import Auto
from myModules.utils import majuscule, minuscule, capitalize, add_mult, replace
from myClasses.Auto import Auto
from myClasses.Moto import Moto
from myClasses.Duree import Duree
from myClasses.Etudiant import Etudiant
from myClasses.ListEtudiants import ListEtudiants
from operator import attrgetter
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

# sort
list1 = [9, 8, 7, 5, 7, 4]
list1.sort()
print(list1)
list1 = [9, 8, 7, 5, 7, 4]
list2 = sorted(list1)
print(list2)

list_init_etudiants = [
    Etudiant('Roger', 'Dupont', 22, 15),
    Etudiant('Robert', 'Jojo', 32, 18),
    Etudiant('Bob', 'Yeah', 48, 12),
    Etudiant('Sophie', 'Flash', 45, 12),
    Etudiant('Patrick', 'Ploua', 18, 19)
]

list_etudiants = list(list_init_etudiants)

print('liste étudiants non triée', list_etudiants)
print('*************************************************************')
list_etudiants.sort(key=lambda etudiant: etudiant.note_moyenne)
print('list_etudiants triée sur note_moyenne via list.sort(key=)\n', list_etudiants)

list_etudiants = list(list_init_etudiants)

print('list_etudiants triée sur note_moyenne via sorted(key=note_moyenne)\n',
      sorted(list_etudiants, key=lambda etudiant: etudiant.note_moyenne))
print('*************************************************************')

print('list_etudiants triée sur age via sorted(key=age)\n', sorted(list_etudiants, key=lambda etudiant: etudiant.age))
print('*************************************************************')

print('list_etudiants triée sur age en ordre inverse via sorted(key=age)\n',
      sorted(list_etudiants, key=lambda etudiant: etudiant.age, reverse=True))

print('*************************************************************')

print('list_etudiants triée sur note_moyenne via sorted(attrgetter(\'note_moyenne\'))\n',
      sorted(list_etudiants, key=attrgetter('note_moyenne')))
print('*************************************************************')

print('list_etudiants triée sur note_moyenne et sur age via sorted(attrgetter(\'note_moyenne\'))\n',
      sorted(list_etudiants, key=attrgetter('note_moyenne', 'age')))
print('*************************************************************')

print('** iteration normale - for')
for e in list_init_etudiants:
    print(e)

print('** iteration normale - print')
print(list_init_etudiants)

le = ListEtudiants(list_init_etudiants)
print('** iteration inverse - for')
for e in le:
    print(e)

print("** iteration inverse - print => le print n'appelle par __iter__")
print(le)


# generateur

def generateur():
    yield 1
    yield 2
    yield 3


print('generateur()', generateur())

# parcours manuel
it = iter(generateur())
print(next(it))
print(next(it))
print(next(it))

# parcours for in
for i in generateur():
    print(i)

# for i in range(3):
#     print(i)

list_etudiants = list(list_init_etudiants)


# le generateur évite de créer une classe héritant de list surchargeant la méthode __iter__ et de créer une classe
# d'itérateur sur la liste en définissant une méthode __next__ la classe ListEtudiants devient inutile. Le generateur
# implemente de maniere cachée le iter (code avant le yield), le next (le yield) et le raise StopIteration en sortie
def le_generateur(ple):
    # iter
    pos = len(ple) - 1
    while pos >= 0:
        # next
        yield ple[pos]
        pos -= 1
    # StopIteration


for e in le_generateur(list_etudiants):
    print(e)
