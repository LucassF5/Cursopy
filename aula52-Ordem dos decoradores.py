# Ordem dos decoradores
def parametros_decorador(nome):  # Aqui pega o nome da função
    def decorador(func):  # Aqui pega a função
        print('Decorador:', nome)

        def sua_nova_funcao(*args, **kwargs):
            res = func(*args, **kwargs)  # Aqui executa a função
            # Aqui junta o resultado e soma com o nome dado no decorador
            final = f'{res} {nome}'
            return final
        return sua_nova_funcao
    return decorador


@parametros_decorador(nome='5')
@parametros_decorador(nome='4')
@parametros_decorador(nome='3')
@parametros_decorador(nome='2')
@parametros_decorador(nome='1')
def soma(x, y):
    return x + y


dez_mais_cinco = soma(10, 5)
print(dez_mais_cinco)
