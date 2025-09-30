.. _przyklad4:

Listy
#####

.. note::

    W tym przykładzie poznasz :term:`listę`. Jest to jedna z najczęściej używanych złożonych struktur danych,
    która pozwala przechowywać wiele danych pod jedną nazwą i wykonywać na nich wiele operacji.

Zadanie
********

Napisz program :file:`lista.py`, który pobiera z klawiatury ``n`` liczb całkowitych i zapisuje je w liście.
Następnie wykonuje podane niżej operacje:

- wypisuje elementy listy i ich indeksy w jednym wierszu,
- wypisuje elementy listy w odwrotnej kolejności
- wypisuje elementy listy posortowane w porządku rosnącym,
- wypisuje liczbę wystąpień oraz indeks pierwszego wystąpienia podanego elementu,
- usuwa z listy podany element,
- usuwa z listy element o podanym indeksie,
- wstawia podany element na podanym indeksie,
- wypisuje z listy elementy od indeksu ``i`` do ``j``.

**Dane**:

Wszystkie dane to liczby całkowite pobierane z klawiatury.

- ``n`` – liczba liczb pobieranych z klawiatury i zapisywanych w liście,
- ``el`` – liczba pobierana z klawiatury, którą należy z listy usunąć, liczba całkowita,
- ``el`` – liczba pobierana z klawiatury, której liczbę wystąpień i indeks pierwszego wystąpienia
  należy wypisać, liczba całkowita,
- ``in`` – indeks elementu do usunięcia pobierany z klawiatury, liczba całkowita,
- ``in, el`` – indeks i element, który należy wstawić do tabeli, liczby całkowite,
- ``i, j`` – indeksy pobierane z klawiatury, liczby całkowite.

.. tip::

    Wszystkie poniższe przykłady warto wykonać w konsoli Pythona.
    Treść komunikatów w funkcjach ``print()`` można skrócić.
    Można również wpisywać kolejne polecenia do pliku i sukcesywnie go uruchomiać.

.. raw:: html

    <div class="code_no">Plik <i>lista.py</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. literalinclude:: przyklad04.py
    :linenos:

Na początku z modułu ``random`` importujemy funkcję ``randint(a, b)``,
która służy do generowania liczb z przedziału [a, b]. Wylosowane liczby
dodajemy do listy.

Lista (zob. :term:`lista`) to sekwencja indeksowanych danych, zazwyczaj tego samego typu.
Listę tworzymy ujmując wartości oddzielone przecinkami w nawiasy kwadratowe,
np. ``lista = [1, 'a']``. Dostęp do elementów sekwencji uzyskujemy podając
nazwę i indeks, np. ``lista[0]``. Elementy indeksowane są od 0 (zera!).
Z każdej sekwencji możemy wydobywać fragmenty dzięki notacji wycinkowej
(ang. *slice*, zob. :term:`notacja wycinkowa`), np.: ``lista[1:4]``.

.. note::

    Sekwencjami w Pythonie są również napisy i tuple.

Funkcje działające na sekwencjach:

* ``len()`` – zwraca ilość elementów;
* ``enumerate()`` – zwraca obiekt zawierający indeksy i elementy sekwencji;
* ``reversed()`` – zwraca obiekt zawierający odwróconą sekwencję;
* ``sorted(lista)`` – zwraca kopię listy posortowanej rosnąco;
* ``sorted(lista, reverse=True)`` – zwraca kopię listy w odwrotnym porządku;

Lista ma wiele użytecznych metod:

* ``.append(x)`` – dodaje x do listy;
* ``.remove(x)`` – usuwa pierwszy x z listy;
* ``.insert(i, x)`` – wstawia x przed indeksem i;
* ``.count(x)`` – zwraca ilość wystąpień x;
* ``.index(x)`` – zwraca indeks pierwszego wystąpienia x;
* ``.pop()`` – usuwa i zwraca ostatni element listy;
* ``.sort()`` – sortuje listę rosnąco;
* ``.reverse()`` – sortuje listę w odwróconym porządku.

Tupla to niemodyfikowalna lista. Wykorzystywana jest do zapamiętywania
i przekazywania wartości, których nie powinno się zmieniać.
Tuple tworzymy podając wartości w nawiasach okrągłych, np. ``tupla = (1, 'a')``
lub z listy za pomocą funkcji: ``tuple(lista)``. Tupla może powstać
również poprzez spakowanie wartości oddzielonych przecinkami,
np. ``tupla = 1, 'a'``. Próba zmiany wartości w tupli generuje błąd.

Funkcja ``eval()`` interpretuje swój argument jako kod Pythona.
W instrukcji ``a, i = eval(input("Podaj element i indeks oddzielone przecinkiem: "))``
podane przez użytkownika liczby oddzielone przecinkiem interpretowane są jako tupla,
która następnie zostaje rozpakowana, czyli jej elementy zostają przypisane
do zmiennych z lewej strony. Przetestuj w konsoli Pythona:

.. code-block:: bash

	>>> tupla = 2, 6
	>>> a, b = tupla
	>>> print(a, b)

Zadania dodatkowe
*****************

Utwórz w konsoli Pythona dowolną listę i przećwicz notację wycinkową.
Sprawdź działanie indeksów pustych i ujemnych, np. ``lista[2:], lista[:4], lista[-2], lista[-2:]``.
Posortuj trwale dowolną listę malejąco. Utwórz kopię listy posortowaną rosnąco.

**POJĘCIA**: *lista, metoda, notacja wycinkowa, tupla*.