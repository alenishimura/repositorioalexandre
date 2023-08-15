#estoque = {"tomate": [1000, 2.3], "alface": [500, 0.45], "batata": [2001, 1.2], "feijão": [100, 1.5]}
#
#produto = input("Qual produto foi vendido?")
#quantidade = int(input("Qual foi a quantidade vendida?"))

#produtos = estoque.keys()

#if produto in produtos:
   # print("Quantidade atual %i" %(estoque[produto][0]))
   # estoque[produto][0] -= quantidade
   #print("Quantidade depois da baixa: %i" %(estoque[produto][0]))

#else:
# print("O produto não existe.")





#dicionário = O kauanzin ->{"O":1, "k":1, "a":1, "u":1, "a":1, "n":1, "z":1, "i":1, "n":1}





dicionario = {"Alexandre": 9, "Pedro": 7, "Gustavo": 5.5, "Pedro Henrique": 6, "Andre": 5}
nome_alunos = dicionario.keys()

soma = 0
for nome in nome_alunos:
    soma += dicionario[nome]

media = soma / 5
