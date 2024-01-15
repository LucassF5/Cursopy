
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
        return f"Nome: {self.nome} - Telefone: {self.telefone} - Data: {self.data} - Hora:{self.hora} - Especialidade:{self.especialidade}"
    
    def __repr__(self):
        return f"Paciente(nome={self.__nome}, telefone={self.__telefone}, data={self.__data}, hora={self.__hora}, especialidade={self.__especialidade}"


def cadastrar_paciente(pacientes_cadastrados):
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
    for index, paciente in enumerate(pacientes_cadastrados):
        print(f"Número: {index} - Nome: {paciente.nome}")

def mostra_agendamentos(paciente, agendamentos):
    for index, paciente in enumerate(agendamentos):
        print(f"Número: {index} - Data: {paciente.data} - Hora: {paciente.hora} - Especialidade: {paciente.especialidade}")

def limpa_tela():
    os.system("cls")

def marca_consulta(pacientes_cadastrados, agendamentos):
    escolha_paciente = int(input("\nDigite o número do paciente que deseja marcar uma consulta:>>> "))
    paciente_escolhido = pacientes_cadastrados[escolha_paciente]
    print(f"\nVocê escolheu o paciente {paciente_escolhido.nome}")

    dados_agendamento(paciente_escolhido,agendamentos)

def dados_agendamento(paciente_escolhido,agendamentos):
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


pacientes_cadastrados = []
agendamentos = []

while True:
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
