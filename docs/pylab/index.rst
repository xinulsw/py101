.. _pylab:

Matplotlib
################

Jedną z potężniejszych bibliotek Pythona jest `matplotlib <http://pl.wikipedia.org/wiki/Matplotlib>`_,
która służy do tworzenia różnego rodzaju wykresów. W tym scenariuszu pokażemy, jak przygotować wykresy funkcji
w dwuwymiarowym układzie współrzędnych.

Środowisko pracy
================

.. note::

    Do kodowania i uruchamiania skryptu możesz użyć dowolnych narzędzi, np. ulubionego edytora kodu i terminala.
    Sugerujemy jednak wykorzystanie środowiska typu **PyCharm** lub innego, ponieważ ułatwiają przygotowania
    i pracę nad projektami w języku Python.

Przed rozpoczęciem pracy przygotuj w wybranym katalogu, np. :file:`matplot` :ref:`wirtualne środowisko Pythona <venv>`
i w aktywnym środowisku zainstaluj pakiet *Matplotlib*:

.. code-block:: bash

    (.venv) ~/matplot$ pip install matplotlib

.. note::

    *Matplotlib* oferuje dwa główne style kodowania:

    - styl jawny, zorientowany obiektowo, w którym po kolei tworzymy wszystkie elementy budujące wykres,
      takie jak *Figure*, *Axes* czy *Axis*,
    - styl niejawny, w którym korzystamy z funkcji interfejsu ``pyplot``.

    Oficjalna dokumentacja sugeruje, aby w bardziej złożonych projektach stosować
    styl jawny. Tak zrobimy w przykładach korzystających z funkcji matematycznych,
    które zaczynać będziemy następującymi importami:

    .. code-block:: python

        import matplotlib.pyplot as plt
        import numpy as np

    W pierwszym wierszu importujemy interfejs ``pyplot`` pod skróconą nazwą (aliasem) ``plt``.
    W drugim importujemy towarzyszącą modułowi ``matplotlib`` bibliotekę ``numpy`` pod aliasem ``np``.
    Dostarcza ona wielu narzędzi wspomagających obliczenia naukowe.

Anatomia wykresu
****************

Zacznijmy od prostego przykładu, który możemy przetestować w konsoli Pythona:

.. raw:: html

    <div class="code_no"><i>Terminal</i>. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python

    import matplotlib.pyplot as plt
    x = [1, 2, 3]
    y = [4, 6, 5]
    plt.plot(x, y)
    plt.show()

Tworzenie wykresów punktowych jest proste. Postępujemy według schematu:

- przygotowujemy dwie listy wartości: argumentów ``x`` i wartości ``y``, odpowiadające sobie wartości
  zinterpretowane zostaną jako współrzędne punktów w 2-wymiarowym układzie współrzędnych,
- obie listy przekazujemy jako argumenty metody ``plot()``,
- wyświetlamy wykres za pomocą metody ``show()``.

W powyższym przykładzie zastosowaliśmy niejawny styl kodowania wystarczający do prostych pojedynczych wykresów.
W jawnym stylu kodowania dwie ostatnie linie zastąpimy poniższym kodem:

.. code-block:: python

    fig, ax = plt.subplots()
    ax.plot(x, y)
    plt.show()

Żeby lepiej go rozumieć, musimy poznać składniki wykresu. Twórcy pakietu przyjęli następującą terminologię:

- **Figure** – nadrzędny pojemnik zawierający wszystkie inne składniki, w praktyce będzie to okno zawierające wykres(y),
- **Axes** – obiekt reprezentujący pojedynczy wykres i jego elementy, wykresów w figurze może być wiele.

Najprostszym sposobem stworzenia omówionych obiektów jest użycie metody ``subplots()``: ``fig, ax = plt.subplots()``.

Figura (*Figure*) zawiera wykres(y). Wykres (*Axes*) może z kolei zawierać różne elementy
pokazane na poniższym diagramie:

