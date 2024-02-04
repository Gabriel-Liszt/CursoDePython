import math

ang = int(input('Digite um ângulo: '))
rad = math.radians(ang)
seno = math.sin(rad)
coseno = math.cos(rad)
tangente = math.tan(rad)

print(f'O seno, coseno e tangente de {ang} são respectivamente {seno}, {coseno} e {tangente}')

