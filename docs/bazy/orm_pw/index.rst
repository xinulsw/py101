.. _systemy_orm:

Systemy ORM
##################

Znajomość języka SQL jest oczywiście bardzo zalecana, aby rozumieć i korzystać z wszystkich możliwości baz danych,
niemniej w wielu projektach można je obsługiwać inaczej, np. za pomocą systemów ORM (ang. *Object-Relational Mapping*
– mapowanie obiektowo-relacyjne). Pozwalają one traktować tabele i relacje w sposób obiektowy, co bywa wygodniejsze,
kiedy obsługujemy bazę danych za pomocą obiektowego języka programowania.

Używanie systemów ORM, takich jak :term:`Peewee` czy :term:`SQLAlchemy`, w prostych projektach
sprowadza się do schematu, który poglądowo można opisać w trzech krokach:

1. deklaracja modelu opisującego bazę
2. utworzenie na podstawie modelu tabel w bazie,
3. wykonywanie operacji :term:`CRUD`.

Przez model (zob. też: :term:`model bazy danych`) rozumiemy tutaj deklaracje klas i ich właściwości (atrybutów)
opisujące obiekty, które będą przechowywane w bazie. Systemy ORM na podstawie klas tworzą
odpowiednie tabele i pola, uwzględniając ich typy i powiązania. Odwzorowanie klas i ich właściwości
na tabele, kolumny i relacje w bazie stanowi istotę mapowania relacyjno-obiektowego.

Poniżej spróbujemy pokazać, jak wykonywać typowe operacje na bazie z wykorzystaniem biblioteki Peewee.

.. note::

    Wyjaśnienia podanego niżej kodu są uproszczone ze względu na przejrzystość i poglądowość instrukcji.
    Do używania systemów ORM wystarczające jest poznanie ich interfejsu API.

Klasa bazowa
************

W ulubionym edytorze utwórz plik o nazwie :file:`orm_pw.py` z następującym kodem:

.. raw:: html

    <div class="code_no">Peewee. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: orm_pw.py
    :linenos:
    :lineno-start: 1
    :lines: 1-16

Na początku importujemy potrzebne klasy. Dalej tworzymy zmienną ``plik_bazy``,
która będzie przechowywała nazwę pliku z bazą danych.
Jeżeli plik znajduje się na dysku (``if os.path.exists()``), usuwamy go (os.remove()),
aby zapewnić bezproblemowe działanie skryptu podczas wielokrotnego uruchamiania.

Następnie tworzymy obiekt ``baza`` do obsługi bazy SQlite3 przechowywanej w pliku :file:`baza_pw.db`.

.. tip::

    Jeżeli zamiast nazwy pliku, podamy argument ``:memory:``, baza utworzona zostanie w pamięci RAM,
    co może być przydatne podczas testowania.

Do utworzenia modeli danych potrzebna będzie **klasa bazowa**, którą tworzymy w oparciu o klasę ``Model``,
w podklasie ``Meta`` dodatkowo przypisujemy obiekt służący do komunikacji z bazą do atrybutu ``database``.

Model danych
*************

Dodajemy definicje klas opisujących dwa obiekty reprezentujące klasę i ucznia. Każda klasa ma swoją nazwę
i profil, każdy uczeń ma imię, nazwisko oraz przynależy do jakiejś klasy.

.. raw:: html

    <div class="code_no">Peewee. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: orm_pw.py
    :linenos:
    :lineno-start: 18
    :lines: 18-32

Deklarowanie modelu opiera się na dziedziczonej klasie podstawowej ``Model``.
Klasy o nazwach ``Klasa`` i ``Uczen`` reprezentują tabele w bazie. Właściwości tych klas odpowiadają polom.
Każde pole jest instancją klasy określającej typ danych i ma ograniczenia podawane jako dodatkowe argumenty
konstruktora:

- ``CharFiled()`` – klasa definiująca pole zawierające ciąg znaków,
- ``null=False`` – ograniczenie, pole nie może zawierać wartości ``NULL``,
- ``default=''`` – ograniczenie, wartość domyślna przechowywana w polu,
- ``ForeignKeyField()`` – klasa definiująca relację, konstruktor otrzymuje nazwę klasy powiązanej,
  z którą tworzymy relację, oraz nazwę atrybutu określającego relację zwrotną w powiązanej klasie;
  dzięki temu wywołanie w postaci ``Klasa.uczniowie`` da nam dostęp do obiektów reprezentujących
  uczniów przypisanych do danej klasy.

Po zdefiniowaniu modelu, co jest relatywnie najtrudniejsze, trzeba go przetestować,
czyli utworzyć tabele i kolumny w bazie. W Peewee łączymy się z bazą (``baza.connect()``)
i wywołujemy metodę ``create_tables()``, której podajemy w liście nazwy klas reprezentujących tabele.