.. figure:: img/anatomy.webp

- **Title** – tytuł ustawiany za pomocą: ``plt.title()`` lub ``ax.set_title()``,
- **Legend** – legenda wykresu może być dodana za pomocą ``plt.legend()`` lub
  ``ax.legend()``,
- **Axis** – obiekty reprezentujące osie X, Y (2D) i ewentualnie Z (3D), zawierają:

    - skalę osi (ang. *tick*) – znaczniki skali, główne (ang. *major*) i poboczne (ang. *minor*),
    - etykiety osi (ang. *label*) – możemy je ustawić za pomocą ``plt.xlabel()`` lub metod wykresu:
      ``ax.set_xlabel()``, ``ax.set_ylabel()``,

- **Markers** – pojedyncze punkty, które można dodać za pomocą ``ax.scatter()``,
- **Line** – linie generowane przez metodę ``plot()``,
- **Grid** – siatka wykresu, którą można dodać za pomoca metody ``grid()``.

Funkcja liniowa
***************

**Zadania**: Wykonaj wykres funkcji ``f(x) = a*x + b``.

**Dane**:

- współczynnik kierunkowy ``a`` i wyraz wolny ``b``, liczby całkowite,
- lista argumentów ``x`` zawierająca liczby całkowite z zakresu ``<-10;10>``.

W pliku :file:`matplot01.py` umieszczamy poniższy kod:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: matplot01.py
    :linenos:

Na początku nadajemy wartości parametrom ``a`` i ``b``. Następnie postępujemy wg omówionego schematu.
Generujemy listę argumentów ``x`` za pomocą funkcji ``range()``.
W pętli ``for`` dla każdego argumentu obliczamy wartość funkcji i dodajemy do listy ``y``.

Następnie stosujemy jawny styl kodowania, tzn. używamy metody ``subplots()``, która obiekty
reprezentujące figurę (``fig``, okno) i wykres (``ax``). Serie danych dodajemy za pomocą metody
``plot()``, która wizualizuje je domyślnie przy użyciu linii ciągłych. Dodajemy tytuł (``set_title()``)
i siatkę (``ax.grid()``). Na koniec wyświetlamy wykres (``plt.show()``).

Ćwiczenie 1
============

Zmodyfikuj powyższy kod tak, aby współczynniki ``a`` i ``b`` oraz zakres argumentów ``x``
pobierane były z klawiatury. Sprawdź poprawność działania programu.

Ćwiczenie 2
============

W konsoli Pythona wydajemy następujące polecenia:

.. raw:: html

    <div class="code_no"><i>Terminal</i>. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python

    >>> a = 2
    >>> x = range(11)
    >>> for i in x:
    ...   print(a + i)
    >>> y = [a + i for i in x]
    >>> print(y)

Powyższy przykład wykorzystuje tzw. :term:`wyrażenie listowe`, które zwięźle
zastępuje pętlę i zwraca listę wartości. Jego działanie należy rozumieć następująco:
dla każdej wartości ``i`` (nazwa zmiennej dowolna) odczytywanej w pętli z listy ``x`` (``for i in x``)
wylicz wyrażenie ``a + i`` i umieść w liście ``y``.

Użyj wyrażenia listowego w naszym programie:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: pylab02.py
    :linenos:
    :emphasize-lines: 1, 2, 6
    :lineno-start: 6
    :lines: 6-12

Dwie funkcje
*************

ZADANIE: wykonaj wykres funkcji:

* *f(x) = x/(-3) + a* dla *x* <= 0,
* *f(x) = x\*x/3* dla *x* >= 0,

– gdzie *x* = <-10;10> z krokiem 0.5. Współczynnik *a* podaje użytkownik.

