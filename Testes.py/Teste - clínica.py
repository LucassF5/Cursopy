"""
1 - Cadastrar um paciente : O programa solicita o nome e o telefone do usuário. Após o
cadastro, exibe a mensagem "Paciente cadastrado com sucesso" e adiciona o paciente à
lista de Pacientes Cadastrados. Em seguida, retorna ao menu principal.

2 - Marcações de consultas : Ao selecionar essa opção, o programa exibe uma lista
numerada dos pacientes cadastrados. Ao escolher o número correspondente a um
paciente, solicita o dia, a hora e a especialidade desejada para a consulta. Após o envio
desses dados, o agendamento é adicionado à lista de agendamentos e o programa
retorna ao menu principal.

3 - Cancelamento de consultas : Ao selecionar essa opção, o programa exibe uma lista
numerada dos agendamentos existentes. Ao escolher o número correspondente ao
agendamento que deseja remarcar, é exibida uma mensagem informando a data, a hora e
a especialidade da consulta agendada. Nesse momento, o usuário pode optar por
cancelar a consulta. Ao confirmar o cancelamento, o agendamento é removido da lista e o
programa retorna ao menu principal.

4 - Sair : O programa encerra a execução.

Tratamento de erros:
● O paciente não pode ser cadastrado mais de uma vez. Para evitar duplicidade,
garanta que o número de telefone seja diferente para cada cadastro. Caso ocorra
uma tentativa de cadastro duplicado, exiba a mensagem "Paciente já cadastrado!"
e retorne ao menu principal.

● Pacientes não podem marcar consultas em dias e horários já agendados. Verifique
se a data e a hora selecionadas estão disponíveis antes de realizar o
agendamento.

● Consultas não podem ser marcadas antes da data atual. Certifique-se de que o
usuário não possa agendar consultas retroativas.


Extra:
Seria muito legal se você conseguisse implementar uma maneira de armazenar as
informações dos pacientes de forma que eles continuassem existindo mesmo após o
usuário sair do sistema. Que funcionasse como uma espécie de “banco de dados”.
"""

import os
from datetime import datetime

class Paciente:
    def __init__(self, nome, telefone, data=None, hora=None, especialidade=None):
        self.__nome = nome
        self.__telefone = telefone
        self.__data = data
        self.__hora = hora
        self.__especialidade = especialidade

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self, novo_tel):
        self.__telefone = novo_tel

    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, nova_data):
        self.__data = nova_data

    @property
    def hora(self):
        return self.__hora
    
    @hora.setter
    def hora(self, nova_hora):
        self.__hora = nova_hora

    @property
    def especialidade(self):
        return self.__especialidade
    
    @especialidade.setter
    def especialidade(self, nova_especialidade):
        self.__especialidade = nova_especialidade

    def __str__(self):
        return f"Nome: {self.__nome} - Telefone: {self.__telefone} - Data: {self.__data} - Hora:{self.__hora} - Especialidade:{self.__especialidade}"
    
    def __repr__(self):
        return f"Paciente(nome={self.__nome}, telefone={self.__telefone})"


def cadastrar_paciente(pacientes_cadastrados):
    repetido = False
    nome = input("\nDigite o nome do paciente: ")
    telefone = int(input("Digite o telefone do paciente(ex:40028922): "))
    p = Paciente(nome, telefone)

    for cadastro in pacientes_cadastrados:
        # print("ENTRA FOR")
        # print(cadastro)
        if telefone == cadastro.telefone:
            repetido = True
            # print("ENTRA IF")
            # print("Telefone já cadastrado")
            break
        else:
            repetido = False
            # print("ENTRA ELSE")

    if repetido:
        # pacientes_cadastrados.pop()
        print("Telefone já cadastrado")
    else:
        pacientes_cadastrados.append(p)
        print(f"\nPaciente cadastrado com sucesso")

def mostra_paciente_enumerado(pacientes_cadastrados):
    for index, paciente in enumerate(pacientes_cadastrados):
        print(f"{index} - {paciente.nome}")

def mostra_agendamentos(paciente, agendamentos):
    for index, paciente in enumerate(agendamentos):
        print(f"{index} - Data:{paciente.data} - Hora:{paciente.hora} - Especialidade:{paciente.especialidade}")

def limpa_tela():
    os.system("cls")

