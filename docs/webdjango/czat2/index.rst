.. _czat-app2:

Czat (cz. 2)
#########################

Dodawanie, edycja, usuwanie czy przeglądanie danych zgromadzonych w bazie
są typowymi czynnościami w aplikacjach internetowych. Utworzony w scenariuszu :ref:`Czat (cz. 1) <czat-app>`
kod ilustruje "ręczną" obsługę żądań GET i POST, w tym tworzenie formularzy,
walidację danych itp. Django zawiera jednak gotowe mechanizmy, których
użycie skraca i ulepsza pracę programisty eliminując potencjalne błędy.

Będziemy rozwijać kod uzyskany po zrealizowaniu punktów **8.1.1 – 8.1.10** scenariusza
:ref:`Czat (cz. 1) <czat-app>`. Pobierz więc :download:`archiwum <czat2_z01.zip>`
i rozpakuj w katalogu domowym użytkownika. Następnie wydaj polecenia:

.. raw:: html

    <div class="code_no">Terminal nr <script>var ter_no = ter_no || 1; document.write(ter_no++);</script></span></div>

.. code-block:: bash

    ~$ source pve3/bin/activate
    (pve3) ~$ cd czat2
    (pve3) ~/czat2$ python manage.py check


.. warning::

    Przypominamy, że pracujemy w wirtualnym środowisku Pythona z zainstalowanym frameworkiem
    Django, które powinno znajdować się w katalogu :file:`pve3`. Zobacz w scenariuszu Czat (cz. 1),
    jak utworzyć takie :ref:`środowisko <czat1-env>`.


Rejestrowanie
=============

Na początku zajmiemy się obsługą użytkowników. Umożliwimy im samodzielne
zakładanie kont w serwisie, logowanie i wylogowywanie się. Inaczej niż w cz. 1
zadania te zrealizujemy za pomocą tzw. widoków wbudowanych opartych na klasach
(ang. `class-based generic views <https://docs.djangoproject.com/en/1.11/topics/class-based-views/>`_).

Na początku pliku :file:`czat2/czat/urls.py` importujemy formularz tworzenia użytkownika
(``UserCreationForm``) oraz wbudowany widok przeznaczony do dodawania danych (``CreateView``):

.. raw:: html

    <div class="code_no">Plik <i>urls.py</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: urls.py
    :linenos:
    :lineno-start: 6
    :lines: 6-7

Następnie do listy ``urlpatterns`` dopisujemy:

.. raw:: html

    <div class="code_no">Plik <i>urls.py</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: urls.py
    :linenos:
    :lineno-start: 18
    :lines: 18-20

Powyższy kod łączy adres URL */rejestruj* z wywołaniem widoku wbudowanego jako funkcji
``CreateView.as_view()``. Przekazujemy jej trzy parametry:

* ``template_name`` – szablon, który zostanie użyty do zwrócenia odpowiedzi;
* ``form_class`` – formularz, który zostanie przekazany do szablonu;
* ``success_url`` – adres, na który nastąpi przekierowanie w przypadku braku błędów
  (np. po udanej rejestracji).

Teraz tworzymy szablon formularza rejestracji, który zapisać należy w pliku :file:`templates/czat/rejestruj.html`:

.. raw:: html

    <div class="code_no">Plik <i>rejestruj.html</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: html
.. literalinclude:: rejestruj_z2.html
    :linenos:

Na koniec wstawimy link na stronie głównej, a więc uzupełniamy plik :file:`index.html`:

.. raw:: html

    <div class="code_no">Plik <i>index.html</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: html
.. literalinclude:: index_z2.html
    :linenos:

**Ćwiczenie:** dodaj link do strony głównej w szablonie :file:`rejestruj.html`.

Uruchom aplikację (``python manage.py runserver``) i przetestuj dodawanie użytkowników:
spróbuj wysłać niepełne dane, np. bez hasła; spróbuj dodać dwa razy tego samego użytkownika.

