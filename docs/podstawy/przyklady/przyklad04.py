from random import randint

n = int(input('Ile liczb podasz? '))
lista = []  # pusta lista
for i in range(n):
    liczba = int(input('Podaj liczbę: '))
    lista.append(liczba)
print('Podane liczby:', lista)

print('Elementy i indeksy:')
for i in range(n):
    # wypisuje: element (indeks)
    print(f'{lista[i]} ({i})', end=' ')
print()

print('Elementy i indeksy:')
for i, e in enumerate(lista):
    print(f'{i} ({e})', end=' ')
print()

print('Elementy w porządku malejącym:')
for e in reversed(lista):
    print(e, end=' ')
print()

print('Elementy w porządku rosnącym:')
for e in sorted(lista):
    print(e, end=' ')
print()

el = int(input('Podaj element, którego wystąpienia należy zliczyć: '))
if el in lista:
    print('Liczba wystąpień:', lista.count(el))
    print('Indeks pierwszego wystąpienia:', lista.index(el))
else:
    print('Brak elementu w liście!')

el_1 = int(input('Podaj liczbę do usunięcia: '))
lista.remove(el_1)
print(lista)



in_1 = int(input('Podaj indeks elementu do usunięcia: '))
el = lista.pop(in_1)
print(f'Usunięto {el} z listy', lista)

print('Wstawianie elementów do listy')
a, i = eval(input('Podaj element i indeks oddzielone przecinkiem: '))
lista.insert(i, a)
print(lista)

print('Część listy (notacja wycinkowa):')
i, j = eval(input('Podaj indeks początkowy i końcowy oddzielone przecinkiem: '))
print(lista[i:j])

print()
print('Tupla to lista niemodyfikowalna.')
print('Próba zmiany tupli generuje błąd:')
tupla = tuple(lista)
tupla[0] = 100
