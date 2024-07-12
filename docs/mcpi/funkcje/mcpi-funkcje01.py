#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import numpy as np  # import biblioteki do obliczeń naukowych
import matplotlib.pyplot as plt  # import biblioteki do tworzenia wykresów
import mcpi.minecraft as minecraft  # import modułu minecraft
import mcpi.block as block  # import modułu block

os.environ["USERNAME"] = "Steve"  # wpisz dowolną nazwę użytkownika
os.environ["COMPUTERNAME"] = "mykomp"  # wpisz dowolną nazwę komputera

mc = minecraft.Minecraft.create("192.168.1.10")  # połaczenie z mc


def plac(x, y, z, roz=10, gracz=False):
    """
    Funkcja tworzy podłoże i wypełnia sześcienny obszar od podanej pozycji,
    opcjonalnie umieszcza gracza w środku.
    Parametry: x, y, z - współrzędne pozycji początkowej,
    roz - rozmiar wypełnianej przestrzeni,
    gracz - czy umieścić gracza w środku
    Wymaga: globalnych obiektów mc i block.
    """

    podloga = block.STONE
    wypelniacz = block.AIR

    # podloga i czyszczenie
    mc.setBlocks(x, y - 1, z, x + roz, y - 1, z + roz, podloga)
    mc.setBlocks(x, y, z, x + roz, y + roz, z + roz, wypelniacz)
    # umieść gracza w środku
    if gracz:
        mc.player.setPos(x + roz / 2, y + roz / 2, z + roz / 2)


def wykres(x, y, tytul="Wykres funkcji", *extra):
    """
    Funkcja wizualizuje wykres funkcji, której argumenty zawiera lista x
    a wartości lista y i ew. dodatkowe listy w parametrze *extra
    """
    if len(extra):
        plt.plot(x, y, extra[0], extra[1])  # dwa wykresy na raz
    else:
        plt.plot(x, y)
    plt.title(tytul)
    # plt.xlabel(podpis)
    plt.grid(True)
    plt.show()


def fun1(blok=block.IRON_BLOCK):
    """
    Funkcja f(x) = a*x + b
    """
    a = int(raw_input('Podaj współczynnik a: '))
    b = int(raw_input('Podaj współczynnik b: '))
    x = range(-10, 11)  # lista argumentów x = <-10;10> z krokiem 1
    y = [a * i + b for i in x]  # wyrażenie listowe
    print x, "\n", y
    wykres(x, y, "f(x) = a*x + b")
    for i in range(len(x)):
        mc.setBlock(x[i], 1, y[i], blok)


def main():
    mc.postToChat("Funkcje w Minecrafcie")  # wysłanie komunikatu do mc
    plac(-80, 0, -80, 160)
    mc.player.setPos(22, 10, 10)
    fun1()
    return 0


if __name__ == '__main__':
    main()
