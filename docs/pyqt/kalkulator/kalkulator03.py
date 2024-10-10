from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QLabel, QGridLayout
from PyQt6.QtWidgets import QLineEdit, QPushButton, QHBoxLayout


class Kalkulator(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.interfejs()

    def interfejs(self):

        # etykiety
        etykieta_1 = QLabel("Liczba 1:", self)
        etykieta_2 = QLabel("Liczba 2:", self)
        etykieta_3 = QLabel("Wynik:", self)

        # przypisanie widgetów do układu tabelarycznego
        uklad_t = QGridLayout()
        uklad_t.addWidget(etykieta_1, 0, 0)
        uklad_t.addWidget(etykieta_2, 0, 1)
        uklad_t.addWidget(etykieta_3, 0, 2)

        # 1-liniowe pola edycyjne
        liczba_1 = QLineEdit(self)
        liczba_2 = QLineEdit(self)
        wynik = QLineEdit(self)

        wynik.readonly = True
        wynik.setToolTip('Wpisz <b>liczby</b> i wybierz działanie...')

        uklad_t.addWidget(liczba_1, 1, 0)
        uklad_t.addWidget(liczba_2, 1, 1)
        uklad_t.addWidget(wynik, 1, 2)

        # przyciski
        prz_dodaj = QPushButton("&Dodaj", self)
        prz_odejmij = QPushButton("&Odejmij", self)
        prz_dziel = QPushButton("&Mnóż", self)
        prz_mnoz = QPushButton("D&ziel", self)
        prz_koniec = QPushButton("&Koniec", self)
        prz_koniec.resize(prz_koniec.sizeHint())

        uklad_h = QHBoxLayout()
        uklad_h.addWidget(prz_dodaj)
        uklad_h.addWidget(prz_odejmij)
        uklad_h.addWidget(prz_dziel)
        uklad_h.addWidget(prz_mnoz)

        uklad_t.addLayout(uklad_h, 2, 0, 1, 3)
        uklad_t.addWidget(prz_koniec, 3, 0, 1, 3)

        # przypisanie utworzonego układu do okna
        self.setLayout(uklad_t)

        self.setGeometry(20, 20, 300, 100)
        self.setWindowIcon(QIcon('kalkulator.png'))
        self.setWindowTitle("Prosty kalkulator")
        self.show()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    okno = Kalkulator()
    sys.exit(app.exec())
