import os
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from typing import List
from sqlalchemy import ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import Session

class Base(DeclarativeBase):
  pass

# klasy Klasa i Uczen opisują rekordy tabel "klasa" i "uczen"
# oraz relacje między nimi
class Klasa(Base):
    __tablename__ = 'klasa'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nazwa: Mapped[str] = mapped_column(String(100), nullable=False)
    profil: Mapped[str] = mapped_column(String(100), default='')
    uczniowie: Mapped[List["Uczen"]] = relationship('Uczen', back_populates='klasa')


class Uczen(Base):
    __tablename__ = 'uczen'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    imie: Mapped[str] = mapped_column(String(100), nullable=False)
    nazwisko: Mapped[str] = mapped_column(String(100), nullable=False)
    klasa_id: Mapped[int] = mapped_column(ForeignKey('klasa.id'), nullable=False)
    klasa: Mapped["Klasa"] = relationship("Klasa", back_populates="uczniowie")


if os.path.exists('test.db'):
    os.remove('test.db')
# tworzymy instancję klasy Engine do obsługi bazy
baza = create_engine('sqlite:///test.db', echo=True)  # ':memory:'

# klasa bazowa
BazaModel = declarative_base()





# tworzymy tabele
BazaModel.metadata.create_all(baza)

# tworzymy sesję, która przechowuje obiekty i umożliwia "rozmowę" z bazą
# BDSesja = sessionmaker(bind=baza)
sesja = Session(baza)

# dodajemy dwie klasy, jeżeli tabela jest pusta
if not sesja.query(Klasa).count():
    sesja.add(Klasa(nazwa='1A', profil='matematyczny'))
    sesja.add(Klasa(nazwa='1B', profil='humanistyczny'))

# tworzymy instancję klasy Klasa reprezentującą klasę "1A"
inst_klasa = sesja.query(Klasa).filter_by(nazwa='1A').one()

# dodajemy dane wielu uczniów
sesja.add_all([
    Uczen(imie='Tomasz', nazwisko='Nowak', klasa_id=inst_klasa.id),
    Uczen(imie='Jan', nazwisko='Kos', klasa_id=inst_klasa.id),
    Uczen(imie='Piotr', nazwisko='Kowalski', klasa_id=inst_klasa.id),
])


def czytajdane():
    for uczen in sesja.query(Uczen).join(Klasa).all():
        print(uczen.id, uczen.imie, uczen.nazwisko, uczen.klasa.nazwa)
    print()


czytajdane()

# zmiana klasy ucznia o identyfikatorze 2
inst_uczen = sesja.query(Uczen).filter(Uczen.id == 2).one()
inst_uczen.klasa_id = sesja.query(Klasa.id).filter(
    Klasa.nazwa == '1B').scalar()

# usunięcie ucznia o identyfikatorze 3
sesja.delete(sesja.get(Uczen, 3))

czytajdane()

# zapisanie zmian w bazie i zamknięcie sesji
sesja.commit()
sesja.close()
