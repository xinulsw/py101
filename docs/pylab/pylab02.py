import pylab

a = int(input('Podaj współczynnik a: '))
b = int(input('Podaj współczynnik b: '))
x_min = int(input('Podaj wartość minimalną x: '))
x_max = int(input('Podaj wartość maksymalną x: '))

x = range(x_min, x_max)  # lista argumentów x

# wyrażenie listowe wylicza zbiór wartości
y = [a * i + b for i in x]

pylab.plot(x, y)
pylab.title('Wykres f(x) = a*x - b')
pylab.grid(True)
pylab.show()