def marca_consulta(pacientes_cadastrados, agendamentos):
    escolha_paciente = int(input("\nDigite o número do paciente que deseja marcar uma consulta: "))
    paciente_escolhido = pacientes_cadastrados[escolha_paciente]
    print(f"\nVocê escolheu o paciente {paciente_escolhido.nome}")
    # print(f" Teste 1 - {paciente_escolhido}\n\n\n")

    dados_agendamento(paciente_escolhido,agendamentos)
    # agendamentos.append(paciente_escolhido)

    # print(lista_marcacao)
    # print(len(agendamentos))
    # print(agendamentos)

def dados_agendamento(paciente_escolhido,agendamentos):
    repetido = False
    data_atual = datetime.now()
    # data_atual_str = data_atual.strftime("%d/%m/%y")
    # print("Data atual:", data_atual_str)

    input_data = input("Digite a data (formato DD/MM/AA): ")
    data = datetime.strptime(input_data, "%d/%m/%y")

    if data >= data_atual:
        # print("Data inserida válida:", data.strftime("%d/%m/%y"))
        data = input_data
        entrada_hora_str = input("Digite a hora (formato HH:MM): ")
        hora = datetime.strptime(entrada_hora_str, "%H:%M").time()
        # print(hora)
        especialidade = input("Qual especialidade deseja marcar?\n>>> ")
        # entrada_hora_str = input("Digite a hora (formato HH:MM): ")
        # hora = datetime.strptime(entrada_hora_str, "%H:%M").time()
        # # print(hora)
        # especialidade = input("Qual especialidade deseja marcar?\n>>> ")

        for paciente in agendamentos:
            # print("ENTRA FOR")
            # print(cadastro)
            if (data != paciente.data) and (hora != paciente.hora):
                # print("ENTRA 1")
                repetido = False
                continue
            else:
                # print("ENTRA 2")
                repetido = True
                print("Data e/ou horário de consulta indisponível, tente novamente")
                break
        if repetido == False:
                    # print("ENTRA 3")
                    # pacientes_cadastrados.append()
                    print(f"\nPaciente cadastrado com sucesso\n")
                    paciente_escolhido.data = data
                    paciente_escolhido.hora = hora
                    paciente_escolhido.especialidade = especialidade
                    # print(f"Data - {paciente_escolhido.data}")
                    # print(f"Hora - {paciente_escolhido.hora}")
                    # print(f"Especialidade - {paciente_escolhido.especialidade}")
                    agendamentos.append(paciente_escolhido)
        
    else:
        print("A data inserida é posterior à data atual e é inválida.")
    # entrada_hora_str = input("Digite a hora (formato HH:MM): ")
    # hora = datetime.strptime(entrada_hora_str, "%H:%M").time()
    # # print(hora)
    # especialidade = input("Qual especialidade deseja marcar?\n>>> ")

    # for paciente in agendamentos:
    #     # print("ENTRA FOR")
    #     # print(cadastro)
    #     if (data != paciente.data) and (hora != paciente.hora):
    #         print("ENTRA 1")
    #         repetido = False
    #         continue
    #     else:
    #         print("ENTRA 2")
    #         repetido = True
    #         print("Consulta indisponível, marque novamente")
    #         break
    # if repetido == False:
    #             print("ENTRA 3")
    #             # pacientes_cadastrados.append()
    #             print(f"\nPaciente cadastrado com sucesso\n")
    #             paciente_escolhido.data = data
    #             paciente_escolhido.hora = hora
    #             paciente_escolhido.especialidade = especialidade
    #             # print(f"Data - {paciente_escolhido.data}")
    #             # print(f"Hora - {paciente_escolhido.hora}")
    #             # print(f"Especialidade - {paciente_escolhido.especialidade}")
    #             agendamentos.append(paciente_escolhido)

    # for index, paciente in enumerate(agendamentos):
    #             # print(f"{index} - {paciente.data} - {paciente.hora} - {paciente.especialidade}")
    #             if (data != paciente.data) and (hora != paciente.hora):
    #                 print("ENTRA 1")
    #                 repetido = False
    #                 continue
    #             else:
    #                 print("ENTRA 2")
    #                 repetido = True
    #                 print("Consulta indisponível, marque novamente")

    #             if repetido == False:
    #                 print("ENTRA 3")
    #                 # pacientes_cadastrados.append()
    #                 print(f"\nPaciente cadastrado com sucesso\n")
    #                 paciente_escolhido.data = data
    #                 paciente_escolhido.hora = hora
    #                 paciente_escolhido.especialidade = especialidade
    #                 # print(f"Data - {paciente_escolhido.data}")
    #                 # print(f"Hora - {paciente_escolhido.hora}")
    #                 # print(f"Especialidade - {paciente_escolhido.especialidade}")
    #                 agendamentos.append(paciente_escolhido)
    

    # if repetido == False:
    #     # pacientes_cadastrados.append()
    #     print(f"\nPaciente cadastrado com sucesso\n")
    #     paciente_escolhido.data = data
    #     paciente_escolhido.hora = hora
    #     paciente_escolhido.especialidade = especialidade
    #     # print(f"Data - {paciente_escolhido.data}")
    #     # print(f"Hora - {paciente_escolhido.hora}")
    #     # print(f"Especialidade - {paciente_escolhido.especialidade}")
    #     agendamentos.append(paciente_escolhido)
        
    # for cadastro in pacientes_cadastrados:
    #     # print("ENTRA FOR")
    #     # print(cadastro)
    #     if telefone == cadastro.telefone:
    #         repetido = True
    #         # print("ENTRA IF")
    #         # print("Telefone já cadastrado")
    #         break
    #     else:
    #         repetido = False
    #         # print("ENTRA ELSE")

    # paciente_escolhido.data = data
    # paciente_escolhido.hora = hora
    # paciente_escolhido.especialidade = especialidade
    
    # print(f" Teste 2 - {paciente_escolhido}\n\n\n")
    # paciente_escolhido.especialidade = input("Qual a especialidade deseja para a consulta?")

    # print(f"Data - {paciente_escolhido.data}")
    # print(f"Hora - {paciente_escolhido.hora}")
    # print(f"Especialidade - {paciente_escolhido.especialidade}")
    
    # lista_marcacao = [paciente_escolhido.data, paciente_escolhido.hora, paciente_escolhido.especialidade]

