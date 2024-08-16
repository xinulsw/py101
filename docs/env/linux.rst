.. _linux-env:

Przygotowanie systemu Linux
###########################

.. _linux-distro:

Polecamy dystrybucje oparte na Debianie z dowolnym środowiskiem graficznym (zob. :term:`środowisko graficzne`), np.
`Linux Mint <https://www.linuxmint.com>`_, `MX Linux <https://mxlinux.org/>`_ lub `Ubuntu <https://www.ubuntu.com/>`__.

.. tip::

    Jeżeli nie masz systemu Linux i nie chcesz instalować go na dysku komputera,
    możesz wykorzystać wersję :ref:`Linux Live <linux-live>`.

.. _linux-tools:

Narzędzia
=========

W Linuksach interpreter Pythona 3.x zainstalowany jest domyślnie.
Aby zainstalować dodatkowe narzędzia, w terminalu wydajemy polecenia:

   .. code-block:: bash

       ~$ sudo apt update
       ~$ sudo apt install python3-pip python3-venv git sqlite3

.. note::

    * Polecenie ``sudo`` oznacza, że do instalacji potrzebne są podwyższone uprawnienia, czyli w praktyce należy być zalogowanym na koncie użytkownika utworzonego podczas instalacji systemu i podać jego hasło.
    * System *Debian* w domyślnej konfiguracji nie wykorzystuje mechanizmu podnoszenia uprawnień ``sudo``, wtedy polecenia instalacji należy wydawać z konta użytkownika *root*.

Następnie przygotowujemy :ref:`środowisko wirtualne Pythona <venv>` i instalujemy w nim wymagane dla danego scenariusza pakiety.

Materiały
---------

* `Windows i Linux na jednym dysku <https://www.dobreprogramy.pl/Windows-i-Linux-Mint-na-jednym-dysku-poradnik-dla-poczatkujacych,News,81165.html>`_;
* `Zainstaluj Linuksa <http://srv40578.seohost.com.pl/linux>`_;
* `Instalacja Ubuntu <http://srv40578.seohost.com.pl/lubuntu>`_;
* `Linux Mint Installation Guide <https://linuxmint-installation-guide.readthedocs.io/en/latest/index.html>`_
