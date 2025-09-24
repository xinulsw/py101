Instrukcja warunkowa
####################

.. note::

    W tym przykładzie poznasz instrukcje warunkową, która steruje działaniem programu.

Specyfikacja zadania 1
**********************

**Zadanie:**

Napisz program, który pobiera od użytkownika imię oraz rok urodzenia i wypisuje podane niżej komunikaty.

**Dane**:

* ``imie`` – ciąg znaków pobierany z klawiatury, imię użytkownika
* ``akt_rok`` – liczba całkowita, aktualny rok pobierany z klawiatury
* ``py_rok`` – liczba całkowita, rok powstania języka Python
* ``rok_urodzenia`` – liczba całkowita pobierana z klawiatury, rok urodzenia użytkownika

**Wynik**:

* komunikaty wypisane na ekranie:

.. code::

    Witaj *imie*! Mów mi Python.
    Mam *wiek_py* lat, ty masz *wiek_u*.
    Jestem starszy od ciebie!
    lub:
    Jestem młodszy od ciebie lub mamy tyle samo lat!

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: przyklad_01.py
    :linenos:

Instrukcja warunkowa ``if wyrażenie:`` (jeżeli) steruje warunkowym wykonaniem kodu.
Jeżeli podane wyrażenie logiczne jest prawdziwe (ma wartość ``True``), wykonywany jest następujący wcięty blok kodu.
Słowo kluczowe ``else:`` (w przeciwnym razie) jest opcjonalne. Następujący po nim blok kodu wykonywany jest,
jeżeli wyrażenie jest fałszywe (ma wartość ``False``).

Składnia
********

* Części instrukcji warunkowej kończymy dwukropkiem, które zapowiadają bloki kodu.
* Blok kodu może zawierać jedną lub wiele instrukcji.
* Bloki kodu wyodrębniane są za pomocą wcięć.
* Wcięcie pierwszego poziomu to 4 spacje, a każdy następny poziom to wielokrotność (8, 16, itd. spacji).

Ćwiczenia
*********

Zmień program tak, aby na końcu wypisany został tylko jeden z trzech komunikatów:

.. code-block::

    Jestem starszy od ciebie!
    Jestem młodszy od ciebie!
    Mamy tyle samo lat!

.. tip::

    Użyj kilku funkcji warunkowych.

.. admonition:: Pojęcia

    :term:`instrukcja warunkowa`, :term:`wyrażenie logiczne`, :term:`blok kodu`, :term:`formatowanie kodu`

.. _trojkat:

Specyfikacja zadania 2
**********************

**Zadanie**:

Napisz program, który na podstawie danych pobranych od użytkownika,
czyli długości boków, sprawdza, czy da się zbudować trójkąt i czy jest to trójkąt prostokątny.
Jeżeli da się zbudować trójkąt, należy wydrukować jego obwód i pole, w przeciwnym wypadku
komunikat, że nie da się utworzyć trójkąta.

**POJĘCIA**: *pętla for, obiekt, typ danych, metoda, lista, instrukcja warunkowa zagnieżdżona*.

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: 01_trojkat.py
    :linenos:

Pętla ``while`` działa podobnie jak w poprzednim przykładzie, ale wykorzystuje
warunek sformułowany przy wykorzystaniu operatora "różne od": ``!=``.

Metoda ``split(",")`` zwraca listę napisów wyodrębnionych z podanego ciągu.
Lista (zob. :term:`lista`) to sekwencja uporządkowanych danych,
np. ['3', '4', '5']. Do przeglądania takich sekwencji używa się pętli ``for``.

Pętla ``for zmienna in sekwencja`` odczytuje kolejne elementy *sekwencji*
i udostępnia je w *zmiennej*. W ciele pętli zmienną skonwertowaną na liczbę
całkowitą dodajemy do nowej listy za pomocą metody ``append()``.

Zapis ``a, b, c = lista`` jest przykładem rozpakowania listy, co polega
na przypisaniu zmiennym z lewej strony kolejnych wartości z listy.

.. note::

    Pętle, które wykonują jakieś operacje na sekwencjach i zapisują je w listach
    zastępuje się w Pythonie tzw. wyrażeniami listowymi. Zostaną one omówione
    w kolejnych przykładach.

Operatory logiczne:

* ``and`` – koniunkcja ("i"), wskazuje, że obydwa warunki muszą być prawdziwe;
* ``or`` – alternatywa ("lub"), przynajmniej jeden z podanych warunków powinien
  być prawdziwy.

Działania matematyczne:

* ``x**y`` – podnoszenie podstawy ``x`` do potęgi ``y``;
* ``sqrt()`` – funkcja z modułu ``math``, oblicza pierwiastek kwadratowy.