Omówiony kod można już uruchomić, w katalogu, z którego uruchamiamy skrypt, powinien zostać utworzony
plik bazy :file:`baza_pw.db`.

Ćwiczenie
==========

1) Wykorzystaj :ref:`interpreter sqlite3 <sqlite3>` i sprawdź, czy zostały utworzone tabele,
   czyli jak wygląda kod SQL wygenerowany przez ORM. Przykładowy zrzut poniżej.

.. figure:: sqlite3_2.png

.. note::

    Nazwy utworzonych tabel to nazwy klas, które je opisują, podobnie nazwy pól odpowiadają nazwom atrybutów.
    Warto zauważyć, że *Peewee* nie wymaga definiowania kluczy głównych, są tworzone automatycznie
    jako pola o nazwie ``id`` zawierające liczby całkowite.

Dodawanie danych
****************

Dodawanie (ang. *create*) danych w Peewee wykonywane jest za pomocą obiektów
reprezentujących rekordy zdefiniowanych tabel oraz ich metod.

.. raw:: html

    <div class="code_no">Peewee. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: orm_pw.py
    :linenos:
    :lineno-start: 33
    :lines: 33-51

Zanim dodamy pierwsze informacje sprawdzamy, czy w bazie są już zapisane jakieś obiekty typu ``Klasa``,
wykonujemy więc kwerendę zliczającą definiowaną za pomocą kolejno wywoływanych metod:
``Klasa().select().count()``. Jeżeli w bazie nie są zapisane żądne klasy, dodajemy dwie klasy.

Dodawanie polega na utworzeniu instancji odpowiedniego obiektu i podaniu w konstruktorze wartości
jego atrybutów, np.: ``Klasa(nazwa = '1A', profil = 'matematyczny')``.
Utworzony obiekt zapisujemy w bazie jako rekord za pomocą metody ``.save()``.

Można również dodawać wiele rekordów na raz. Na początku tworzymy obiekt reprezentujący klasę
o podanej nazwie jako kwerendę warunkową. Warunki podajemy jako parametry metody ``where()``:
``Klasa.select().where(Klasa.nazwa == '1A').get()``.

Następnie definiujemy listę słowników ``uczniowie``. Każdy słownik zawieraja dane w formacie
"klucz":"wartość", przy czym klucze są nazwami atrybutów klasy. Wartością klucza ``'klasa'`` jest
utworzona wcześniej instancja klasy o nazwie ``1A``.

Za pomocą metody ``insert_many()``, która jako parametr przyjmuje listę słowników,
dodajemy rekordy z danymi wielu uczniów do bazy.

Odczytywanie danych
*******************

Odczytywanie danych polega na u użyciu metody ``select()`` obiektu z opcjonalnymi metodami,
które zawężają zbiór zwracanych rekordów. Do tej pory użyliśmy już instrukcji:

- ``Klasa().select().count()`` – wybieramy wszystkie klasy i je zliczamy;
– ``Klasa.select().where(Klasa.nazwa == '1A').get()`` – wybieramy obiekt reprezentujący klasę o nazwie ``1A``.

Do skryptu dodajemy poniższy kod, który wypisze dane wszystkich klas oraz wszystkich uczniów zapisanych w bazie:

.. raw:: html

    <div class="code_no">Peewee. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: orm_pw.py
    :linenos:
    :lineno-start: 52
    :lines: 52-67

Metoda ``select()`` wywołana dla danej klasy zwraca listę obiektów zapisanych w bazie.
Elementy listy odczytujemy w pętli `for klasa in klasy:` i wypisujemy atrybuty kolejnych obiektów używając
notacji z kropką: ``print(klasa.id, klasa.nazwa, klasa.profil)``.

Funkcja ``czytaj_dane()``, pokazuje jak odczytywać dane obiektów połączonych relacjami, tj. dane z wielu tabel.
Oprócz metody ``select()`` używamy metody ``join()``, aby wskazać obiekt (tabelę) połączony relacją zawierający
dodatkowe dane, w tym przypadku informacje o klasie, do której przypisany jest uczeń: ``Uczen.select().join(Klasa)``.

Pętla ``for`` odczytuje zwrócone rekordy...

