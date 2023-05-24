# Métodos e operadores úteis em sets

# Métodos úteis:
# add, update, clearr, discard
s1 = set() # Cria o set vazio
s1.add("Lucas") # Adiciona um valor
s1.add(2)
s1.update(("Lucas2", 2)) # Adiciona mais de um valor ao set
# Para adicionar mais de um elemento coloca-se parêntesis senão vai iterar sobre o iterável string
s1.clear() #Limpa o set completo
s1.update((1,2,3,5,8,5,"Olá Lucas"))
s1.discard(3) # Tira um elemento em específico do set
print(s1)

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos
set1 = {1,2,3,4}
set2 = {3,4,5,6}
set3 = set1 | set2
# set3 = set1.union(set2) #Equivalente da expressão acima

set3 = set1 & set2
# set3 = set1.intersection(set2) #Equivalente da expressão acima

set3 = set1 - set2 
# A ordem influencia, vai registrar a diferença apenas com o set da esquerda
set3 = set1.difference(set2) #Equivalente da expressão acima

set3 = set1 ^ set2
set3 = set1.symmetric_difference(set2) #Equivalente da expressão acima


print(set3)
