.. _przyklad2:

Instrukcja warunkowa
####################

.. note::

    W tym przykładzie poznasz różne postaci instrukcji warunkowej, za pomocą której sterujemy działaniem programu.

Zadanie
************

Uzupełnij program :file:`witaj.py` z :ref:`przykładu 1 <przyklad1>`, który pobiera od użytkownika imię oraz rok urodzenia i wypisuje podane niżej komunikaty.

**Wynik**:

* komunikaty wypisane na ekranie:

.. code::

    Witaj *imie*! Mów mi Python.
    Mam *wiek_py* lat, ty masz *wiek_u*.
    Jestem starszy od ciebie!
    lub:
    Jestem młodszy od ciebie lub mamy tyle samo lat!

.. raw:: html

    <div class="code_no">Plik <i>witaj.py</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: przyklad_02.py
    :linenos:
    :emphasize-lines: 17-21

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

Ćw. 1 – kilka warunków
***********************

Zmień program :file:`witaj.py` tak, aby na końcu wypisany został **tylko jeden** z trzech komunikatów:

.. code-block::

    Jestem starszy od ciebie!
    Jestem młodszy od ciebie!
    Mamy tyle samo lat!

Można użyć kilku osobnych instrukcji warunkowych:

.. code-block::

    if warunek_1:
        pass
    if warunek_2:
        pass
    if warunek_3:
        pass

Można użyć instrukcji warunkowych zagnieżdżonych:

.. code-block::

    if warunek_1:
        pass
    else:
        if warunek_2:
            pass
        else:
            pass

Można użyć jednej złożonej instrukcji warunkowej, w której sprawdzamy kolejne warunki za pomocą
słowa kluczowego ``elif``:

.. code-block::

    if warunek_1:
        pass
    elif warunek_2:
        pass
    else:
        pass

Ćw. 2 – Najmniejsza liczba
***************************

Napisz program :file:`najmniejsza.py`, który pobiera trzy liczby całkowite i wypisuje najmniejszą z nich.

.. tip::

    Zadanie wymaga użycia zagnieżdżonych instrukcji warunkowych.

Ćw. 3 – Trójkąt
****************

Napisz program :file:`trojkat.py`, który pobiera długości trzech boków trójkąta i sprawdza, czy da się
z nich zbudować trójkąt. Jeżeli tak, program powinien wypisać komunikat "Da się", w przeciwnym razie "Nie da się".

.. tip::

    Trójkąt mozna zbudować wtedy, kiedy suma dwóch dowolnych boków jest większa od trzeciego.
    Do sprawdzenia są więc trzy warunki.

Jeżeli kilka warunków ma być spełnionych jednocześnie, można je połączyć za pomocą operatora logicznej
koniunkcji ``and``:

.. code-block::

    if warunek1 and warunek2:
        pass

Jeżeli szukamy przynajmniej jednego prawdziwego warunku, warunki można połączyć za pomocą operatora logicznej
alternatywy ``or``:

.. code-block::

    if warunek1 or warunek2:
        pass

- Do programu :file:`trojkat.py` dopisz kod, który jeżeli da się zbudować trójkąt, sprawdzi, czy jest to
   trójkąt prostokątny i wypisze komunikat "Prostokątny" lub "Nieprostokątny".

.. tip::

    Przydatne działania matematyczne:

    * ``x**y`` – podnoszenie podstawy ``x`` do potęgi ``y``;
    * ``sqrt()`` – funkcja oblicza pierwiastek kwadratowy, aby jej użyć na początku skryptu umieszczamy
      import: ``from math import sqrt``.

- Do programu :file:`trojkat.py` dopisz kod, który jeżeli da się zbudować trójkąt, obliczy i wypisze obwód oraz pole.

.. admonition:: Pojęcia

    :term:`instrukcja warunkowa`, :term:`wyrażenie logiczne`, :term:`blok kodu`, :term:`formatowanie kodu`