Odczytywanie danych z wielu tabel połączonych relacjami może być w porównaniu
do zapytań SQL-a bardzo proste. W Peewee wystarcza polecenie: ``Uczen.select()``,
ale przy próbie odczytania klasy, do której przypisano ucznia (``inst_uczen.klasa.nazwa``),
wykonane zostanie dodatkowe zapytanie, co nie jest efektywne.
Dlatego lepiej otwarcie wskazywać na powiązania między obiektami,
czyli w zależności od ORM-u używać:
``Uczen.select().join(Klasa)`` lub ``sesja.query(Uczen).join(Klasa).all()``.
Tak właśnie postępujemy w bliźniaczych funkcjach ``czytajdane()``, które
pokazują, jak pobierać i wyświetlać wszystkie rekordy z tabel powiązanych
relacjami.

Systemy ORM oferują pewne ułatwiania w zależności od tego, ile rekordów lub pól
i w jakiej formie chcemy wydobyć. Metody w Peewee:

    - ``.get()`` - zwraca pojedynczy rekord pasujący do zapytania lub wyjątek ``DoesNotExist``, jeżeli go brak;
    - ``.first()`` - zwróci z kolei pierwszy rekord ze wszystkich pasujących.

Metody SQLAlchemy:

    - ``.get(id)`` - zwraca pojedynczy rekord na podstawie podanego identyfikatora;
    - ``.one()`` - zwraca pojedynczy rekord pasujący do zapytania lub wyjątek ``DoesNotExist``, jeżeli go brak;
    - ``.scalar()`` - zwraca pierwszy element pierwszego zwróconego rekordu lub wyjątek ``MultipleResultsFound``;
    - ``.all()`` - zwraca pasujące rekordy w postaci listy.

Modyfikowanie i usuwanie danych
=================================

Systemy ORM ułatwiają modyfikowanie i usuwanie danych z bazy, ponieważ
operacje te sprowadzają się do zmiany wartości pól klasy reprezentującej
tabelę lub do usunięcia instancji danej klasy.

.. raw:: html

    <div class="code_no">Peewee. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: orm_pw.py
    :linenos:
    :lineno-start: 65
    :lines: 65-

.. raw:: html

    <div class="code_no">SQLAlchemy. Kod nr <script>var code_no = code_no || 1; document.write(code_no++);</script></div>

.. literalinclude:: orm_sa.py
    :linenos:
    :lineno-start: 67
    :lines: 67-

Załóżmy, że chcemy zmienić przypisanie ucznia do klasy. W obydwu systemach
tworzymy więc obiekt reprezentujący ucznia o identyfikatorze "2". Stosujemy
omówione wyżej metody zapytań. W następnym kroku modyfikujemy odpowiednie
pole tworzące relację z tabelą "klasy", do którego przypisujemy
pobrany w zapytaniu obiekt (Peewee) lub identyfikator (SQLAlchemy).
Różnice, tzn. przypisywanie obiektu lub identyfikatora, wynikają ze sposobu
definiowania modeli w obu rozwiązanich.

Usuwanie jest jeszcze prostsze. W Peewee wystarczy do zapytania zwracającego
obiekt reprezentujący ucznia o podanym id "dokleić" odpowiednią metodę:
``Uczen.select().where(Uczen.id == 3).get().delete_instance()``.
W SQLAlchemy korzystamy jak zwykle z metody sesji, której przekazujemy
obiekt reprezentujący ucznia: ``sesja.delete(sesja.query(Uczen).get(3))``.

Po zakończeniu operacji wykonywanych na danych powinniśmy pamiętać o zamknięciu
połączenia, robimy to używając metody obiektu bazy ``baza.close()`` (Peewee)
lub sesji ``sesja.close()`` (SQLAlchemy). UWAGA: operacje dokonywane
podczas sesji w SQLAlchemy muszą zostać zapisane w bazie, dlatego przed
zamknięciem połączenia trzeba umieścić polecenie ``sesja.commit()``.

Zadania
********

- Spróbuj dodać do bazy korzystając z systemu Peewee lub SQLAlchemy
  wiele rekordów na raz pobranych z pliku. Wykorzystaj i zmodyfikuj
  funkcję ``pobierz_dane()`` opisaną w materiale :ref:`Dane z pliku <dane_z_pliku>`.

- Postaraj się przedstawione aplikacje wyposażyć w konsolowy interfejs,
  który umożliwi operacje odczytu, zapisu, modyfikowania i usuwania rekordów.
  Dane powinny być pobierane z klawiatury od użytkownika.

- Przedstawione rozwiązania warto użyć w aplikacjach internetowych
  jako relatywnie szybki i łatwy sposób obsługi danych. Zobacz,
  jak to zrobić na przykładzie scenariusza aplikacji :ref:`Quiz ORM <quiz-orm>`.

- Przejrzyj scenariusz aplikacji internetowej :ref:`Czat <czat1>`, zbudowanej z użyciem
  frameworku *Django*, korzystającego z własnego modelu ORM.

Źródła
********

* :download:`orm.zip <orm.zip>`


