.. _przyklad5:

Ciąg Fibonacciego
#################

.. note::

    W tym przykładzie poznasz i zastosujesz **funkcje**

Zadanie
********

Wypisz ciąg Fibonacciego aż do ``n``-tego wyrazu podanego przez użytkownika.
Ciąg Fibonacciego to ciąg liczb naturalnych, którego każdy wyraz poza dwoma
pierwszymi jest sumą dwóch wyrazów poprzednich.
Początkowe wyrazy tego ciągu to: ``0 1 1 2 3 5 8 13 21``.

**Dane**:

- ``n`` – wyraz, na którym kończymy wypisywanie ciągu, liczba całkowita.

.. raw:: html

    <div class="code_no">Plik <i>fibonacci.py</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. literalinclude:: przyklad05.py
    :linenos:

Funkcje pozwalają grupować instrukcje realizujące jedno zadanie w nazwanym blok kodu,
dzięki czemu mozna je wielokrotnie wywoływać. Funkcję definiujemy za pomocą słowa kluczowego ``def``:

.. code::

    def nazwa_funkcji(parametry):
        pass

Parametry to przekazywane do funkcji wartości i/lub dane. Parametry są opcjonalne.
Po dwukropku od nowego wiersza umieszczamy odpowiednio wcięte instrukcje,
które tworzą ciało funkcji. Funkcja może zwracać jakąś wartość za pomocą
polecenia ``return``.



Zapis ``a, b = 1, 2`` jest przykładem przypisania wielokrotnego, tzn. zmienne ``a`` i ``b``
przyjmują wartości kolejnych elementów rozpakowanych z tupli po prawej stronie.
W taki sam spsób przypisujemy wartości w kodzie ``a, b = b, b + a``.
Jak widać, liczba zmiennych z lewej strony musi odpowiadać liczbie wartości rozpakowywanych z tupli.

Algorytmy iteracyjne można implementować za pomocą różnych instrukcji sterujących,
w tym wypadku pętli ``while`` i ``for``, a także z wykorzystaniem rekurencji.

Zadania dodatkowe
*****************

Zmień funkcje tak, aby zwracały poprawne wartości przy założeniu,
że dwa pierwsze wyrazy ciągu równe są 1 (bez zera).

.. admonition:: Pojęcia

    :term:`funkcja`, :term:`tupla`