.. figure:: img/django_rejestracja.png

Wy(logowanie)
=============

Na początku pliku :file:`urls.py` aplikacji dopisujemy wymagany import:

.. raw:: html

    <span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: urls.py
    :linenos:
    :lineno-start: 8
    :lines: 8-9

– a następnie:

.. raw:: html

    <div class="code_no">Plik <i>urls.py</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: urls.py
    :linenos:
    :lineno-start: 22
    :lines: 22-27

Widać, że z adresami */loguj* i */wyloguj* wiążemy wbudowane w Django widoki ``login``
i ``logout`` importowane z modułu ``django.contrib.auth.views``. Jedynym nowym
parametrem jest ``next_page``, za pomocą którego wskazujemy stronę
wyświetlaną po wylogowaniu (``reverse_lazy('czat:index')``).

Logowanie wymaga szablonu :file:`loguj.html`, który tworzymy i zapisujemy w podkatalogu :file:`templates/czat`:

.. raw:: html

    <div class="code_no">Plik <i>loguj.html</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: html
.. literalinclude:: loguj_z3.html
    :linenos:

Musimy jeszcze określić stronę, na którą powinien zostać przekierowany
użytkownik po udanym zalogowaniu. W tym wypadku na końcu pliku :file:`czat2/settings.py`
definiujemy wartość zmiennej ``LOGIN_REDIRECT_URL``:

.. raw:: html

    <div class="code_no">Plik <i>settings.py</i>. <span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. code-block:: python

    # czat2/settings.py

    from django.core.urlresolvers import reverse_lazy
    LOGIN_REDIRECT_URL = reverse_lazy('czat:index')

**Ćwiczenie:** Uzupełnij plik :file:`index.html` o linki służące do logowania i wylogowania.

.. figure:: img/django_logowanie.png

Lista wiadomości
================

Chcemy, by zalogowani użytkownicy mogli przeglądać wiadomości wszystkich użytkowników,
zmieniać, usuwać i dodawać własne. Najprostszy sposób to skorzystanie z
widoków wbudowanych.

.. note::

    Django oferuje wbudowane widoki przeznaczone do typowych operacji:

    * DetailView i ListView – (ang. *generic display view*) widoki przeznaczone
      do prezentowania szczegółów i listy danych;
    * FormView, CreateView, UpdateView i DeleteView – (ang. *generic editing views*)
      widoki przeznaczone do wyświetlania formularzy ogólnych, w szczególności
      służących dodawaniu, uaktualnianiu, usuwaniu obiektów (danych).

Do wyświetlania listy wiadomości użyjemy klasy ``ListView``.
Do pliku :file:`urls.py` dopisujemy importy:

.. raw:: html

    <div><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: urls.py
    :linenos:
    :lineno-start: 10
    :lines: 10-12

– i wiążemy adres */wiadomosci* z wywołaniem widoku:

.. raw:: html

    <span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: urls.py
    :linenos:
    :lineno-start: 28
    :lines: 28-33

Zakładamy, że wiadomości mogą oglądać tylko użytkownicy zalogowani. Dlatego
całe wywołanie widoku umieszczamy w funkcji ``login_required()``.

W funkcji ``ListView.as_view()`` podajemy kolejne parametry
modyfikujące działanie widoków:

* ``model`` – podajemy model, którego dane zostaną pobrane z bazy;
* ``context_object_name`` – pozwala zmienić domyślną nazwę (object_list)
  listy obiektów przekazanych do szablonu;
* ``paginate_by``– pozwala określić ilość obiektów wyświetlanych na stronie.


Na końcu pliku :file:`czat2/settings.py` określamy adres logowania,
na który przekierowani zostaną niezalogowani użytkownicy, którzy próbowaliby
zobaczyć listę wiadomości:

