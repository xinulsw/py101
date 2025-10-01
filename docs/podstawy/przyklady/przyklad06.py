from oceny_funkcje import drukuj, srednia, mediana, odchylenie


def main():
    przedmioty = {'polski', 'angielski'}  # definicja zbioru
    drukuj(przedmioty, 'Lista przedmiotów zawiera: ')

    while True:
        przedmiot = input('Podaj nazwę przedmiotu lub ENTER, żeby zakończyć: ')
        if len(przedmiot):
            if przedmiot in przedmioty:  # czy przedmiot jest w zbiorze?
                print('Ten przedmiot już mamy :-)')
            przedmioty.add(przedmiot)  # dodaj przedmiot do zbioru
        else:
            drukuj(przedmioty, '\nTwoje przedmioty: ')
            przedmiot = input('\nZ którego przedmiotu wprowadzisz oceny? ')
            # jeżeli przedmiotu nie ma w zbiorze
            if przedmiot not in przedmioty:
                print('Brak takiego przedmiotu, możesz go dodać.')
            else:
                break  # wyjście z pętli

    oceny = []  # pusta lista ocen
    ocena = None  # zmienna sterująca pętlą i do pobierania ocen
    while not ocena:
        try:
            ocena = int(input('Podaj ocenę (1-6) lub 0, aby zakończyć: '))
            if 0 < ocena < 7:
                oceny.append(float(ocena))
            elif ocena == 0:
                break
            else:
                print('Błędna ocena.')
            ocena = None
        except ValueError:
            print('Błędne dane!')

    drukuj(oceny, przedmiot.capitalize() + ' - wprowadzone oceny: ')
    s = srednia(oceny)
    m = mediana(oceny)
    o = odchylenie(oceny, s)
    print('\nŚrednia: {0:5.2f}'.format(s))
    print('Mediana: {0:5.2f}\nOdchylenie: {1:5.2f}'.format(m, o))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main())
