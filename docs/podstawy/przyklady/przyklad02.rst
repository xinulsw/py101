Pętle
#####

.. note::

    W tym przykładzie poznasz instrukcje iteracyjne, tzw. pętle,
    pozwalające powtrzać określone operacje.

Zadanie
********

Napisz program :file:`alfabet.py`, który wypisze ``n`` początkowych małych i dużych liter alfabetu
w formacie: "mała - litera, duża - litera". Jeżeli ``n`` jest większe od 2, wypisuj po 2 litery w wierszu.

**Dane**:

* ``n`` – liczba całkowita oznaczająca liczbę liter do wypisania.

**Wynik**:

* wypisane pary małych i dużyc liter na ekranie, np.:

.. code::

    a - A, b - B
    c - C, d - D
    e - E

.. raw:: html

    <div class="code_no">Plik <i>alfabet.py</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: przyklad02.py
    :linenos:

Pętla ``while warunek`` umożliwia powtarzanie bloku operacji, dopóki warunek
jest prawdziwy. W tym wypadku dopóki zmienna *op* ma wartość "t".
Zwróć uwagę na operator porównania: ``==``.

W Pythonie wszystko jest obiektem. Każdy obiekt przynależy do jakiegoś typu
i ma jakąś wartość. Typ determinuje, jakie operacje można wykonać na wartości danego obiektu.
Funkcja ``input()`` zwraca pobrane dane jako napis (typ *string*).
Metoda ``split(separator)`` pozwala rozbić napis na składowe (w tym wypadku liczby).

Instrukcje warunkowe (``if``), jak i pętle, można zagnieżdżać stosując wcięcia.
Instrukcje o takich samych wcięciach tworzą bloki kodu.
W jednej złożonej instrukcji warunkowej można sprawdzać wiele warunków (``elif:``).

Zadania
-------

Sprawdź, co się stanie, jeśli podasz liczby oddzielone przecinkiem lub podasz
za mało liczb. Zmień program tak, aby poprawnie interpretował dane oddzielane przecinkami.

**POJĘCIA**: *pętla while, obiekt, typ danych, metoda, instrukcja warunkowa zagnieżdżona*.