.. raw:: html

    <span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. code-block:: python

    # czat2/settings.py

    LOGIN_URL = reverse_lazy('czat:loguj')

.. raw:: html

    <hr />

Potrzebujemy szablonu, którego Django szuka pod domyślną nazwą
*<nazwa modelu>_list.html*, czyli w naszym przypadku tworzymy plik :file:`czat/wiadomosc_list.html`:

.. raw:: html

    <div class="code_no">Plik <i>wiadomosc_list.html</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: html
.. literalinclude:: wiadomosc_list_z4.html
    :linenos:

Kolejne wiadomości odczytujemy i wyświetlamy w pętli przy użyciu tagu ``{% for %}``.
Dostęp do właściwości obiektów umożliwia operator kropki, np.: ``{{ wiadomosc.autor.username }}``.

Linki nawigacyjne tworzymy w instrukcji warunkowej ``{% if is_paginated %}``.
Obiekt ``page_obj`` zawiera następujące właściwości:

* ``has_previous`` – zwraca ``True``, jeżeli jest poprzednia strona;
* ``previous_page_number`` – numer poprzedniej strony;
* ``next_page_number`` – numer następnej strony;
* ``number`` – numer aktualnej strony;
* ``paginator.num_pages`` – ilość wszystkich stron.

Numer strony do wyświetlenia przekazujemy w zmiennej ``page`` adresu URL.

**Ćwiczenie:** Dodaj link do strony wyświetlającej wiadomości na stronie głównej dla zalogowanych użytkowników.

.. figure:: img/django_index.png

.. figure:: img/django_wiadomosci.png

Dodawanie wiadomości
====================

Zadanie to zrealizujemy wykorzystując widok ``CreateView``. Aby ułatwić
dodawanie wiadomości **dostosujemy klasę widoku** tak, aby użytkownik
nie musiał wprowadzać pola autor.

Na początek dopiszemy w pliku :file:`urls.py` skojarzenie adresu URL
*wiadomosc/* z wywołaniem klasy ``CreateView`` jako funkcji:

.. raw:: html

    <div class="code_no">Plik <i>urls.py</i> <span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: urls.py
    :linenos:
    :lineno-start: 34
    :lines: 34-37

Dalej kodujemy w pliku :file:`views.py`. Na początku dodajemy importy:

.. raw:: html

    <div class="code_no">Plik <i>views.py</i> <span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. literalinclude:: views.py
    :linenos:
    :lineno-start: 6
    :lines: 6-9

.. raw:: html

    <div class="code_no">Plik <i>views.py</i> <span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. literalinclude:: views.py
    :linenos:
    :lineno-start: 19
    :lines: 19-40

Tworzymy klasę opartą na widoku ogólnym (``class DodajWiadomosc(CreateView)``),
określamy jej podstawowe właściwości i nadpisujemy wybrane metody:

* ``fields`` – pozwala wskazać pola, które mają znaleźć się na formularzu;
* ``get_initial()`` – metoda pozwala ustawić domyślne wartości dla wybranych pól.
  Wykorzystujemy ją do zainicjowania pola ``data_pub`` aktualna datą:
  ``initial['data_pub'] = timezone.now()``.
* ``get_context_data()`` – metoda pozwala przekazać do szablonu dodatkowe dane,
  w tym wypadku jest to lista wszystkich wiadomości: ``context['wiadomosci'] = Wiadomosc.objects.all()``.
* ``form_valid()`` – metoda, która sprawdza poprawność przesłanych danych i zapisuje je w bazie:

    - ``wiadomosc = form.save(commit=False)`` – tworzymy obiekt wiadomości, ale go nie zapisujemy;
    - ``wiadomosc.autor = self.request.user`` – uzupełniamy dane autora;
    - ``wiadomosc.save()`` – zapisujemy obiekt;
    - ``messages.success(self.request, "Dodano wiadomość!")`` – przygotowujemy komunikat,
      który wyświetlony zostanie po dodaniu wiadomości.


.. raw:: html

    <hr />

Domyślny szablon dodawania danych nazywa się *<nazwa modelu>_form.html*. W nowym pliku
wstawiamy poniższą treść i zapisujemy pod nazwą :file:`templates/czat/wiadomosc_form.html`:

.. raw:: html

    <div class="code_no">Plik <i>wiadomosc_form.html</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: html
.. literalinclude:: wiadomosc_form_z5.html
    :linenos:

W szablonie :file:`templates/czat/wiadomosc_list.html` wstawimy jeszcze po nagłówku
``<h1>`` kod wyświetlający komunikaty:

.. raw:: html

    <div class="code_no">Plik <i>wiadomosc_list.html</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: html
.. literalinclude:: wiadomosc_list_z5.html
    :linenos:
    :lineno-start: 6
    :lines: 6-12

.. warning::

    W pliku :file:`czat/models.py` trzeba usunąć parametr ``auto_now_add=True``
    z definicji pola ``data_pub``, aby użytkownik mógł modyfikować datę
    dodania wiadomości w formularzu.


**Ćwiczenie:** Jak zwykle, umieść link do dodawanie wiadomości na stronie głównej.

.. figure:: img/django_dodawanie.png

Edycja wiadomości
=================

Widok pozwalający na edycję wiadomości i jej aktualizację dostępny będzie
pod adresem **/edytuj/id_wiadomości**, gdzie **id_wiadomosci** będzie identyfikatorem
obiektu do zaktualizowania. Zaczniemy od uzupełnienia pliku :file:`urls.py`:

