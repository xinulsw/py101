# inicjalizujemy zmienne
akt_rok = int(input('Podaj aktualny rok: '))
py_rok = 1989

# obliczamy wiek Pythona
wiek_py = akt_rok - py_rok

# pobieramy dane
imie = input('Jak się nazywasz? ')
wiek = int(input('Ile masz lat? '))

# wypisujemy komunikaty
print("Witaj", imie)
print("Mów mi Python, mam", wiek_py, "lat.")

print()

if wiek_py > wiek:
    roznica_lat = wiek_py - wiek
    print('Jestem starszy o ', roznica_lat)
else:
    print('Jestem młodszy lub mamy tyle samo lat.')
