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
