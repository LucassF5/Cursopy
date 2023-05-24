# Método copy
# Shallow copy e Deep copy

# Shallow copy = faz uma cópia rasa, copiando apenas os elementos imutáveis e "linkando" os mutáveis, ou seja,
# sendo alterado em ambos os dicionários

# Deep copy = faz uma cópia profunda, assim, não mudando os elementos caso haja alguma alteração

import copy

dict1 = {
    "c1" : 1, 
    "c2" : 2,
    "lista1" : [0,1,2]
# c1 e c2 copiam por serem mutáveis
# lista1 só copia em Deep copy por ser um elemento mutável
}

# dict2 = dict1
# Dessa forma não está sendo a cópia, mas sim indicando que dict2 está apontando ao mesmo endereço de memória de dict1

dict2 = dict1.copy() # Fazendo a cópia rasa do dicionário 1

print(f"Dicionário 1 inicialmente{dict1}\n")
print(f'Dicionário 2 inicialmente {dict2}\n')

dict2['c1'] = 10 # Isso vai ser alterado por ser um dado imutável
dict2['lista1'][2] = 20 # Fazendo alteração do índice 2 na lista e mudando em ambas as listas

print(f'Dicionário 1 após alteração {dict1}\n')
print(f'Dicionário 2 após alteração {dict2}\n')

print("\n*****************************")
print()
print("*****************************\n")

dict3 = {
    "c3" : 1,
    "c4" : 2,
    "lista2" : [3,4,5]

}

dict4 = copy.deepcopy(dict3) # Fazendo a cópia profunda do dicionário 3, nesse não há alteração em dados mutáveis

print(f"Dicionário 3 inicialmente{dict3}\n")
print(f'Dicionário 4 inicialmente {dict4}\n')

dict4['c3'] = 10000
dict4['lista2'][2] = 20000

print(f'Dicionário 3 após alteração {dict3}\n')
print(f'Dicionário 4 após alteração {dict4}\n')
# Como não foi feito uma cópia rasa, logo, a lista foi alterada sem problemas
