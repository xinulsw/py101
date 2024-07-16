Podstawy Pythona
################

Python to język interpretowany. Kod źródłowy Pythona zapisujemy w plikach tekstowych z rozszerzeniem ``.py``. Skrypty Pythona można uruchamiać w terminalu przy użyciu interpretera w katalogu, w którym zapisany jest skrypt:

.. code-block:: bash

    ~$ python3 nazwa_skryptu.py

Ze względów praktycznych warto korzystać z programów ułatwiających pisanie kodu
(obsługa wcięć, podświetlenia itd.) i jego uruchamianie. Zobacz `Edytory kodu <https://linetc.readthedocs.io/pl/latest/tools/edytory/index.html>`_.

**Tryb interaktywny** interpretera Pythona jest podstawowym narzędziem nauki
i testowania kodu. Uruchamiamy go, wydając w terminalu polecenie:

.. code-block:: bash

    ~$ python3

– lub ``python`` (w systemie Windows).

Po uruchomieniu interpreter wyświetla znak zachęty ``>>>``. Przydatne polecenia:

.. code-block:: bash

    >>> help()         # uruchomienie interaktywnej pomocy
    help> quit         # wyjście z trybu interaktywnej pomocy
    >>> help(obiekt)   # wyświetla pomoc dotyczącą dowolnego obiektu
    >>> import math    # zaimportowanie przykładowego pakietu math
    >>> dir(math)      # przegląd dostępnych w pakiecie stałych i funkcji
    >>> help(math.pow) # wyświetla pomoc nt. stałej lub funkcji dostępnej w pakiecie
    >>> exit()         # wyjście z trybu interaktywnego interpretera

Znaki ``...`` oznaczają, że wpisujemy instrukcję złożoną, np. warunkową lub pętlę, i dalszy kod wymaga wcięć.

.. _pve:

Środowisko wirtualne
====================

Wirtualne środowisko Pythona (ang. *Python virtual environment*) pozwala instalować dodatkowe pakiety w wybranych wersjach bez uprawnień administratora. W praktyce to katalog zawierający niezbędne pliki potrzebne do działania interpretera oraz menedżer instalacji pakietów **pip**.

.. note::

    Po utworzeniu środowiska przed każdym użyciem należy go aktywować.

Środowisko możemy utworzyć, a następnie aktywować i korzystać z niego w terminalu:

.. code-block:: bash

    ~$ python3 -m venv pve           # utworzenie środowiska katalogu pve
    ~$ source pve/bin/activate       # aktywacja w Linuksie
    > pve\\Scripts\\activate.bat     # aktywacja w Windowsie
    (pve) ~$ python skrypt.py        # uruchamianie skryptu w wirtualnym środowisku
    (pve) ~$ deactivate              # deaktywacja środowiska

.. tip::

    Niektóre edytory programistyczne lub IDE, np. PyCharm, umożliwiają tworzenie środowiska wirtualnego.

Aby zainstalować pakiety wykorzystywane w materiałach w aktywnym środowisku wydajemy polecenia:

.. code-block:: bash

    (pve) ~$ pip3 install matplotlib
    (pve) ~$ pip3 install pygame
    (pve) ~$ pip3 install flask flask-wtf peewee sqlalchemy flask-sqlalchemy django
    (pve) ~$ pip3 install pyqt6

.. tip::

    Skopiowane polecenia bez znaku zachęty ``$`` i poprzedzającego tekstu
    możemy wkleić do terminala za pomocą środkowego klawisza myszki
    lub skrótów :kbd:`CTRL+SHIFT+V`, :kbd:`CTRL+SHIFT+Insert`.

.. note::
    
    Składnia przydatnych poleceń instalatora pakietów *pip*:

    .. code-block:: bash

        (pve) ~$ pip3 install biblioteka==1.4   # instalacja biblioteki we wskazanej wersji
        (pve) ~$ pip3 -V                        # wersja narzędzia pip
        (pve) ~$ pip3 list                      # lista zainstalowanych pakietów
        (pve) ~$ pip3 install nazwa_pakietu     # instalacja pakietu
        (pve) ~$ pip3 install nazwa_pakietu -U  # aktualizacja pakietu
        (pve) ~$ pip3 uninstall nazwa_pakietu   # usunięcie pakietu
