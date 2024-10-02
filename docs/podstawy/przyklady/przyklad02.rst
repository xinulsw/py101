Instrukcje warunkowe
####################

Zadanie
*******

Napisz program, który Pobiera od użytkownika trzy liczby całkowite i wypisuje najmniejszą z nich, sprawdź, która jest najmniejsza i wydrukuj ją na ekranie.

**POJĘCIA**: *pętla while, obiekt, typ danych, metoda, instrukcja warunkowa zagnieżdżona*.

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: 01_if.py
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