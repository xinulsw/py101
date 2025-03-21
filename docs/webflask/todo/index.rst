.. _todo-app:

ToDo
#####

.. highlight:: python

Realizacja aplikacji internetowej ToDo (lista zadań do zrobienia) w oparciu o :term:`framework` Flask 3.1.x.
Aplikacja umożliwia dodawanie z określoną datą, przeglądanie i oznaczanie jako wykonane różnych zadań,
które zapisywane będą w bazie danych `SQLite <http://pl.wikipedia.org/wiki/SQLite>`_.

.. contents::
    :depth: 1
    :local:

Do pracy potrzebne nam będzie wirtualne środowisko Pythona z zainstalowanym pakietem Flask.
Początek pracy jest taki sam, jak w przypadku aplikacji :ref:`Quiz <quiz-app>`, tzn.:

1. przygotowujemy wirtualne środowisko Pythona w katalogu :file:`projekty_flask`, chyba że
   zrobiliśmy to wcześniej podczas realizacji aplikacji Quiz;
2. w katalogu :file:`projekty_flask` tworzymy **katalog aplikacji**: :file:`todo`;
3. wykonujemy 2. i 3. punkt scenariusza Quiz, tj.: "Projekt i aplikacja" oraz "Strona główna".

W pliku :file:`app.py` zmieniamy w konfiguracji aplikacji nazwę serwisu
zapisaną w kluczu ``SITE_NAME`` na "Projekty Flask".

Model danych i baza
===================

Jako źródło danych aplikacji wykorzystamy tym razem bazę SQLite3 obsługiwaną za pomocą
modułu Pythona `sqlite3 <https://docs.python.org/3/library/sqlite3.html>`_.

**Model danych**: w katalogu aplikacji tworzymy plik :file:`todo.sql`,
który zawiera instrukcje języka `SQL <https://pl.wikipedia.org/wiki/SQL>`_
tworzące tabelę z zadaniami i dodające przykładowe dane.

.. raw:: html

    <div class="code_no">plik <i>schema.pl</i> <span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: sql
.. literalinclude:: source/todo.sql
    :linenos:

Funkcje potrzebne do obsługi bazy danych umieścimy w nowym pliku :file:`db.py`, który zapisujemy
w katalogu aplikacji.

.. raw:: html

    <div class="code_no">plik <i>schema.pl</i> <span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: sql
.. literalinclude:: source/db.py
    :linenos:

.. note::

    Podczas działania aplikacji Flask mamy dostęp do tzw. kontekstu aplikacji,
    który tworzą ustawienia zapisane w słowniku ``config`` oraz dane w obiektach
    ``current_app`` i ``g``.

Zadaniem funkcji ``get_db()`` będzie połączenie z bazą danych i zapisanie obiektu
``db`` reprezentującego bazę w kontekście aplikacji:

* ``if 'db' not in g:`` – sprawdzamy, czy w obiekcie ``g`` nie ma
  obiektu ``db``;
* dalsza część kodu tworzy połączenie wywołując metodę ``sqlite3.connect()``
  i zapisuje je w kontekście aplikacji.

Funkcja ``close_db()`` odpowiadać będzie za zamknięcie połączenia. Będzie ona wywoływana
po obsłużeniu każdego żądania dzięki kolejnej funkcji ``init_app()``, która
rejestruje funkcję ``close_db()`` w kontekście aplikacji: ``app.teardown_appcontext(close_db)``.

Funkcja ``init_db()`` posłuży do utworzenia pliku bazy danych, a następnie tabel
do przechowywania danych.

.. hint::

    Bazę danych można też utworzyć ręcznie za pomocą wiersza poleceń bazy Sqlite3.
    W terminalu w katalogu aplikacji możemy użyć następujących poleceń:

    .. raw:: html

        <div class="code_no">Terminal nr <script>var ter_no = ter_no || 1; document.write(ter_no++);</script></div>

    .. code-block:: bash

        ~/projekty_flask/todo$ sqlite3 db.sqlite < schema.sql
        ~/projekty_flask/todo$ sqlite3 db.sqlite
        sqlite> select * from zadania;
        sqlite> .quit

    Pierwsze polecenie tworzy bazę danych w pliku :file:`db.sqlite`.
    Drugie otwiera ją w interpreterze. Trzecie to zapytanie SQL, które pobiera
    wszystkie dane z tabeli *zadania*. Interpreter zamykamy poleceniem ``.quit``.

    .. figure:: img/sqlite3_cmd.png


