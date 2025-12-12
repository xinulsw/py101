import os
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from typing import List
from sqlalchemy import ForeignKey, Integer, String, create_engine, select
from sqlalchemy.orm import Session

plik_bazy = 'baza_sa.db'
if os.path.exists(plik_bazy):
    os.remove(plik_bazy)

# tworzymy instancję klasy Engine do obsługi bazy
baza = create_engine('sqlite:///' + plik_bazy)  # ':memory:'

# klasa bazowa dla modeli
class Base(DeclarativeBase):
    pass

# klasy Klasa i Uczen opisują rekordy tabel "klasa" i "uczen" oraz relacje między nimi
class Klasa(Base):
    __tablename__ = 'klasa'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nazwa: Mapped[str] = mapped_column(String(100), nullable=False)
    profil: Mapped[str] = mapped_column(String(100), default='')
    uczniowie: Mapped[List["Uczen"]] = relationship(back_populates='klasa')


class Uczen(Base):
    __tablename__ = 'uczen'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    imie: Mapped[str] = mapped_column(String(100), nullable=False)
    nazwisko: Mapped[str] = mapped_column(String(100), nullable=False)
    klasa_id: Mapped[int] = mapped_column(ForeignKey('klasa.id'), nullable=False)
    klasa: Mapped["Klasa"] = relationship(back_populates="uczniowie")

# tworzymy tabele
Base.metadata.create_all(baza)

# tworzymy sesję, która przechowuje obiekty i umożliwia "rozmowę" z bazą
with Session(baza) as sesja:

    # dodajemy dwie klasy
    klasa1 = Klasa(nazwa='1A', profil='matematyczny')
    klasa2 = Klasa(nazwa='1B', profil='humanistyczny')
    sesja.add(klasa1)
    sesja.add(klasa2)

    sesja.commit()

    uczniowie = [
        Uczen(imie='Tomasz', nazwisko='Nowak', klasa_id=klasa1.id),
        Uczen(imie='Jan', nazwisko='Kos', klasa_id=klasa2.id),
        Uczen(imie='Piotr', nazwisko='Kowalski', klasa_id=klasa2.id)
    ]
    # dodajemy dane wielu uczniów
    sesja.add_all(uczniowie)
    sesja.commit()

    # odczytujemy wiele rekordów
    print('Klasy:')
    zapytanie = select(Klasa)
    klasy = sesja.scalars(zapytanie)
    for klasa in klasy:
        print(klasa.id, klasa.nazwa, klasa.profil)
    print()

    # odczytujemy jeden rekord
    zapytanie = select(Klasa).where(Klasa.nazwa == '1A')
    klasa = sesja.scalar(zapytanie)
    print('Klasa:', klasa.nazwa)
    print()

    def wypisz_listę_uczniow():
        """ Odczytujemy i wypisujemy dane uczniów, w tym klasę"""
        if sesja.query(Uczen).count():
            print('Uczniowie:')
            uczniowie = sesja.query(Uczen).join(Klasa).all()
            for uczen in uczniowie:
                print(uczen.id, uczen.imie, uczen.nazwisko, uczen.klasa.nazwa)
            print()
        else:
            print('Brak uczniów w bazie!')

    wypisz_listę_uczniow()

    # zmiana klasy ucznia o identyfikatorze 2
    uczen = sesja.query(Uczen).filter(Uczen.id == 2).one()
    id_klasa = sesja.query(Klasa.id).filter(Klasa.nazwa == '1A').scalar()
    print('Zmieniam klasę ucznia:', uczen.imie, uczen.nazwisko, uczen.klasa.nazwa)
    uczen.klasa_id = id_klasa
    sesja.commit()
    wypisz_listę_uczniow()

    # usunięcie ucznia o identyfikatorze 3
    uczen = sesja.get(Uczen, 3)
    print('Usuwam ucznia:', uczen.id, uczen.imie, uczen.nazwisko)
    sesja.delete(uczen)
    sesja.flush()
    wypisz_listę_uczniow()

    print('Usuwam uczniów z klasy 1A')
    from sqlalchemy import delete
    id_klasa = sesja.query(Klasa.id).filter(Klasa.nazwa == '1A').scalar()
    zapytanie = delete(Uczen).where(Uczen.klasa_id==id_klasa)
    sesja.execute(zapytanie)
    wypisz_listę_uczniow()
