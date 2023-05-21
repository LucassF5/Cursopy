# dir, hasattr e getattr em Python

# dir no debug console serve pra ver se tal objeto possui determinado método
# Ex: dir(string) -> vai mostrar as funções que podem ser aplicadas a ele

#  hasattr checa se determinado objeto tem determinado nome dentro dele

# getattr executa tal ação com o parâmetro passado

string = 'Luiz'
metodo = 'strip'

if hasattr(string, metodo):
    print('Existe upper')
    print(getattr(string, metodo)())
else:
    print('Não existe o método', metodo)