def remarcacao():
    escolha_agendamento = int(input("\nDigite o número do paciente que deseja marcar uma consulta: "))
    paciente_escolhido = agendamentos[escolha_agendamento]
    limpa_tela()
    print(f"\nVocê escolheu o paciente {paciente_escolhido.nome}")
    remarcar = int(input("Agora escolha o procedimento:\n1 - Cancelar consulta\t 2 - Remarcar consulta\n>>> "))
    if remarcar == 1:
        # print("CANCELAR")
        mostra_agendamentos(pacientes_cadastrados, agendamentos)
        paciente_escolhido.data = None
        paciente_escolhido.hora = None
        paciente_escolhido.especialidade = None
        agendamentos.remove(paciente_escolhido)
        # print(str(paciente_escolhido))
        # print(agendamentos)
        # mostra_agendamentos(pacientes_cadastrados, agendamentos)

    elif remarcar == 2:
        agendamentos.remove(paciente_escolhido)
        dados_agendamento(paciente_escolhido,agendamentos)
        # print(str(paciente_escolhido))


pacientes_cadastrados = []
agendamentos = []
while True:
    # p = Paciente
    try:
        print("\nBem vindo(a) ao sistema de agendamento de consultas")
        print("\n1 - Cadastrar um paciente\n2 - Marcações de consultas\n3 - Cancelamento de consultas\n4 - Sair")
        escolha = input("\nEscolha uma opção:>>> ")
        
        if escolha == "1":
            limpa_tela()
            # print("CADASTRAR\n")
            cadastrar_paciente(pacientes_cadastrados)

        elif escolha == "2":
            limpa_tela()
            # print("MARCAR\n")
            if len(pacientes_cadastrados) == 0:
                print("\nNenhum paciente cadastrado")
                continue
            print("\nLista de pacientes cadastrados:")

            mostra_paciente_enumerado(pacientes_cadastrados)

            marca_consulta(pacientes_cadastrados, agendamentos)

        elif escolha == "3":
            if len(agendamentos) > 0:
                limpa_tela()
                # print("CANCELAR/REMARCAR\n")
                mostra_agendamentos(pacientes_cadastrados, agendamentos)

                remarcacao()

            else:
                print("Sem agendamentos cadastrados")
            

        elif escolha == "4":
            limpa_tela()
            # print("SAIR")
            print("\nEncerrando programa")
            break

    except(ValueError,IndexError):
        print("\nDigite uma opção válida\n")



# ● Consultas não podem ser marcadas antes da data atual. Certifique-se de que o
# usuário não possa agendar consultas retroativas.