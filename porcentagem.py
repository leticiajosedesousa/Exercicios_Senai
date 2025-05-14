# • Cálculo de Porcentagem de um Número.
# • O programa deve calcular e exibir o valor que corresponde a essa
# porcentagem do total. Exemplo: se o usuário digitar 200 como
# valor total e 15 como porcentagem, o programa deverá calcular
# que 15% de 200 é 30.
# • Exemplo de fórmula:
# valor_parte = valor_total * (porcentagem / 100)

#15% de 200 é 30
produto = input('qual é o produto? ')



total =int(input('qual é o valor total? '))
porcentagem = int(input('qual é a porcentagem desse numero? '))
resultado = total * (porcentagem / 100)
print(porcentagem , '% de R$' , total , 'é R$' , resultado)
desconto = total - resultado 
print('o valor do' , produto , 'com R$', resultado, 'de desconto é: R$' , desconto )