Wykonanie zadania wymaga umieszczenia na wykresie dwóch funkcji.
Wykorzystamy funkcję ``arange()``, która zwraca listę wartości
zmiennoprzecinkowych (zob. :term:`typy danych`) z zakresu określonego przez
dwa pierwsze argumenty i z krokiem wyznaczonym przez argument trzeci.
Drugą przydatną konstrukcją będzie wyrażenie listowe uzupełnione o instrukcję
warunkową, która ogranicza wartości, dla których obliczane jest podane wyrażenie.

Ćwiczenie 3
============

Zanim zrealizujemy zadanie przećwiczmy w konsoli Pythona następujący kod:

.. raw:: html

    <div class="code_no"><i>Terminal</i>. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python

    >>> import pylab
    >>> x = pylab.arange(-10, 10.5, 0.5)
    >>> print(x)
    >>> len(x)
    >>> a = 3
    >>> y1 = [i / -3 + a for i in x if i <= 0]
    >>> len(y1)

Uwaga: nie zamykaj tej sesji konsoli, zaraz się nam jeszcze przyda.

W pliku :file:`pylab02.py` umieszczamy poniższy kod:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: pylab03.py
    :linenos:

Uruchom program. Nie działa, dostajemy komunikat:
*ValueError: x and y must have same first dimension*,
czyli listy wartości *x* i *y1* nie zawierają tyle samo elementów.

Co należy z tym zrobić? Jak wynika z warunków zadania, wartości *y1* obliczane
są tylko dla argumentów mniejszych od zera. Zatem trzeba ograniczyć listę
*x*, tak aby zawierała tylko wartości z odpowiedniego przedziału.
Wróćmy do konsoli Pythona:

Ćwiczenie 4
============

.. raw:: html

    <div class="code_no"><i>Terminal</i>. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python

    >>> x
    >>> x[0]
    >>> x[0:5]
    >>> x[:5]
    >>> x[:len(y1)]
    >>> len(x[:len(y1)])

Uwaga: nie zamykaj tej sesji konsoli, zaraz się nam jeszcze przyda.

Z pomocą przychodzi nam wydobywanie z listy wartości wskazywanych przez
indeksy liczone od 0. Jednak prawdziwym ułatwieniem jest **notacja wycinania**
(ang. *slice*), która pozwala podać pierwszy i ostatni indeks interesującego
nas zakresu. Zmieniamy więc wywołanie funkcji ``plot()``:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python

    pylab.plot(x[:len(y1)], y1)

Uruchom i przetestuj działanie programu.

Udało się nam zrealizować pierwszą część zadania.
Spróbujmy zakodować część drugą. Dopisujemy:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: pylab04.py
    :linenos:
    :lineno-start: 14
    :lines: 14-16

Wyrażenie listowe wylicza nam drugą dziedzinę wartości. Następnie do argumentów
funkcji ``plot()`` dodajemy drugą parę list. Spróbuj uruchomić program.
Nie działa, znowu dostajemy komunikat: *ValueError: x and y must have same first dimension*.
Teraz jednak wiemy już dlaczego...

Ćwiczenie 5
============

Przetestujmy kod w konsoli Pythona:

.. raw:: html

    <div class="code_no"><i>Terminal</i>. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python

    >>> len(x)
    >>> x[-10]
    >>> x[-10:]
    >>> len(y2)
    >>> x[-len(y2):]

Jak widać, w **notacji wycinania** możemy używać indeksów ujemnych wskazujących
elementy od końca listy. Jeżeli taki indeks umieścimy jako pierwszy przed
dwukropkiem, czyli separatorem przedziału, dostaniemy resztę elementów listy.

Na koniec musimy więc zmodyfikować funkcję ``plot()``:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python

    pylab.plot(x[:len(y1)], y1, x[-len(y2):], y2)

Ćwiczenie 6
============

Spróbuj dziedziny wartości *x* dla funkcji *y1* i *y2* wyznaczyć nie za pomocą
notacji wycinkowej, ale przy użyciu wyrażeń listowych, których wynik przypisz
do zmiennych *x1* i *x2*. Użyj ich jako argumentów funkcji ``plot()`` i przetestuj
program.

