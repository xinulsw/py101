.. _extra-lotek:

Extra Lotek
###########

Kod "Dużego Lotka" wypracowany w poprzednim przykładzie zilustrował m.in.,
jak używać pętli warunkowej do pobierania danych z klawiatury,
jak sprawdzać poprawność wprowadzanych danych oraz jak używać list i zbiorów
jako złożonych struktur danych. Uzyskany skrypt wygląda następująco:

.. raw:: html

    <div class="code_no">Plik <i>duzy_lotek.py</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: duzy_lotek.py
    :linenos:

.. note::

    Przykład "Extra Lotek" pokazuje jak używać funkcji i modułów oraz
    jak zapisywać i odczytywać dane z plików tekstowych w różnych formatach.

Zadanie
*******

Napisz program :file:`extra_lotek.py`, który losuje ``n`` liczb naturalnych
z podanego zakresu ``maks``, a następnie pobiera z klawiatury ``n`` typów, sprawdza i wypisuje,
ile z nich zostało trafionych. Pobieranie typów, sprawdzanie i wypisywanie wyników
powtarza się tyle razy, ile poda użytkownik. Dodatkowo program powinien:

* sprawdzać poprawność podawanych danych wejściowych,
* zapisywać w pliku i odczytywać dane wejściowe: nick użytkownika, liczbę losowanych liczb,
  wartość maksymalną oraz liczbę typowań,
* pozwalać na zmianę danych wejściowych.

**Dane**:

* ``nick`` – nick użytkownika, ciąg znaków pobierany z klawiatury,
* ``n`` – liczba całkowita pobierana z klawiatury,
* ``maks`` – liczba całkowita pobierana z klawiatury,
* ``ile_typowan`` – liczba całkowita pobierana z klawiatury,
* ``typ`` – liczba całkowita pobierana z klawiatury z zakresu ``<0; maks>``.

**Wynik**

Komunikaty podczas pierwszego uruchomienia:

.. code::

    Podaj nick: adam
    Podaj liczbę losowanych liczb: 3
    Podaj maksymalną losowaną liczbę: 10
    Podaj liczbę typowań: 1
    Wytypuj 3 z 10 liczb:
    Podaj typ: 1
    Podaj typ: 3
    Podaj typ: 5

    Wylosowane liczby: [10, 3, 4]
    Trafione liczby: {3}
    Liczba trafień 1

Komunikaty po kolejnym uruchomieniu przez tego samego użytkownika:

.. code::

    Podaj nick: adam
    Ustawienia:
    Liczb: 3
    Maks: 10
    Typowań: 1
    Zmieniasz (t/n)? n
    Wytypuj 3 z 10 liczb:
    ...

Funkcje i moduły
*****************

Tam, gdzie w programie występują powtarzające się operacje lub zestaw poleceń
realizujący wyodrębnione zadanie, wskazane jest używanie funkcji.
Wyodrębnienie funkcji poprawia czytelność działania programu, ułatwia sprawdzanie i poprawianie kodu.

Często używane funkcje można umieszczać w osobnych modułach (zob. , :term:`moduł`), z których
importujemy je do różnych programów za pomocą instrukcji ``import`` lub ``from ... import``.

.. mote::

    Jeżeli program korzysta z niewielu i/lub unikalnych funkcji,
    można umieszczać je w jednym pliku na początku.

**Funkcja główna**

Jeżeli cały kod programu umieszczamy w funkcjach, to jedną z nich trzeba wywołać na początku, aby program zaczął
działać. Taka funkcja zwyczajowo nazywana jest ``main()`` i zazwyczaj zawiera logikę działania programu.

W nowym pliku :file:`extra_lotek.py` umieszczamy początkowy kod:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python

.. code::

    def main(args):
        nick = input('Podaj nick: ')

    if __name__ == '__main__':
        import sys
        sys.exit(main(sys.argv))

Funkcja w Pythonie to wyodrębniony i nazwany blok kodu.
Definicja funkcji zawiera: słowo kluczowe ``def``, nazwę funkcji,
obowiązkowe nawiasy okrągłe z opcjonalnymi parametrami oraz dwukropek.

