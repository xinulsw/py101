.. _maly-lotek:

Mały Lotek
###########

.. note::

    Przykład pokazuje użycie instrukcji wejścia i wyjścia, instrukcji iteracyjnej oraz warunkowej,
    a także generatora liczb pseudolosowych.

.. contents::
    :depth: 1
    :local:

Zadanie
********

Napisz program :file:`maly_lotek.py`, który losuje liczbę i daje użytkownikowi trzy szansy na jej odgadnięcie.

**Dane**:

* ``liczba`` – losowa liczba całkowita z zakresu <1; 10>, którą należy odgadnąć,
* ``typ`` – liczba całkowita pobierana z klawiatury,

**Wynik** to wypisane komunikaty:

* "Zgadłeś!" – jeżeli użytkownik odgadł wylosowaną liczbę,
* "Nie zgadłeś. Spróbuj jeszcze raz." – jeżeli użytkownik nie zgadł, ale ma jeszcze szanse,
* "Miałem na myśli liczbę: liczba" – jeżeli użytkownik nie odgadł wylosowanej liczby.

Losowanie liczby
****************

Korzystanie z generatora liczb pseudolosowych umożliwia moduł ``random``. Zawiera on m.in. funkcję ``randint(a, b)``,
która zwraca liczbę z zakresu ``<a; b>``:

.. raw:: html

    <div class="code_no">Plik <i>maly_lotek.py</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: maly_lotek.py
    :linenos:
    :lineno-start: 1
    :lines: 1-5

Pobieranie typów
****************

Trafienie za pierwszym razem wylosowanej liczby jest bardzo trudne, damy
graczowi 3 szanse. Uzupełniamy kod:

.. raw:: html

    <div class="code_no">Plik <i>maly_lotek.py</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: maly_lotek.py
    :linenos:
    :lineno-start: 6
    :lines: 6-10

Pobieranie i sprawdzanie kolejnych liczb wymaga powtórzeń, czyli **pętli** (zob. :term:`pętla`).
Ponieważ wiemy, że użytkownik ma trzy szanse, zastosujemy pętlę ``for i in range(3):``.
W każdym powtórzeniu wypisujemy numer próby i pobieramy z klawiatury liczbę całkowitą, którą zapisujemy w zmiennej:
``typ = int(input('Jaką liczbę od 1 do 10 mam na myśli? '))``.

.. attention::

    Zakładamy na razie, że gracz wprowadza poprawne dane, czyli liczby całkowite!

Sprawdzanie typów
******************

Do sprawdzenia, czy użytkownik odgadł wylosowaną liczbę, musimy skorzystać ze złożonej instrukcji warunkowej:

.. raw:: html

    <div class="code_no">Plik <i>maly_lotek.py</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: maly_lotek.py
    :linenos:
    :lineno-start: 11
    :lines: 11-19

Jeżeli zmienne ``liczba `` i ``typ`` zawierają tę samą wartość, wypisujemy komunikat o sukcesie.
W przeciwnym  razie jeżeli pobrano trzeci typ i nie był on trafny, wypisujemy wylosowaną liczbę,
w przeciwnym razie wypisujemy komunikat, żeby spróbować jeszcze raz.

Ćwiczenie 1
=============

* Zgadywanie, gdy losowana liczba jest drukowana, nie jest zabawne. Zakomentuj
  więc instrukcję drukowania: ``# print("Wylosowana liczba:", liczba``) – będzie pomijana
  przez interpreter.

* Dopisz odpowiednie polecenie, które wyświetli liczbę podaną przez gracza.
  Przetestuj jego działanie.

.. attention::

    Uwaga na WCIĘCIA!

    Podporządkowane bloki kodu wyodrębniamy za pomocą wcięć (zob. :term:`formatowanie kodu`).
    Standardem są 4 spacje i ich wielokrotności. Przyjęty rozmiar wcięć obowiązuje w całym pliku.
    Błędy wcięć sygnalizowane są komunikatem ``IndentationError``.

    W naszym kodzie linie 10, 13, 16 wcięte są na 4 spacje, zaś 14-15, 17-18 na 8.

Ćwiczenie
*********

W trybie interaktywnym interpretera Pythona sprawdź:

1) działanie funkcji ``randint()``:

.. code-block:: bash

    ~$ python3
    >>> list(range(30))
    >>> for i in range(0, 100, 2)
    ...   print i
    ...
    >>> exit()

Funkcja ``range()`` może przyjmować opcjonalne parametry określające początek, koniec
oraz krok generowanej listy wartości.

Materiały
**********

**Źródła:**

* :download:`Mały Lotek <mlotek.zip>`