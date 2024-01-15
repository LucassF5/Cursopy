"""
Author: Lucas Franco Rocha

Projeto de um sistema de agendamento de consultas para uma clínica médica

O sistema deve permitir o cadastro de pacientes, com nome e telefone, 
e o agendamento de consultas, com data, hora e especialidade.

O sistema deve permitir a remoção ou remarcação de consultas agendadas.

Funcionamento do sistema:
Na tela inicial, o usuário deve escolher entre as opções:
1 - Cadastrar um paciente
2 - Marcações de consultas
3 - Cancelamento de consultas
4 - Sair

Ao escolher a opção 1, o usuário deve digitar o nome e o telefone do paciente.
O sistema deve verificar se o telefone já está cadastrado, em caso positivo,
deve retornar uma mensagem de erro, em caso negativo, deve cadastrar o paciente.

Ao escolher a opção 2, o sistema deve mostrar a lista de pacientes cadastrados
com o número(index) do paciente e seu nome. Após a escolha do paciente, o sistema
deve perguntar a data, hora e especialidade da consulta. O sistema deve verificar
se a data é posterior à data atual e se a data e hora não estão repetidas. Em caso
positivo, deve guardar os dados na lista de agendamentos.

Ao escolher a opção 3, o sistema deve mostrar a lista de agendamentos com o número(index)
do paciente, a data, a hora e a especialidade da consulta. Após a escolha do paciente,
o sistema deve perguntar se o usuário deseja cancelar ou remarcar a consulta. Em caso
de cancelamento, o sistema deve remover os dados da lista de agendamentos. Em caso de
remarcação, o sistema deve remover os dados da lista de agendamentos e perguntar a data,
hora e especialidade da consulta. O sistema deve verificar se a data é posterior à data
atual e se a data e hora não estão repetidas. Em caso positivo, deve guardar os dados na
lista de agendamentos.

Ao escolher a opção 4, o sistema deve encerrar.
"""
import os
from datetime import datetime

class Paciente:
    """
    Classe que representa um paciente

    Atributos:
        nome (str): nome do paciente
        telefone (int): telefone do paciente
        data (str): data da consulta
        hora (str): hora da consulta
        especialidade (str): especialidade da consulta

    Métodos:
        init: construtor da classe
        str: retorna uma string com os dados do paciente para o usuário
        repr: retorna uma string com os dados do paciente para o desenvolvedor.
    """
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
        return f"Nome: {self.nome} - Telefone: {self.telefone} - Data: {self.data} - Hora:{self.hora} - Especialidade:{self.especialidade}"
    
    def __repr__(self):
        return f"Paciente(nome={self.__nome}, telefone={self.__telefone}, data={self.__data}, hora={self.__hora}, especialidade={self.__especialidade}"


def cadastrar_paciente(pacientes_cadastrados):
    """
    Função que cadastra um paciente

    Esta função recebe nome e telefone do paciente e verifica se o telefone já está cadastrado
    Em caso positivo, retorna uma mensagem de erro
    Em caso negativo, cadastra o paciente na lista de pacientes cadastrados

    Args:
        pacientes_cadastrados (list): lista com os pacientes cadastrados
    """
    repetido = False
    nome = input("\nDigite o nome do paciente: ")
    telefone = int(input("Digite o telefone do paciente(ex:40028922):>>> "))
    p = Paciente(nome, telefone)

    for cadastro in pacientes_cadastrados:
        if telefone == cadastro.telefone:
            repetido = True
            break

        else:
            repetido = False

    if repetido:
        print("Telefone já cadastrado")
    else:
        pacientes_cadastrados.append(p)
        print(f"\nPaciente cadastrado com sucesso")

def mostra_paciente_enumerado(pacientes_cadastrados):
    """
    Função que mostra os pacientes cadastrados

    Esta função recebe a lista de pacientes cadastrados e apresenta o resultado
    da iteração na lista com o número(index) do paciente e seu nome.
    """
    for index, paciente in enumerate(pacientes_cadastrados):
        print(f"Número: {index} - Nome: {paciente.nome}")

def mostra_agendamentos(paciente, agendamentos):
    """
    Função que mostra os agendamentos
    Esta função recebe a lista de pacientes cadastrados e a lista de agendamentos
    e apresenta o resultado da iteração na lista de agendamentos com o número(index) do paciente,
    a data, a hora e a especialidade da consulta.
    """
    for index, paciente in enumerate(agendamentos):
        print(f"Número: {index} - Data: {paciente.data} - Hora: {paciente.hora} - Especialidade: {paciente.especialidade}")

def limpa_tela():
    """
    Função que limpa a tela do terminal, facilitando a visualização do usuário
    """
    os.system("cls")

