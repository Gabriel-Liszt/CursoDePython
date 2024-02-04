import math

ca = float(input('Digite o cateto adjacente do seu triangulo: '))
co = float(input('Digite o cateto oposto do seu triânghulo: '))
h = math.hypot(co, ca)

print(f'O comprimento da hipotenusa é {h}')
