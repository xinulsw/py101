.. _linux-env:

Przygotowanie systemu Linux
###########################

Jeżeli nie masz zainstalowanego systemu Linux, możesz wykorzystać wersję
:ref:`Linux Live <linux-live>`. Jeżeli masz Linuksa lub planujesz go zainstalować
na dysku, czytaj dalej.

.. _linux-distro:

Dystrybucje
===========

Polecamy dysstrybucje oparte na Debianie:

* `Linux Mint <https://www.linuxmint.com>`_
* `Ubuntu <https://www.ubuntu.com/>`__.
* `MX Linux <https://mxlinux.org/>`_

Środowisko graficzne (zob. :term:`środowisko graficzne`) dowolne.

**Wskazówki dotyczące instalacji:**

* `Windows i Linux na jednym dysku <https://www.dobreprogramy.pl/Windows-i-Linux-Mint-na-jednym-dysku-poradnik-dla-poczatkujacych,News,81165.html>`_;
* `Zainstaluj Linuksa <http://srv40578.seohost.com.pl/linux>`_;
* `Instalacja Ubuntu <http://srv40578.seohost.com.pl/lubuntu>`_;
* `Linux Mint Installation Guide <https://linuxmint-installation-guide.readthedocs.io/en/latest/index.html>`_

.. _linux-pakiety:

Interpreter, narzędzia i pakiety
================================

W Linuksach interpreter Pythona 3.x zainstalowany jest domyślnie.

.. note::

    * Polecenie ``sudo`` oznacza, że do instalacji potrzebne są uprawnienia administracyjne,
      czyli w praktyce należy być zalogowanym na koncie użytkownika utworzonym podczas instalacji systemu.
    * System *Debian* w domyślnej konfiguracji nie wykorzystuje
      mechanizmu podnoszenia uprawnień ``sudo``, wtedy polecenia instalacji
      należy wydawać z konta użytkownika *root*.    

* Aktualizacja bazy oprogramowania i instalacja podstawowych narzędzi:

   .. code-block:: bash

       ~$ sudo apt update
       ~$ sudo apt install python3-pip python3-venv git sqlite3

* Przygotowanie :ref:`środowiska wirtualnego <pve>` i instalacja wymaganych pakietów.

