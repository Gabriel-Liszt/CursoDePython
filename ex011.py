larg = float(input('Digite a largura da sua parede:'))
alt = float(input('Digite a altura da parede: '))
area = larg  * alt
print(f'sua parede tem a dimensao{larg}x{alt} e tem {area}m².')
tinta = area / 2
print(f'Para pintar a sua parede você precisará de {tinta}L de tinta')