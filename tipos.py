#TIPOS DE DADOS 

#-------------------------------------------- STRING (str) ---------------------------------------------
# strings são textos, eles devem estar com aspas simples ' ' ou aspas duplas " "

texto1 = 'oii'
texto2 = "tudo bom?"
#use o comando type() para verifcar o tipo de dado em uma variável
print(type(texto1))

#-------------------------------------------Inteiros (int) -----------------------------------------------
# Os inteiros são números inteiros e podem ser utilizados para operações matemáticas
numero1 = 10
numero2 = 30
print(type(numero1))
print(numero1+numero2)
print(numero1 * texto1) # É possivel multiplicar inteiros com string

#--------------------------------------------- Decimais (float) -----------------------------------------
# Para numeros não inteiros, usamos a representeção de "ponto flutuante" ou seja "float"
numero3 = 3.5 #(numeros quebrados)
numero4 = 5.7
print(type(numero3))

#------------------------------------------ lógico (bool) ----------------------------------------------
# quando falamos em tipos de dados imaginamos "verdadeiro" ou "falso" (true, false)
# em python classificamos esse tipo de booleano bool 

v = True
f = False
print(type(v))