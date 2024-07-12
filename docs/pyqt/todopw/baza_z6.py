# -*- coding: utf-8 -*-

from peewee import *
from datetime import datetime

baza = SqliteDatabase('adresy.db')


class BazaModel(Model):  # klasa bazowa

    class Meta:
        database = baza


class Osoba(BazaModel):
    login = CharField(null=False, unique=True)
    haslo = CharField()

    class Meta:
        order_by = ('login',)


class Zadanie(BazaModel):
    tresc = TextField(null=False)
    datad = DateTimeField(default=datetime.now)
    wykonane = BooleanField(default=False)
    osoba = ForeignKeyField(Osoba, related_name='zadania')

    class Meta:
        order_by = ('datad',)


def polacz():
    baza.connect()  # nawiązujemy połączenie z bazą
    baza.create_tables([Osoba, Zadanie], True)  # tworzymy tabele
    ladujDane()  # wstawiamy początkowe dane
    return True


def loguj(login, haslo):
    try:
        osoba, created = Osoba.get_or_create(login=login, haslo=haslo)
        return osoba
    except IntegrityError:
        return None


def ladujDane():
    """ Przygotowanie początkowych danych testowych """
    if Osoba.select().count() > 0:
        return
    osoby = ('adam', 'ewa')
    zadania = ('Pierwsze zadanie', 'Drugie zadanie', 'Trzecie zadanie')
    for login in osoby:
        o = Osoba(login=login, haslo='123')
        o.save()
        for tresc in zadania:
            z = Zadanie(tresc=tresc, osoba=o)
            z.save()
    baza.commit()
    baza.close()


def czytajDane(osoba):
    """ Pobranie zadań danego użytkownika z bazy """
    zadania = []  # lista zadań
    wpisy = Zadanie.select().where(Zadanie.osoba == osoba)
    for z in wpisy:
        zadania.append([
            z.id,  # identyfikator zadania
            z.tresc,  # treść zadania
            '{0:%Y-%m-%d %H:%M:%S}'.format(z.datad),  # data dodania
            z.wykonane,  # bool: czy wykonane?
            False])  # bool: czy usunąć?
    return zadania


def dodajZadanie(osoba, tresc):
    """ Dodawanie nowego zadania """
    zadanie = Zadanie(tresc=tresc, osoba=osoba)
    zadanie.save()
    return [
        zadanie.id,
        zadanie.tresc,
        '{0:%Y-%m-%d %H:%M:%S}'.format(zadanie.datad),
        zadanie.wykonane,
        False]


pola = ['Id', 'Zadanie', 'Dodano', 'Zrobione', 'Usuń']


def zapiszDane(zadania):
    """ Zapisywanie zmian """
    for i, z in enumerate(zadania):
        # utworzenie instancji zadania
        zadanie = Zadanie.select().where(Zadanie.id == z[0]).get()
        if z[4]:  # jeżeli zaznaczono zadanie do usunięcia
            zadanie.delete_instance()  # usunięcie zadania z bazy
            del zadania[i]  # usunięcie zadania z danych modelu
        else:
            zadanie.tresc = z[1]
            zadanie.wykonane = z[3]
            zadanie.save()
