from docs.podstawy.elotek.modul_lotek import wypisz_wyniki
from modul_lotek import wczytaj_ustawienia, pobierz_ustawienia, zapisz_ustawienia
from modul_lotek import losuj_liczby, pobierz_typy


def main(args):
    nick = input('Podaj nick: ')
    dane = wczytaj_ustawienia(nick)
    if dane:
        print(f'Ustawienia:\nLiczb: {dane[1]}\nMaks: {dane[2]}\nTypowań: {dane[3]}')

    if not dane or input('Zmieniasz (t/n)? ').lower() == 't':
        dane = pobierz_ustawienia(nick)
        zapisz_ustawienia(nick, dane)

    mick, n, maks, ile_losowan = dane[0:1] + [int(x) for x in dane[1:4]]

    liczby = losuj_liczby(n, maks)

    for i in range(ile_losowan):
        typy = pobierz_typy(n, maks)
        if wypisz_wyniki(liczby, typy) == n:
            break

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
