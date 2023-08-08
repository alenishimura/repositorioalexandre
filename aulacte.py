#Aula sobre dicionário

carros= {'Corolla':['R$140.000,00',2022],
         'Civic':['R$150.000,00',2022],
         'Impreza':['R$200.000,00',2023]}

print(carros)
print(carros['Corolla'])

carros['Civic'] [1] = 'R$130.000,00'
print(carros)

del carros['Corolla']
print(carros)

carros['Sentra'] = ['R$145.000,00', '2023']

print('Sentra' in carros)
print('STI' in carros)

print(carros.keys())
print(carros.values())

