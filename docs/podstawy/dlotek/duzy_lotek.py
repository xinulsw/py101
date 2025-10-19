#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

try:
    n = int(input('Podaj ilość typowanych liczb: '))
    maks = int(input('Podaj maksymalną losowaną liczbę: '))
    if n > maks:
        print('Błędne dane!')
        exit()
except ValueError:
    print('Błędne dane!')
    exit()

liczby = []
i = 0
while i < n:
    liczba = random.randint(1, maks)
    if liczby.count(liczba) == 0:
        liczby.append(liczba)
        i = i + 1

print(f'Wytypuj {n} z {maks} liczb: ')
typy = set()
j = 0
while j < n:
    try:
        typ = int(input(f'Podaj liczbę {j+1}: '))
    except ValueError:
        print('Błędne dane!')
        continue

    if 0 < typ <= maks and typ not in typy:
        typy.add(typ)
        j = j + 1

print()
trafione = set(liczby) & typy
if trafione:
    print(f'Trafione liczby: {trafione}')
    print(f'Liczba trafień {len(trafione)}')
else:
    print('Brak trafień. Spróbuj jeszcze raz!')

print('Wylosowane liczby:', liczby)
