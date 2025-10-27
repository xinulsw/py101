from modul_lotek import wczytaj_ustawienia
from modul_lotek import pobierz_ustawienia, zapisz_ustawienia
from modul_lotek import losuj_liczby, pobierz_typy
from modul_lotek import wypisz_wyniki


def main(args):
    nick = input('Podaj nick: ')
    dane = wczytaj_ustawienia(nick)

    if dane:
        print(f'Ustawienia:\nLiczb: {dane[1]}\nMaks: {dane[2]}\nTypowań: {dane[3]}')

    if not dane or input('Zmieniasz (t/n)? ').lower() == 't':
        dane = pobierz_ustawienia(nick)
        zapisz_ustawienia(nick, dane)

    mick, n, maks, ile_typowan = dane[0:1] + [int(x) for x in dane[1:4]]
    print(mick, n, maks, ile_typowan)  # tę instrukcję można później zakomentować

    liczby = losuj_liczby(n, maks)

    for i in range(ile_typowan):
        typy = pobierz_typy(n, maks)
        if wypisz_wyniki(liczby, typy) == n:
            break

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