Pozostaje nam uzupełnienie kodu w pliku :file:`app.py`:

.. raw:: html

    <div class="code_no">Plik <i>todo.py</i> <span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: source/app2.py
    :linenos:
    :lineno-start: 1
    :emphasize-lines: 1-3, 11, 14, 24-25

Przede wszystkim uzupełniamy importy. Następnie słowniku konfiguracji dodajemy
klucz ``DATABASE`` wskazujący na plik bazy danych :file:`db.sqlite`.

Następnie umieszczamy wywołanie funkcji ``init_app(app)``, dzięki czemu jeżeli
na dysku nie będzie pliku bazy danych, zostanie on utworzony, a wraz z nim
tabele zdefiniowane w pliku :file:`todo.sql`.

Po uruchomieniu serwera deweloperskiego i otwarciu strony ``http://127.0.0.1:5000``
powinniśmy zobaczyć stronę:

.. figure:: img/todo_01.png

– a w katalogu aplikacji powinien zostać utworzony plik bazy danych :file:`db.sqlite`.

Budowa modułowa
===============

Jedna aplikacja Flask może składać się z wielu modułów odpowiedzialnych np. za
autoryzację użytkowników, system komentarzy, quiz czy listę zadań.
Obsługę tych składników warto rozdzielić na osobne moduły, nazywane we Flasku
<foreign lang='en'>blueprint</foreign>, co ułatwia konstruowanie i rozszerzanie aplikacji.

Nasz pierwszy <foreign lang='en'>blueprint</foreign> umieścimy w pliku :file:`todo.py`,
który tworzymy w katalogu aplikacji:

.. raw:: html

    <div class="code_no">Plik <i>todo.py</i> <span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: source/todo1.py
    :linenos:



Lista zadań
===========

Dodajemy widok, czyli funkcję ``zadania()`` powiązaną z adresem URL ``/zadania``:

.. raw:: html

    <div class="code_no">Plik <i>todo.py</i> <span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: todo_z3.py
    :linenos:
    :lineno-start: 40
    :lines: 40-45

* ``db = get_db()`` – utworzenie obiektu bazy danych ();
* ``db.execute('select...')`` – wykonanie podanego zapytania SQL,
  czyli pobranie wszystkich zadań z bazy;
* ``fetchall()`` – metoda zwraca pobrane dane w formie listy;

Szablon tworzymy w pliku :file:`todo/templates/zadania_lista.html`:

.. raw:: html

    <div class="code_no">Plik <i>zadania_lista.html</i>. <span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: html
.. literalinclude:: templates/zadania_lista_z3.html
    :linenos:

* ``{% %}`` – tagi używane w szablonach do instrukcji sterujących;
* ``{{ }}`` – tagi używane do wstawiania wartości zmiennych;
* ``{{ config.SITE_NAME }}`` – w szablonie mamy dostęp do obiektu ustawień ``config``;
* ``{% for zadanie in zadania %}`` – pętla odczytująca zadania z listy przekazanej
  do szablonu w zmiennej ``zadania``;

Odnośniki
---------

W szablonie :file:`index.html` warto wstawić link do strony z listą zadań,
czyli kod:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: html

    <p><a href="{{ url_for('zadania') }}">Lista zadań</a></p>

* ``url_for('zadania')`` – funkcja dostępna w szablonach, generuje adres
  powiązany z podaną nazwą funkcji.

**Ćwiczenie**

Wstaw link do strony głównej w szablonie listy zadań.
Po odwiedzeniu strony *127.0.0.1:5000/zadania* powinniśmy zobaczyć listę zadań.

.. figure:: img/todo_03_zadania.png

Dodawanie zadań
===============

Po wpisaniu adresu w przeglądarce i naciśnięciu Enter, wysyłamy do serwera żądanie typu :term:`GET`,
które obsługujemy zwracając klientowi odpowiednie dane (listę zadań).
Dodawanie zadań wymaga przesłania danych z formularza na serwer – są to
żądania typu :term:`POST`, które modyfikują dane aplikacji.

Na początku pliku :file:`todo.py` trzeba, jak zwykle, zaimportować wymagane funkcje:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: todo_z4.py
    :linenos:
    :lineno-start: 8
    :lines: 8-9