Zmienne lokalne w funkcjach są niezależne od zmiennych w programie
głównym, ponieważ definiowane są w różnych zasięgach, a więc w różnych przestrzeniach nazw.
Możliwe jest modyfikowanie zmiennych globalnych dostępnych w całym programie,
o ile wskażemy je w funkcji instrukcją typu: ``global nazwa_zmiennej``.

Program główny po zmianach przedstawia się następująco:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: toto30.py
    :linenos:
    :emphasize-lines: 4, 7, 9, 12, 30-32

Na początku z modułu ``totomodul``, którego nazwa jest taka sama jak nazwa pliku,
importujemy potrzebne funkcje. Następnie w funkcji głównej ``main()``
wywołujemy je podając nazwę i ewentualne argumenty.
Zwracane przez nie wartości zostają przypisane podanym zmiennym.

Warto zauważyć, że funkcja może zwracać więcej niż jedną wartość naraz,
np. w postaci krotki ``return (ile, maks, ilelos)`` (zob. :term:`krotka`).

Wiele wartości zwracanych w krotce można jednocześnie przypisać
kilku zmiennym dzięki operacji tzw. **rozpakowania krotki**:
``ileliczb, maksliczba, ilerazy = ustawienia()``. Należy jednak
pamiętać, aby liczba zmiennych z lewej strony wyrażenia odpowiadała liczbie
elementów w krotki.

Konstrukcja ``while True`` oznacza nieskończoną pętlę. Stosujemy ją w funkcji
``ustawienia()``, aby wymusić na użytkowniku podanie poprawnych danych.

Cały program zawarty został w funkcji głównej ``main()``. O tym, czy zostanie
ona wykonana decyduje warunek ``if __name__ == '__main__':``, który będzie
prawdziwy, kiedy nasz skrypt zostanie uruchomiony jako główny.
Wtedy nazwa specjalna ``__name__`` ustawiana jest na ``__main__``.
Jeżeli korzystamy ze skryptu jako modułu, importując go,
``__main__`` ustawiane jest na nazwę pliku, dzięki czemu kod się nie wykonuje.

.. note::

    **Komentarze**: w rozbudowanych programach dobrą praktyką ułatwiającą późniejsze przeglądanie
    i poprawianie kodu jest opatrywanie jego fragmentów **komentarzami**. Zazwyczaj umieszczamy
    je po znaku ``#``. Z kolei funkcje opatruje się krótkim opisem
    działania i/lub wymaganych argumentów, ograniczanym **potrójnymi cudzysłowami**.
    Notacja ``"""..."""`` lub ``'''...'''`` pozwala zamieszczać teksty wielowierszowe.


Ćwiczenie
==========

* Przenieś kod powtarzany w pętli ``for`` (linie 17-24) do funkcji zapisanej w module
  programu.Wywołanie funkcji: ``iletraf = wyniki(set(liczby), typy)`` umieść w linii 17
  programu głównego. Wykorzystaj szkielet funkcji:

.. code-block:: python

    def wyniki(liczby, typy):
        """Funkcja porównuje wylosowane i wytypowane liczby,
        zwraca ilość trafień"""
        ...

        return len(trafione)


* Popraw wyświetlanie listy trafionych liczb. W funkcji ``wyniki()`` przed instrukcją
  ``print("Trafione liczby: %s" % trafione``) wstaw:
  ``trafione = ", ".join(map(str, trafione))``.

  Funkcja ``map()`` (zob. :ref:`mapowanie funkcji <map-fun>`) pozwala na zastosowanie
  jakiejś innej funkcji, w tym wypadku ``str`` (czyli konwersji na napis),
  do każdego elementu sekwencji, w tym wypadku zbioru ``trafione``.

  Metoda napisów ``join()`` pozwala połączyć elementy listy (muszą być typu *string*)
  podanymi znakami, np. przecinkami (``", "``).


Zapis/odczyt plików
*******************