Ruchy Browna
***************

Napiszemy program, który symuluje `ruchy Browna <https://pl.wikipedia.org/wiki/Ruchy_Browna>`_. Jak wiadomo są to chaotyczne ruchy cząsteczek, które będziemy mogli zwizualizować w płaszczyźnie dwuwymiarowej.
Na początku przyjmujemy następujące założenia:

* cząsteczka, której ruch będziemy śledzić, znajduje się w początku układu współrzędnych (0, 0);
* w każdym ruchu cząsteczka przemieszcza się o stały wektor o wartości 1;
* kierunek ruchu wyznaczać będziemy losując kąt z zakresu <0; 2Pi>;
* współrzędne kolejnego położenia cząsteczki wyliczać będziemy ze wzorów:

.. math::

    x_n = x_{n-1} + r * cos(\phi)

    y_n = y_{n-1} + r * sin(\phi)


– gdzie: *r* – długość jednego kroku, :math:`\phi` – kąt wskazujący kierunek ruchu w odniesieniu do osi *OX*.

* końcowy wektor przesunięcia obliczymy ze wzoru: :math:`|s| = \sqrt{(x^2 + y^2)}`

Zacznijmy od wyliczenia współrzędnych opisujących ruch cząsteczki. Do pustego pliku o nazwie :file:`rbrowna.py` wpisujemy:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: rbrowna01.py
    :linenos:

Funkcje trygonometryczne zawarte w module ``math`` wymagają kąta podanego w radianach,
dlatego wylosowany kąt po zamianie na liczbę zmiennoprzecinkową mnożymy przez wyrażenie
``math.pi / 180``. Uruchom i przetestuj kod.

Ćwiczenie 6
============

Do przygotowania wykresu ilustrującego ruch cząsteczki generowane współrzędne musimy
zapisać w listach. Wstaw w odpowiednich miejscach pliku poniższe instrukcje:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python

    lx = [0]
    ly = [0]

    lx.append(x)
    ly.append(y)

Na końcu skryptu dopisz instrukcje wyliczającą końcowy wektor przesunięcia
(:math:`|s| = \sqrt{(x^2 + y^2)}`) i drukującą go na ekranie. Przetestuj program.

Pozostaje dopisanie importu biblioteki *matplotlib* oraz instrukcji generujących wykres.
Poniższy kod ilustruje również użycie opcji wzbogacających wykres o legendę, etykiety czy tytuł.

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: rbrowna03.py
    :linenos:
    :emphasize-lines: 6, 28-34
    :lineno-start: 1
    :lines: 1-

Warto zwrócić uwagę na dodatkowe opcje formatujące wykres w poleceniu
``p.plot(lx, ly, "o:", color="green", linewidth=2, alpha=0.5)``.
Trzeci parametr określa styl linii, możesz sprawdzić inne wartości, np:
``r:.``, ``r:+``, ``r.``, ``r+``. Można też określać kolor (``color``),
grubość linii (``linewidth``) i przezroczystość (``alpha``). Poeksperymentuj.

Ćwiczenie 7
============

Spróbuj uzupełnić kod tak, aby na wykresie zaznaczyć prostą linią w kolorze niebieskim wektor przesunięcia.
Efekt końcowy może wyglądać następująco:

.. figure:: img/rbrowna.png

Zadania dodatkowe
*****************

Przygotuj wykres funkcji kwadratowej:
*f(x) = a*x^2 + b*x + c*, gdzie *x* = <-10;10> z krokiem 1, przyjmij następujące
wartości współczynników: *a = 1, b = -3, c = 1*.

Uzyskany wykres powinien wyglądać następująco:

.. figure:: img/pylab01.png

Źródła
*******************

* :download:`pylab.zip <pylab.zip>`
