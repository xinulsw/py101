.. _venv:

Środowisko wirtualne
####################

Wirtualne środowisko Pythona (ang. *Python virtual environment*) pozwala instalować dodatkowe pakiety
w wybranych wersjach bez uprawnień administratora. W praktyce to katalog zawierający niezbędne pliki
potrzebne do działania interpretera oraz menedżer instalacji pakietów **pip**.

.. note::

    Po utworzeniu środowiska przed każdym użyciem należy go aktywować.

Środowisko możemy utworzyć, a następnie aktywować i korzystać z niego w terminalu (wierszu poleceń):

.. code-block:: bash

    ~$ python3 -m venv venv           # utworzenie środowiska katalogu venv
    ~$ source venv/bin/activate       # aktywacja w Linuksie
    > venv\\Scripts\\activate.bat     # aktywacja w Windowsie
    (venv) ~$ python skrypt.py        # uruchamianie skryptu w wirtualnym środowisku
    (venv) ~$ deactivate              # deaktywacja środowiska

.. tip::

    Niektóre edytory programistyczne lub IDE, np. PyCharm, umożliwiają tworzenie środowiska wirtualnego.

Do zarządzania pakietami w aktywnym środowisku używamy narzędzia `pip`,
za pomocą którego instalujemy wymagane w danym scenariuszu pakiety, np.:

.. code-block:: bash

    (venv) ~$ pip install matplotlib
    (venv) ~$ pip install pygame
    (venv) ~$ pip install flask flask-wtf peewee sqlalchemy flask-sqlalchemy django
    (venv) ~$ pip install pyqt6

.. tip::

    Skopiowane polecenia bez znaku zachęty ``$`` i poprzedzającego tekstu
    możemy wkleić do terminala za pomocą środkowego klawisza myszki
    lub skrótów :kbd:`CTRL+SHIFT+V`, :kbd:`CTRL+SHIFT+Insert`.

.. note::
    
    Składnia przydatnych poleceń instalatora pakietów *pip*:

    .. code-block:: bash

        (venv) ~$ pip install --upgrade pip     # aktualizacja narzędzia pip do najnowszej wersji
        (venv) ~$ pip install biblioteka==1.4   # instalacja biblioteki we wskazanej wersji
        (venv) ~$ pip -V                        # wersja narzędzia pip
        (venv) ~$ pip list                      # lista zainstalowanych pakietów
        (venv) ~$ pip install nazwa_pakietu     # instalacja pakietu
        (venv) ~$ pip install nazwa_pakietu -U  # aktualizacja pakietu
        (venv) ~$ pip uninstall nazwa_pakietu   # usunięcie pakietu
