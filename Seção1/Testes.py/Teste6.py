import os
import time

def ingredientes_completos(num,valor):
    for num in valor:
        print(f"{num} -> {valor[num]}")

def apresenta_modos(modo):
    for i,letra in enumerate(modo):
        print(f"{i}) ", letra,"\n")

print("Código para anotar receitas")

nome_receita = input("Digite o nome da receita\n>> ")

num_ingredientes = int(input("\nQuantos ingredientes são necessários?\n>> "))

ingredientes = {}

modo_de_fazer = []

for num in range(num_ingredientes):
    qtd_ingredientes = input('Quantidade >>> ')
    ingredientes[qtd_ingredientes] = input("Ingrediente >>> ")
    print()

ingredientes_completos(qtd_ingredientes, ingredientes)
# for qtd_ingredientes in ingredientes:
#     print(f"{qtd_ingredientes} {ingredientes[qtd_ingredientes]}")

num_dpassos = int(input("\nSão necessários quantos passos no modo de fazer?\n"))
# resposta = True
# while resposta == True:
#     if  isdigit() :
#         continue

print()
for num in range(num_dpassos):
    passos = input("")
    modo_de_fazer.append(passos)
    print()

apresenta_modos(modo_de_fazer)
    
time.sleep(4)
os.system("cls")

print(f"Receita de {nome_receita}\n")
ingredientes_completos(qtd_ingredientes, ingredientes)
print()
apresenta_modos(modo_de_fazer)