Uruchamiając wielokrotnie program, musimy podawać wiele danych, aby zadziałał.
Dodamy więc możliwość zapamiętywania ustawień i ich zmiany. Dane zapisywać
będziemy w zwykłym pliku tekstowym. W pliku :file:`toto2.py` dodajemy
tylko jedną zmienną ``nick``:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: toto32.py
    :linenos:
    :emphasize-lines: 2
    :lineno-start: 8
    :lines: 8-9

W pliku :file:`totomodul.py` zmieniamy funkcję ``ustawienia()`` oraz dodajemy
dwie nowe: ``czytaj_ust()`` i ``zapisz_ust()``.

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: totomodul32.py
    :linenos:
    :emphasize-lines: 14, 21, 34-35, 37, 42, 51
    :lineno-start: 1
    :lines: 1-55

**Operacje na plikach**:

* ``plik = open(nazwapliku, tryb)`` – otwarcie pliku w trybie ``"w"`` (zapis), "r" (odczyt) lub "a" (dopisywanie);
* ``plik.readline()`` – odczytanie pojedynczej linii z pliku;
* ``plik.write(napis)`` – zapisanie podanego napisu do pliku;
* ``plik.close()`` – zamknięcie pliku.

**Operacje na tekstach**:

* operator ``+``: konkatenacja, czyli łączenie tekstów,
* ``linia.split(";")`` – rozbijanie tekstu wg podanego znaku na elementy listy,
* ``";".join(gracz)`` – wspomniane już złączanie elementów listy za pomocą podanego znaku,
* ``odp.lower()`` – zmiana wszystkich znaków na małe litery,
* ``str(arg)`` – przekształcanie podanego argumentu na typ tekstowy.

W funkcji ``ustawienia()`` pobieramy nick użytkownika i tworzymy nazwę pliku
z ustawieniami, następnie próbujemy je odczytać wywołując funkcję ``czytaj_ust()``.
Funkcja ta sprawdza, czy podany plik istnieje na dysku i otwiera go do odczytu.
Plik powinien zawierać 1 linię, która przechowuje ustawienia w formacie:
``nick;ile_liczb;maks_liczba;ile_prób``. Po jej odczytaniu i rozbiciu na elementy
(``linia.split(";")``) zwracamy ją jako listę ``gracz``.

Jeżeli uda się odczytać zapisane ustawienia, pytamy użytkownika,
czy chce je zmienić. Jeżeli brak ustawień lub użytkownik chce je zmienić,
pobieramy informacje, tworzymy z nich listę i przekazujemy do zapisania:
``zapisz_ust(nazwapliku, gracz)``.

Ponieważ w programie głównym oczekujemy, że funkcja ``ustawienia()``
zwróci dane typu *napis, liczba, liczba, liczba* – używamy konstrukcji:
``return gracz[0:1] + [int(x) for x in gracz[1:4]]``.

Na początku za pomocą notacji wycinkowej (ang. *slice*, :term:`notacja wycinkowa`)
tworzymy 1-elementową listę zawierającą nick użytkownika (``gracz[0:1]``).
Pozostałe elementy z listy ``gracz`` (``gracz[1:4]``) umieszczamy w wyrażeniu listowym
(:term:`wyrażenie listowe`). Przy użyciu pętli przekształca ono każdy element
na liczbę całkowitą i umieszcza w nowej liście.

Na końcu operator ``+`` ponownie tworzy nową listę, która zawiera wartości oczekiwanych typów.

Ćwiczenie
=========

Przećwicz w konsoli notację wycinkową, wyrażenia listowe i łączenie list:

.. code-block:: bash

    ~$ python3
    >>> dane = ['a', 'b', 'c', '1', '2', '3']
    >>> dane[0:3]
    >>> dane[3:6]
    >>> duze = [x.upper() for x in dane[0:3]]
    >>> kwadraty = [int(x)**2 for x in dane[3:6]]
    >>> duze + kwadraty

Słowniki
******************

Skoro umiemy już zapamiętywać wstępne ustawienia programu, możemy również
zapamiętywać losowania użytkownika, tworząc rejestr do celów informacyjnych
i/lub statystycznych. Zadanie wymaga po pierwsze zdefiniowania jakieś struktury,
w której będziemy przechowywali dane, po drugie zapisu danych albo w plikach,
albo w bazie danych.

