Podstawowe pojęcia
##################

Tryb interaktywny
*****************

Interpreter Pythona może i powinien być używany w trybie interaktywnym do nauki i testowania kodu.

Uruchamiamy go, wydając w terminalu wybranego systemu polecenie:

.. code-block:: bash

    python3  # system Linux
    py       # system Windows

Po uruchomieniu interpreter wyświetla znak zachęty ``>>>``. Przydatne polecenia:

.. code-block:: bash

    >>> help()         # uruchomienie interaktywnej pomocy
    help> quit         # wyjście z trybu interaktywnej pomocy
    >>> help(obiekt)   # wyświetla pomoc dotyczącą dowolnego obiektu
    >>> import math    # zaimportowanie przykładowego pakietu math
    >>> dir(math)      # przegląd dostępnych w pakiecie stałych i funkcji
    >>> help(math.pow) # wyświetla pomoc nt. stałej lub funkcji dostępnej w pakiecie
    >>> exit()         # wyjście z trybu interaktywnego interpretera

.. figure:: img/python3_shell_terminal.png

Tryb interaktywny może być również uruchomiony za pomocą domyślnego dla Pythona środowiska programowania, tzn. IDLE:

.. figure:: img/python3_shell_idle.png

Znaki ``...`` oznaczają, że wpisujemy instrukcję złożoną, np. warunkową lub pętlę, i kod wymaga wcięć.

Skrypty Pythona
***************

* Kod źródłowy Pythona zapisujemy w plikach tekstowych z rozszerzeniem ``.py``.
* Skrypty Pythona można uruchamiać w terminalu przy użyciu interpretera w katalogu, w którym zapisany jest skrypt:

  .. code-block:: bash

      python3 nazwa_skryptu.py  # system Linux
      py nazwa_skryptu.py       # system Windows

* Ze względów praktycznych warto korzystać z edytorów programistycznych lub środowisk IDE ułatwiających pisanie i testowanie
  kodu (formatowanie kodu, obsługa błędów itd.)
* Podczas przepisywania (kopiowanie) można pominąć komentarze, czyli teksty zaczynające się od znaku ``#``.
* Przepisując lub wklejając kod pamiętać trzeba o zachowywaniu wcięć, które służą w Pythonie do wyodrębniania bloków kodu.
* W wielu scenariuszach kod rozwijany jest krok po kroku, trzeba uważać, żeby któregoś nie pominąć.
* Większość fragmentów kodu jest numerowana, ale jeśli Twój kod różni się nieznacznie numeracją linii, nie musi to oznaczać błędu.

Dla przykładu poniższy kod powinien zostać wklejony w linii ``51`` skryptu:

.. raw:: html

    <div class="code_no">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. code-block:: python
    :linenos:
    :lineno-start: 51

    def run(self):
        """
        Główna pętla programu
        """
        while not self.handle_events():
            self.ball.move(self.board)
            self.board.draw(
                self.ball,
            )
            self.fps_clock.tick(30)

Katalog domowy
**************

Linux
=====

* **Katalog domowy** jest podkatalogiem katalogu ``/home`` i ma nazwę zalogowanego użytkownika,
  np. ``/home/uczen``. W poleceniach wydawanych w terminalu ścieżkę do tego katalogu symbolizuje znak ``~``.
* Zapis typu ``~/quiz2$`` oznacza więc, że dane polecenie należy wykonać w podkatalogu
  ``quiz2`` katalogu domowego użytkownika.
* Znak ``$`` oznacza, że komendy wydajemy jako zwykły użytkownik, natomiast ``#`` – jako root, czyli administrator.

Windows
=======

Jeżeli scenariusze będziemy wykonywać w MS Windows, musimy pamiętać o różnicach:

* Katalog domowy użytkownika w Windows nie nadaje się do przechowywania w nim
  kodów programów lub repozytoriów. Katalog do programowania można utworzyć
  na Pulpicie lub w katalogu głównym wybranej partycji, np. :file:`C:\\python101`,
  i w nim tworzyć foldery dla poszczególnych scenariuszy.
* Najstarszym terminalem jest program ``cmd``, czyli wiersz poleceń; jest on jednak
  ograniczony, warto używać konsoli PowerShell lub Windows Terminal.
* W systemie Windows znaki ``/`` (slash) w ścieżkach zmieniamy na ``\\`` (backslash).
* Zamieniamy również komendy systemu Linux na odpowiedniki wiersza poleceń Windows,
  np. ``mkdir`` na ``md``.
* Pamiętaj, że skrypty powinny być zapisywane w plikach z rozszerzeniem ``.py`` i kodowaniem UTF-8.

.. admonition:: Pojęcia
    
    :term:`interpreter`, :term:`terminal`, :term:`kod źródłowy`