Następnie rozbudujemy widok listy zadań:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. highlight:: python
.. literalinclude:: todo_z4.py
    :linenos:
    :lineno-start: 43
    :lines: 43-63
    :emphasize-lines: 1, 3-16, 21

* ``methods=['GET', 'POST']`` – w liście wymieniamy typy obsługiwanych żądań;
* ``request.form['zadanie']`` – dane przesyłane w żądaniach POST odczytujemy ze
  słownika ``form``;
* ``db.execute(...)`` – wykonujemy zapytanie, które dodaje nowe zadanie,
  w miejsce symboli zastępczych ``(?, ?, ?, ?)`` wstawione zostaną dane
  z listy podanej jako drugi parametr;
* ``flash()`` – funkcja pozwala przygotować komunikaty dla użytkownika,
  które można będzie wstawić w szablonie;
* ``redirect(url_for('zadanie'))`` – przekierowanie użytkownika na adres związany
  z podanym widokiem – żądanie typu GET.

Warto zauważyć, że do szablonu przekazujemy dodatkową zmienną ``error``.

W szablonie :file:`zadania_lista.html` po znaczniku ``<h1>`` umieszczamy kod:

.. raw:: html

    <div class="code_no">Plik <i>zadania_lista.html</i>. <span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: html
.. literalinclude:: templates/zadania_lista_z4.html
    :linenos:
    :lineno-start: 10
    :lines: 10-25

* ``{% if error %}`` – sprawdzamy, czy zmienna ``error`` cokolwiek zawiera;
* ``{% for message in get_flashed_messages() %}`` – pętla odczytująca komunikaty;

.. figure:: img/todo_04_dodawanie.png

Style CSS
=========

O wyglądzie aplikacji decydują arkusze stylów CSS. Umieszczamy je w podkatalogu ``static``
folderu aplikacji. Tworzymy więc plik :file:`~/todo/static/style.css`
z przykładowymi definicjami:

.. raw:: html

    <div class="code_no">Plik <i>style.css</i>. <span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: css
.. literalinclude:: static/style.css
    :linenos:

Arkusz CSS dołączamy do pliku :file:`zadania_lista.html` w sekcji ``head``:

.. raw:: html

    <div class="code_no">Plik <i>zadania_lista.html</i>. <span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: html
.. literalinclude:: templates/zadania_lista_z5.html
    :linenos:
    :lineno-start: 3
    :lines: 3-8
    :emphasize-lines: 4-5

**Ćwiczenie**

Dołącz arkusz stylów CSS również do szablonu :file:`index.html`. Odśwież aplikację w przeglądarce.

.. figure:: img/todo_05_css.png

Zadania wykonane
================

Do każdego zadania dodamy formularz, którego wysłanie będzie oznaczało,
że wykonaliśmy dane zadanie, czyli zmienimy atrybut ``zrobione`` wpisu
z *0* (niewykonane) na *1* (wykonane). Odpowiednie żądanie typu POST
obsłuży nowy widok w pliku :file:`todo.py`, który wstawiamy
przed kodem uruchamiającym aplikację (``if __name__ == '__main__':``):

.. raw:: html

    <div class="code_no">Plik <i>todo.py</i> <span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: todo_z6.py
    :linenos:
    :lineno-start: 65
    :lines: 65-73

* ``zadanie_id = request.form['id']`` – odczytujemy przesłany identyfikator zadania;
* ``db.execute('UPDATE zadania SET zrobione=1 WHERE id=?', [zadanie_id])`` – wykonujemy
  zapytanie aktualizujące staus zadania.

W szablonie :file:`zadania_lista.html` modyfikujemy fragment wyświetlający
listę zadań i dodajemy formularz:

.. raw:: html

    <div class="code_no">Plik <i>zadania_lista.html</i>. <span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: html
.. literalinclude:: templates/zadania_lista_z6.html
    :linenos:
    :lineno-start: 29
    :lines: 29-50

Możemy dodawać zadania oraz zmieniać ich status.

.. figure:: img/todo_06_zrobione.png

Zadania dodatkowe
=================

* Dodaj możliwość usuwania zadań.
* Dodaj mechanizm logowania użytkownika tak, aby użytkownik mógł dodawać i edytować tylko swoją listę zadań.

Materiały
=========

**Źródła:**

* :download:`todo.zip <todo.zip>`
