from colorama import init, Fore
init(autoreset=True)
filme = input('qual é o seu filme favorito? ')
if filme == 'harry potter': 
    print('o meu tambem!!')
else:
    print('o meu favorito é piratas do caribe')
personagem = input(' e qual é o seu personagem favorito? ')
if personagem =='draco malfoy':

    print('o meu tambem!!')
else:
    print(Fore.RED+'o meu é o sirius')
                   