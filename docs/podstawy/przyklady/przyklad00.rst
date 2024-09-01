Mów mi Python!
##############

Zadanie
*******

Napisz program, który pobiera od użytkownika *imię* oraz *wiek* i wypisuje komunikat:

.. code::

    Witaj *imie*.
    Mów mi Python, mam *wiek_py* lat.

Wartość zmiennej ``wiek_py``, czyli wiek Pythona, należy wyliczyć.

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: przyklad_00.py
    :linenos:

**Zmienne** służą do zapamiętywania używanych w programie wartości, np. napisów lub liczb.
Tworzymy je poprzez **przypisanie wartości** określonego typu za pomocą operatora `=`.
Przypisywane wartości mogą być wyrażeniami, np. działaniami arytmetycznymi lub logicznymi.

Do **pobierania danych** z klawiatury (domyślne wejście) i **wypisywania komunikatów** na ekranie (domyślne wyjście)
służą wbudowane funkcje:

* ``input()`` – zwraca pobrane z klawiatury znaki jako napis (ciąg znaków).
* ``print()`` – wypisuje podane argumenty oddzielone przecinkami.
* ``int()`` – funkcja umożliwia zamianę napisu na liczbę całkowitą.

Składnia
========

* Nazwy zmiennych nie powinny zawierać znaków narodowych,
  w Pythonie preferuje się małe litery oraz łączenie członów nazwy znakiem podkreślenia `_`.
* **Napisy** w kodzie źródłowym, czyli stałe znakowe, ujmujemy w cudzysłowy podwójne lub pojedyncze.
* Znak ``#`` oznacza 1-liniowy komentarz, który nie jest interpretowany.

Zadania
=======

Zmień program tak, aby wartość zmiennej `akt_rok` (aktualny rok) była podawana przez użytkownika na początku programu.

.. tip::

    Użyj funkcji ``input()`` oraz ``int()``.

.. admonition:: Pojęcia
    
    :term:`zmienna`, wartość, :term:`typ danych`, wyrażenie, wejście i wyjście, komentarz
