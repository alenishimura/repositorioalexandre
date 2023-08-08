""" #Aula sobre dicionário

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
print(carros.values())"""

tabela = {'alface': 0.45, 'batata': 1.2, 'tomate': 2.3, 'feijao': 1.5}
while true:
    produto = input('Digite o nome do produto ou fim para terminar')
if produto == 'fim':
    break
if produto in tabela:
    print(f'preço: R${tabela[produto]:.2f}')
else:
    print('produto não encontrado.')