Na początku dopiszemy kod w programie głównym :file:`toto2.py`:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: toto33.py
    :linenos:
    :emphasize-lines: 4-6, 19-31
    :lineno-start: 1
    :lines: 1-

Dane graczy zapisywać będziemy w plikach nazwanych nickiem użytkownika
z rozszerzeniem ".json": ``nazwapliku = nick + ".json"``.
Informacje o grach umieścimy w liście ``losowania``, którą na początku
zainicjujemy danymi o grach zapisanymi wcześniej: ``losowania = czytaj(nazwapliku)``.

Każda gra w liście ``losowania`` to :term:`słownik`. Struktura ta pozwala
przechowywać dane w parach "klucz: wartość", przy czym indeksami mogą być napisy:

* ``"czas"`` – będzie indeksem daty gry (potrzebny import modułu ``time``!),
* ``"dane"`` – będzie wskazywał tuplę z ustawieniami,
* ``"wylosowane"`` – listę wylosowanych liczb,
* ``"ile"`` – ilość trafień.

Na koniec dane ostatniej gry dopiszemy do listy (``losowania.append()``),
a całą listę zapiszemy do pliku: ``zapisz(nazwapliku, losowania)``.

Teraz zobaczmy, jak wyglądają funkcje ``czytaj_json()`` i ``zapisz_json()`` w module
:file:`totomodul.py`:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: totomodul33.py
    :linenos:
    :lineno-start: 102
    :lines: 102-

Kiedy czytamy i zapisujemy dane, ważną sprawą staje się ich format. Najprościej
zapisywać dane jako znaki, tak jak zrobiliśmy to z ustawieniami, jednak często
programy użytkowe potrzebują zapisywać złożone struktury danych, np.
listy, zbiory czy słowniki. Znakowy zapis wymagałby wtedy wielu dodatkowych
manipulacji, aby możliwe było poprawne odtworzenie informacji. Prościej
jest skorzystać z *serializacji*, czyli zapisu danych obiektowych (zob. :term:`serializacja`).
Często stosowany jest prosty format tekstowy `JSON <https://pl.wikipedia.org/wiki/JSON>`_.

W funkcji ``czytaj()`` zawartość podanego pliki dekodujemy do listy: ``dane = json.load(plik)``.
Funkcja ``zapisz()`` oprócz nazwy pliku wymaga listy danych. Po otwarciu
pliku w trybie zapisu ``"w"``, co powoduje wyczyszczenie jego zawartości,
dane są serializowane i zapisywane formacie JSON: ``json.dump(dane, plik)``.

Dobrą praktyką jest zwalnianie uchwytu do otwartego pliku i przydzielonych mu zasobów
poprzez jego zamknięcie: ``plik.close()``. Tak robiliśmy w funkcjach
czytających i zapisujących ustawienia. Teraz jednak pliki otworzyliśmy przy
użyciu konstrukcji typu ``with open(nazwapliku, "r") as plik:``, która zadba
o ich właściwe zamknięcie.

Przetestuj, przynajmniej kilkukrotnie, działanie programu.

Ćwiczenie
==============

Załóżmy, że jednak chcielibyśmy zapisywać historię losowań w pliku tekstowym,
którego poszczególne linie zawierałyby dane jednego losowania, np.:
``wylosowane:[4, 5, 7];dane:(3, 10);ile:0;czas:1434482711.67``

Funkcja zapisująca dane mogłaby wyglądać np. tak:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python

    def zapisz_str(nazwapliku, dane):
        """Funkcja zapisuje dane w formacie txt do pliku"""
        with open(nazwapliku, "w") as plik:
            for slownik in dane:
                linia = [k + ":" + str(w) for k, w in slownik.iteritems()]
                linia = ";".join(linia)
                # plik.write(linia+"\n") – zamiast tak, można:
                print >>plik, linia

Napisz funkcję ``czytaj_str()`` odczytującą tak zapisane dane. Funkcja
powinna zwrócić listę słowników.

Materiały
**********

**Źródła:**

* :download:`Extra Lotek <elotek.zip>`

:term:`funkcja`