.. raw:: html

    <div class="code_no">Plik <i>urls.py</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: urls.py
    :linenos:
    :lineno-start: 38
    :lines: 38-41

Nowością w powyższym kodzie są wyrażenia regularne definiujące adresy z dodatkowym
parametrem, np. ``r'^edytuj/(?P<pk>\d+)/'``. Część ``/(?P<pk>\d+)`` oznacza,
że oczekujemy 1 lub więcej cyfr (``\d+``), które zostaną zapisane w zmiennej o nazwie
``pk`` (``?P<pk>``) – nazwa jest tu skrótem od ang. wyrażenia *primary key*,
co znaczy "klucz główny". Zmienna ta zawierać będzie identyfikator wiadomości
i dostępna będzie w klasie widoku, który obsłuży edycję wiadomości.

Na początku pliku :file:`views.py` importujemy więc potrzebny widok:

.. raw:: html

    <div class="code_no">Plik <i>views.py</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: views.py
    :linenos:
    :lineno-start: 10
    :lines: 10

Dalej tworzymy klasę ``EdytujWiadomosc``, która dziedziczy, czyli dostosowuje wbudowany
widok ``UpdateView``:

.. raw:: html

    <div class="code_no">Plik <i>views.py</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: views.py
    :linenos:
    :lineno-start: 43
    :lines: 43-59

Najważniejsza jest tu metoda ``get_object()``, która pobiera i zwraca wskazaną przez
identyfikator w zmiennej *pk* wiadomość: ``wiadomosc = Wiadomosc.objects.get(id=self.kwargs['pk'])``.
Omawianą już metodę ``get_context_data()`` wykorzystujemy, aby przekazać
do szablonu listę wiadomości, ale tylko zalogowanego użytkownika
(``context['wiadomosci'] = Wiadomosc.objects.filter(autor=self.request.user)``).

Właściwości ``model``, ``context_object_name``, ``template_name`` i ``success_url``
wyjaśniliśmy wcześniej. Jak widać, do edycji wiadomości można wykorzystać ten sam szablon,
którego użyliśmy podczas dodawania.

Formularz jednak dostosujemy. Wykorzystamy właściwość ``form_class``,
której przypisujemy utworzoną w nowym pliku :file:`forms.py` klasę zmieniającą
domyślne ustawienia:

