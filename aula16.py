"""
Closure e funções que retornam outras funções
"""
"""
def criar_saudacao(saudacao, nome):
    def saudar():
        return f'{saudacao}, {nome}!'#2
    return saudar #1
# Função que retorna a função para saudar

# Em #1 é guardada a função que vai ser usada mais tarde
# Quando é chegada a hora de exibir, então #2 é chamado e retornado os valores guardados


s1 = criar_saudacao("Bom dia", 'Lucas')
s2 = criar_saudacao("Boa noite", 'Lucas')

print(s1()) # É necessário colocar os parêntesis pois a variável vai agir como a função retornando o valor
print(s2())
"""

def criar_saudacao(saudacao):
    def saudar(nome): # Agora, com o nome sendo o parâmetro dessa função, pode ser explicitada por meio da variável no print
        return f'{saudacao}, {nome}!'
    return saudar 

falar_bom_dia = criar_saudacao("Bom dia") # Na chamada da função é necessário explicitar qual saudação usar
falar_boa_noite = criar_saudacao("Boa noite")

print(falar_bom_dia("Lucas")) 
# Ao adicionar a variável no print é necessário explicitar qual nome usar, pois esta manda o parâemetro para a função
print(falar_boa_noite("Lucas"))

#Também é possível utilizar com uma lista de nomes
for nome in ["Lucas", "Francisca Maria", "Sivia"]:
    print()
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))