def marca_consulta(pacientes_cadastrados, agendamentos):
    """
    Função que marca uma consulta
    Esta função recebe a lista de pacientes cadastrados e a lista de agendamentos
    e apresenta o resultado da iteração na lista de pacientes cadastrados com o número(index) do paciente
    e seu nome. Após a escolha do paciente, a função chama a função dados_agendamento
    que recebe o paciente escolhido e a lista de agendamentos.
    """
    escolha_paciente = int(input("\nDigite o número do paciente que deseja marcar uma consulta:>>> "))
    paciente_escolhido = pacientes_cadastrados[escolha_paciente]
    print(f"\nVocê escolheu o paciente {paciente_escolhido.nome}")

    dados_agendamento(paciente_escolhido,agendamentos)

def dados_agendamento(paciente_escolhido,agendamentos):
    """
    Função que guarda os dados do agendamento na lista de agendamentos

    Esta função recebe o paciente escolhido e a lista de agendamentos
    e apresenta faz a verificação da data e hora da consulta, se a data é posterior à data atual
    e se a data e hora não estão repetidas. Em caso positivo, guarda os dados na lista de agendamentos.

    Args:
        paciente_escolhido (Paciente): paciente escolhido para o agendamento
        agendamentos (list): lista de agendamentos
    """
    repetido = False
    data_atual = datetime.now()

    input_data = input("Digite a data (formato DD/MM/AA):>>> ")
    data = datetime.strptime(input_data, "%d/%m/%y")

    if data >= data_atual:
        data = input_data
        entrada_hora_str = input("Digite a hora (formato HH:MM):>>> ")
        hora = datetime.strptime(entrada_hora_str, "%H:%M").time()
        especialidade = input("Qual especialidade deseja marcar?\n>>> ")

        for paciente in agendamentos:
            if (data != paciente.data) and (hora != paciente.hora):
                repetido = False
                continue

            else:
                repetido = True
                print("Data e/ou horário de consulta indisponível, tente novamente")
                break

        if repetido == False:
                    print(f"\nPaciente cadastrado com sucesso\n")
                    paciente_escolhido.data = data
                    paciente_escolhido.hora = hora
                    paciente_escolhido.especialidade = especialidade
                    agendamentos.append(paciente_escolhido)
        
    else:
        print("A data inserida é anterior à data atual e é inválida.")

def remarcacao():
    """
    Função que remaneja/cancela uma consulta
    Esta função recebe a lista de agendamentos e apresenta o resultado da iteração na lista de agendamentos
    com o número(index) do paciente, a data, a hora e a especialidade da consulta. Após a escolha do paciente,
    a função chama a função remarcar que recebe a lista de agendamentos e o paciente escolhido.

    Esta função também permite o cancelamento de uma consulta, caso o usuário escolha a opção 1.

    Caso o usuário escolha a opção 2, a função chama a função dados_agendamento que recebe o paciente escolhido
    e a lista de agendamentos. Fazendo com que o paciente possa alterar a data, hora e especialidade da consulta.

    Args:
        agendamentos (list): lista de agendamentos
    """
    escolha_agendamento = int(input("\nDigite o número do paciente que deseja marcar uma consulta:>>> "))
    paciente_escolhido = agendamentos[escolha_agendamento]

    limpa_tela()
    print(f"\nVocê escolheu o paciente {paciente_escolhido.nome}")
    remarcar = int(input("Agora escolha o procedimento:\n1 - Cancelar consulta\t 2 - Remarcar consulta\n>>> "))

    if remarcar == 1:
        paciente_escolhido.data = None
        paciente_escolhido.hora = None
        paciente_escolhido.especialidade = None
        agendamentos.remove(paciente_escolhido)

    elif remarcar == 2:
        agendamentos.remove(paciente_escolhido)
        dados_agendamento(paciente_escolhido,agendamentos)


pacientes_cadastrados = [] # Lista de pacientes cadastrados
agendamentos = [] # Lista de agendamentos

while True: # Loop que mantém o programa em execução
    try:
        print("\nBem vindo(a) ao sistema de agendamento de consultas")
        print("\n1 - Cadastrar um paciente\n2 - Marcações de consultas\n3 - Cancelamento de consultas\n4 - Sair")
        escolha = input("\nEscolha uma opção:>>> ")
        
        if escolha == "1":
            limpa_tela()
            cadastrar_paciente(pacientes_cadastrados)

        elif escolha == "2":
            limpa_tela()
            if len(pacientes_cadastrados) == 0:
                print("\nNenhum paciente cadastrado")
                continue

            print("\nLista de pacientes cadastrados:")
            mostra_paciente_enumerado(pacientes_cadastrados)
            marca_consulta(pacientes_cadastrados, agendamentos)

        elif escolha == "3":
            if len(agendamentos) > 0:
                limpa_tela()
                mostra_agendamentos(pacientes_cadastrados, agendamentos)
                remarcacao()

            else:
                print("Sem agendamentos cadastrados")
            
        elif escolha == "4":
            print("\nPrograma encerrado")
            break

        else:
            limpa_tela()
            print("Por favor, digite um dos valores indicados")

    except(ValueError,IndexError):
        print("\nDigite uma opção válida\n")
