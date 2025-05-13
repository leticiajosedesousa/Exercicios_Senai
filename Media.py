from colorama import init, Fore
init(autoreset=True)
Nome = input('qual é o nome do aluno? ')
n1 = float(input('primeira nota: '))
n2 = float(input('segunda nota: '))
n3 = float(input('terceira nota: '))
media = round((n1+n2+n3) /3, 2)
print(media)
print('a aluna' , Nome , 'tirou' , media)
if media>=5:
    print(Fore.GREEN+'aprovado')
else:
    print(Fore.RED+'reprovado')   