.. raw:: html

    <div class="code_no">Plik <i>forms.py</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: forms_z6.py
    :linenos:

Klasa ``EdytujWiadomoscForm`` oparta jest na wbudowanej klasie ``ModelForm``.
Właściwości formularza określamy w podklasie ``Meta``:

* ``model`` – oznacza to samo co w widokach, czyli model, dla którego tworzony jest formularz;
* ``fields`` – to samo co w widokach, lista pól do wyświetlenia;
* ``exclude`` – opcjonalnie lista pól do pominięcia;
* ``widgets`` – słownik, którego klucze oznaczają pola danych, a ich wartości
  odpowiadające im w formularzach HTML typy pól i ich właściwości, np. rozmiar.

Żeby przetestować aktualizowanie wiadomości, w szablonie :file:`wiadomosc_list.html`
trzeba wygenerować linki *Edytuj* dla wiadomości utworzonych przez zalogowanego użytkownika.
Wstaw w odpowiednie miejsce szablonu, tzn po tagu wyświetlającym tekst wiadomości
(``{{ wiadomosc.tekst }}``) poniższy kod:

.. raw:: html

    <div class="code_no">Plik wiadomosc_lista.html</i> <span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: html
.. literalinclude:: wiadomosc_list_z6.html
    :linenos:
    :lineno-start: 20
    :lines: 20-22

**Ćwiczenie:** Ten sam link "Edytuj" umieść również w szablonie dodawania.

.. figure:: img/django_edycja.png

Usuwanie wiadomości
===================

**Usuwanie danych** realizujemy za pomocą widoku ``DeleteView``, który importujemy
na początku pliku :file:`urls.py`:

.. raw:: html

    <div class="code_no">Plik <i>urls.py</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: urls.py
    :linenos:
    :lineno-start: 13
    :lines: 13

Podobnie, jak w przypadku edycji, usuwanie powiążemy z adresem URL zawierającym
identyfikator wiadomości */usun/id_wiadomości*. W pliku :file:`urls.py` dopisujemy:


.. raw:: html

    <div class="code_no">Plik <i>urls.py</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: python
.. literalinclude:: urls.py
    :linenos:
    :lineno-start: 42
    :lines: 42-48

Warto zwrócić uwagę, że podobnie jak w przypadku listy wiadomości, o ile wystarcza nam
domyślna funkcjonalność widoku wbudowanego, nie musimy niczego implementować w pliku :file:`views.py`.

Domyślny szablon dla tego widoku przyjmuje nazwę *<nazwa-modelu>_confirm_delete.html*,
dlatego uprościliśmy jego nazwę we właściwości ``template_name``. Tworzymy więc plik
:file:`wiadomosc_usun.html`:

.. raw:: html

    <div class="code_no">Plik <i>wiadomosc_usun.html</i><span class="right">Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></span></div>

.. highlight:: html
.. literalinclude:: wiadomosc_usun_z7.html
    :linenos:

Tag ``{{ object }}`` zostanie zastąpiony treścią wiadomości zwróconą przez funkcję
"autoprezentacji" ``__str__()`` modelu.

**Ćwiczenie:** Wstaw link "Usuń" (``&bull; <a href="{% url 'czat:usun' wiadomosc.id %}">Usuń</a>``) za linkiem "Edytuj" w szablonach wyświetlających listę wiadomości.

.. figure:: img/django_edycja_usun.png

.. figure:: img/django_usun.png

Materiały
=========

1. O Django http://pl.wikipedia.org/wiki/Django_(informatyka)
2. Strona projektu Django https://www.djangoproject.com/
3. Co to jest framework? http://pl.wikipedia.org/wiki/Framework
4. Co nieco o HTTP i żądaniach GET i POST http://pl.wikipedia.org/wiki/Http

**Źródła:**

* :download:`czat2.zip <czat2.zip>`
