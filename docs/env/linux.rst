.. _linux-env:

Python w systemie Linux
#######################

Polecamy dystrybucje oparte na Debianie z dowolnym środowiskiem graficznym (zob. :term:`środowisko graficzne`), np.
`Linux Mint <https://www.linuxmint.com>`_, `MX Linux <https://mxlinux.org/>`_ lub `Ubuntu <https://www.ubuntu.com/>`_.

.. tip::

    Jeżeli nie masz systemu Linux i nie chcesz instalować go na dysku komputera,
    możesz wykorzystać :ref:`Linux Live USB <linux-live>`, czyli system Linux
    zainstalowany i uruchamiany z klucza USB.

Wymagane pakiety
==================

W Linuksach interpreter Pythona 3.x zainstalowany jest domyślnie, natomiast do zarządzania dodatkowymi pakietami
(bibliotekami itp.) Pythona oraz do tworzenia środowiska wirtualnego wymagana jest instalacja poniższego oprogramowania.
Najłatwiej zainstalować je w terminalu za pomocą poleceń:

   .. code-block:: bash

       ~$ sudo apt update                            # aktualizacja systemowej listy pakietów
       ~$ sudo apt install python3-pip python3-venv

.. note::

    * Polecenie ``sudo`` oznacza, że do instalacji potrzebne są podwyższone uprawnienia, czyli w praktyce należy być zalogowanym
      na koncie użytkownika utworzonego podczas instalacji systemu i podać jego hasło.
    * System *Debian* w domyślnej konfiguracji nie wykorzystuje mechanizmu podnoszenia uprawnień ``sudo``,
      wtedy polecenia instalacji należy wydawać z konta użytkownika *root*.

Następnie przygotowujemy :ref:`środowisko wirtualne Pythona <venv>`
i w razie potrzeby instalujemy w nim wymagane dla danego scenariusza pakiety.

Dodatkowe informacje
====================

Gdybyś chciał zainstalować Linuksa na dysku twardym swojego komputera,
zapoznaj się z poniższymi materiałami:

* `Windows i Linux na jednym dysku <https://www.dobreprogramy.pl/Windows-i-Linux-Mint-na-jednym-dysku-poradnik-dla-poczatkujacych,News,81165.html>`_;
* `Linux Mint Installation Guide <https://linuxmint-installation-guide.readthedocs.io/en/latest/index.html>`_
