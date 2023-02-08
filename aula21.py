# Tipos set
# Sets em Python são mutáveis, porém só aceitam 
# tipos de dados imutáveis como valor interno

# Criando um set
# set(iterável) ou {1,2,3}
# s1 = set("Lucas") # Porém assim vai dividir cada parte do nome
s1 = set() # Vazio
s1 = {"Lucas", 1, 2, 3} # Com dados
print(s1)

# Sets são eficientes para remover valores duplicados de iteráveis
#  - Seus valores serão sempre únicos;
#  - Não aceitam valores mutáveis;
#  - Não tem índexes;
#  - não garantem ordem;
#  - são iteráveis (for, in, not in)

lista1 = [1,2,3,4,3,2,3,4,2,1,3,3]
set1 = set(lista1) 
# Ao transformar a lista em set foram tirados todos oos valores duplicados
# porém não é garantida que se mantenha a ordem
lista2 = list(set1)
print(set1)
print(lista2)

set2 = {1,2,3,4,"set"} # Armaazena os valores que não são mutáveis
print(set2)
print(5 not in set2)
for coisa in set2:
    print(coisa)
