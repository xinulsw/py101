System i oprogramowanie
#######################

Materiały mogą być realizowane w dowolnym systemie operacyjnym, który zawiera interpreter języka Python.
Sugerujemy systemy Linux (mogą być w wersji  :ref:`Live <linux-live>`),
w których Python 3.x jest domyślnie zainstalowany.

.. _tools:

Podczas realizacji scenariuszy wykorzystywać będziemy interpreter Pythona instalowany razem z biblioteką standardową
oraz dodatkowe pakiety i narzędzia:

* `pip <https://pip.pypa.io/en/stable/>`_  – instalator pakietów Pythona,
  podstawowe narzędzie służące do zarządzania pakietami Pythona zgromadzonymi
  w repozytorium `PyPI <https://pypi.python.org/pypi>`_  (Python Package Index);
* `git <https://git-scm.com/downloads>`_  – konsolowy klient systemu wersjonowania kodu umożliwiający korzystanie z repozytoriów w serwisie `Github <https://github.com/>`_;
* `sqlite3 <https://www.sqlite.org/>`_ – konsolowa powłoka dla baz SQLite3,
  umożliwia przeglądanie schematów tabel oraz zarządzanie bazą za pomocą języka SQL.

Poniżej wyjaśniamy, jak je zainstalować i wykorzystywać w wybranym systemie operacyjnym.

..  toctree::
    :maxdepth: 2

    linux
    live
    windows
    interpreter
    Edytory kodu <https://linetc.readthedocs.io/pl/latest/tools/edytory/index.html>
