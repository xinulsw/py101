Windows
#######

Brak Pythona
============

Można też samemu rozszerzyć zmienną systemową ``PATH`` swojego użytkownika
o ścieżkę do ``python.exe``. Najwygodniej wykorzystać konsolę PowerShell:

.. code-block:: posh

    [Environment]::SetEnvironmentVariable("Path", "$env:Path;C:\Python36\;C:\Python36\Scripts\", "User")

Ewentualnie, jeśli posiadamy uprawnienia administracyjne, możemy zmienić zmienną ``PATH`` wszystkim użytkownikom:

.. code-block:: posh

    $CurrentPath=[Environment]::GetEnvironmentVariable("Path", "Machine")
    [Environment]::SetEnvironmentVariable("Path", "$CurrentPath;C:\Python36\;C:\Python36\Scripts\", "Machine")

Jeżeli nie mamy dostępu do konsoli PowerShell, w oknie "Uruchamianie" (:kbd:`WIN+R`)
wpisujemy polecenie wywołujące okno "Zmienne środowiskowe" – można je również
uruchomić z okna właściwości komputera:

.. code-block:: bat

    rundll32 sysdm.cpl,EditEnvironmentVariables

.. figure:: img/winpath01.jpg
.. figure:: img/winpath02.jpg

Następnie klikamy przycisk "Nowa" i dopisujemy ścieżkę do katalogu z Pythonem, np.:
``PATH=%PATH%;C:\Python36\;C:\Python36\Scripts\``; w przypadku zmiennej systemowej
klikamy "Edytuj", a ścieżki ``C:\Python36\;C:\Python36\Scripts\`` dopisujemy po średniku.
Dla pojedynczej sesji (do momentu przelogowania się) możemy użyć polecenia w konsoli tekstowej:

.. code-block:: bat

    set PATH=%PATH%;c:\Python36\;c:\Python36\Scripts\


.. warning::

    W powyższych przykładach założono, że Python zainstalowany został w katalogu
    :file:`C:\Python36`, co nie jest opcją domyślną.

.. _pyqt-win:

Biblioteki
==========

.. tip::

    W przypadku bibliotek warto rozważyć instalację
    w :ref:`środowisku wirtualnym <venv>` dostępną dla zwykłego użytkownika.

PyQt
-----

*Qtconsole* wymaga bibliotek PyQt. W 64-bitowej wersji Windowsa w wierszu poleceń wydajemy polecenie:

.. code-block:: bat

    pip install python-qt5

.. _pygame-win:

PyGame
-------

Jest to moduł wymagany m.in. przez scenariusze gier. W przypadku Windows 32-bitowego ze strony
`PyGame <http://pygame.org>`_ pobieramy plik
`pygame-1.9.1.win32-py2.7.msi <http://pygame.org/ftp/pygame-1.9.1.win32-py2.7.msi>`_
i instalujemy:

.. figure:: img/pygame_windows01.jpg

W przypadku wersji 64-bitowej wchodzimy na stronę
`http://www.lfd.uci.edu/~gohlke/pythonlibs <http://www.lfd.uci.edu/~gohlke/pythonlibs>`_
i pobieramy pakiet ``pygame‑1.9.3‑cp36‑cp36m‑win_amd64.whl`` (dla Pythona 3.6).
Następnie otwieramy terminal w katalogu z zapisanym pakietem i wydajemy polecenie:

.. code-block:: bat

    pip install pygame-1.9.2b1-cp27-cp27m-win_amd64.whl

.. _matplotlib-win:

Matplotlib
----------

Wejdź na stronę `http://www.lfd.uci.edu/~gohlke/pythonlibs <http://www.lfd.uci.edu/~gohlke/pythonlibs>`_
i pobierz pakiety ``numpy`` oraz ``matplotlib`` w formacie ``whl`` dostosowane do wersji Pythona i Windows.
Np. jeżeli mamy *Pythona 3.6.x* i *Windows 64-bit*, pobierzemy:
``numpy‑1.13.1+mkl‑cp36‑cp36m‑win_amd64.whl`` i ``matplotlib‑2.0.2‑cp36‑cp36m‑win_amd64.whl``.
Następnie otwieramy terminal w katalogu z pobranymi pakietami i instalujemy:

.. code-block:: bat

    pip install numpy‑1.13.1+mkl‑cp36‑cp36m‑win_amd64.whl
    pip matplotlib‑2.0.2‑cp36‑cp36m‑win_amd64.whl


.. figure:: img/win_matplotlib.jpg


.. note::

    Oficjalne kompilacje **matplotlib** dla Windows dostępne są w serwisie
    `Sourceforge matplotlib <http://sourceforge.net/projects/matplotlib/files/matplotlib>`_.

.. _webapps-win: