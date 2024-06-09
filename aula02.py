# -*- coding: utf-8 -*-
"""Aula02.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mKzHw7-8GahlXvy1PihvsI-0GQZDXMZd

#Dia 2

##Estruturas Condicionais simples e compostas, operações condicionais e estrutura de repetição for

#Condicional composta
Se está frio, pego um casaco. Senão, coloco uma bermuda e um chinelo.

Se está calor, tomo um sorvete. Senão, bebo um
chocolate quente.
"""

x = int(input("Sua idade: "))
if x >= 18:
  print("Você já pode dirigir.")
else:
  print("Você não tem idade para dirigir.")

x = float(input("Valor livro 1: "))
y = float(input("Valor livro 2: "))

if x > y:
  print("O livro 1 é mais caro.")
elif x < y:
  print("O livro 2 é mais caro")
else:
  print("Os livros tem o mesmo valor.")

#Exercício: Ano Bissexto
#Esse programa solicita ao usuário que ele informe um ano e determina se ele é um ano bissexto ou não.

ano = int(input("Ano: "))
if ano%4 == 0 and ano%400 == 0 or ano%100 != 0:
  print("O ano é bissexto")
else:
    print("O ano não é bissexto")

#Exercício: Aprovação
#Esse programa lê a nota de um aluno e informa se ele foi aprovado, reprovado ou está de recuperação

nota = float(input("Digite a sua nota: "))
if nota < 5:
  print("Reprovado")
elif nota >= 5 and nota <=7:
  print("Você está de recuperação")
elif nota > 7 and nota <= 10:
  print("Aprovado")

#Exercício: Voto
#Esse programa pergunta a idade do usuário e informa se ele tem idade para votar ou não.

idade = int(input("Digite sua idade: "))
if idade < 16:
  print("Você não tem idade para votar.")
elif idade >= 18 and idade <= 65:
  print("Voto obrigatório.")
else:
  print("Voto facultativo.")

#Exercício: Maior de idade
#Verifica se o usuário é maior de idade, e se ele pode ou não beber.

idade = int(input("Idade: "))
if idade >= 18:
  print(f"Você tem {idade} anos, pode beber.")
elif idade < 18:
  print(f"Você tem {idade} anos, não pode beber.")

"""Mas e se tivermos mais de duas condições?

Em Python, usamos a estrutura

if...

elif (else if)...

else
"""

idade = int(input("Idade: "))
if idade >= 18 and idade <= 60:
  print("Você é adulta.")
elif idade < 18 and idade >= 12:
  print("Você é adolescente.")
elif idade <12 and idade >= 0:
  print("Você é criança.")
else:
  print("Você é idosa.")

#Exercício: O pragrama deve informar se o número é par ou ímpar e se ele é maior ou igual a 100.

numero = int(input("Digite um número: "))

if numero % 2 == 0 and numero < 100:
  print("O número é par e é menor que 100.")

elif numero % 2 == 0 and numero >= 100:
  print("O número é par e é maior ou igual a 100.")

elif numero % 2 != 0 and numero < 100:
  print("O número é impar e é menor que 100.")

else:
  print("O número é ímpar e é maior ou igual a 100.")

#.lower()
#função já estabelecida do Python que transforma todos os caracteres em minúsculo
nome = input("Nome: ").lower()
print(nome)

#.upper()
#função já estabelecida do Python que transforma todos os caracteres em maiúsculo
nome = input("Nome: ").upper()
print(nome)

#Exercício: solicite à usuária que digite o nome e a idade e depois, imprime na tela estas informações.
nome = input("Digite o nome: ")
idade = input("Digite a idade: ")
print(f"O nome é {nome} e tem {idade} anos.")

"""#Laços de repetição ou Loops

#Repetições no dia a dia

Exemplo:
Dirigir = Ação

Até chegar ao destino = Condição

As repetições, também chamadas de laços ou loops,
são usadas quando queremos fazer a mesma coisa
várias vezes sem ter que repetir o código.

Dessa forma, não há a necessidade de escrever a
mesma ação várias vezes.

#Range

Um range é um intervalo de números que você define e
que possui um início e um fim. É representado da
seguinte maneira :

range(valor_inicial,valor_final)

O valor final é utilizado para marcar o fim e não é
incluído no resultado.

Por que eu preciso do range?

No nosso caso, usaremos o range para determinar quantas vezes um determinado bloco de código será repetido em um programa
"""

sequencia = range(1,3)
print(list(sequencia))

impar = range(1, 21, 2)
for num in impar:
    print(num)

for i in range (3,9):
    print(i)

x = int(input('Valor de início da sequência: '))
y = int(input('Valor de parada da sequência: '))
for i in range(x, y):
  print(i)

"""No lugar de i você pode usar  qualquer outra variável."""

intervalo = range(0,20+1, 2)
contagem = list(intervalo)
print(contagem)

intervalo = range(1,19+1, 2)
contagem = list(intervalo)
print(contagem)

print(list(range(0,20+1, 2)))

"""#Estrutura de repetição:

#FOR

As estruturas de repetição, como o for,
ajudam a deixar o código mais conciso e
simples de ser lido e entendido.
"""

for i in range(5):
    nome = input("Nome: ")
    idade = input("Idade: ")
    print("Seu nome é " + nome + " e sua idade é " + idade + " anos.")

n = 15
for i in range(0,15):
  print(i)

n = 21
for i in range(0,21):
  print(i)

num = int(input("Quantos itens terá na nossa lista? "))
for i in range(1,num+1):
  print(i)

for i in range(3):
    nome = input("Digite o nome :")
    idade = input("Digite a idade : ")
    print("O nome é " + nome, " e tem ", idade, " anos.")

"""#Controle condicional (if/else)

Não podemos assumir que o usuário sempre fornecerá os valores corretos ou esperados.
"""

idade = int(input("Digite sua idade: "))

if idade < 0:
  print("Idade inválida.")

else:
    print(f"Você tem {idade} anos.")

"""#Atividade

Convidadas da festa:

1 - Solicite ao usuário um número de convidadas da festa e ARMAZENE EM UMA VARIÁVEL. LEMBRE DE CONVERTER A STRING PARA NÚMERO.

2 - Crie uma estrutura condicional IF-ELSE para verificar se o número de convidadas é válido, ou seja, se a variável é menor ou igual a zero.

2.1 - Se não for válido, exiba uma mensagem de erro.

2.2 - Se for válido, crie um loop FOR.

2.3 - Dentro do loop FOR, solicite a usuária o nome de cada convidada utilizando a função input()

2.4 - Utilize a função print() para exibir uma mensagem de boas-vindas para cada
convidada, exibindo seu nome.
"""

numConvidadas = int(input('Quantidade de convidadas: '))

if numConvidadas <= 0:
  print('Quantidade de convidadas inválida.')

else:
  for i in range (1, numConvidadas+1):
    nome = input('Convidada: ')
    print(f'Boas vindas {nome}')

n_convidados = int(input("Número de convidados: "))

if n_convidados <= 0:
  print("Número de convidados inválido.")

else:
  for i in range(1, n_convidados+1):
    nome = input("Nome:")
    print(f"Boas vindas {nome}")

"""#Variáveis acumuladoras

É uma variável que vai aumentando de valor usando ela mesma.
"""

a = 10
a = a + 5
a = a * 2
a = a / 3
print(a)

total = 0
total = total + 3
total = total + 4
print(total)

"""#Atividade

1 - Crie uma lista de vendas diárias, que contém os nomes de 4 produtos vendidos (qualquer nome!);

2 - Crie uma variável acumuladora e iguale a zero;

3 - Crie um loop FOR para percorrer a lista de vendas diárias e acumular o total de itens vendidos;

3.1 - Dentro do loop, incrementamos a variável acumuladora em 1 para contar cada produto vendido;

4 - Por fim, exiba o resultado da variável acumuladora.
"""

produtos_vendidos = ['camiseta', 'calça', 'moletom', 'vestido']
total = 0
for produto in produtos_vendidos:
  total = total + 1

print(f'O total de itens vendidos é: {total}')

lista = ['arroz', 'feijão', 'macarrão']
variavel_acumuladora = 0
for variavel in lista:
    variavel_acumuladora = variavel_acumuladora + 1

print(f"O total de itens vendidos é: {variavel_acumuladora}")

"""# Break

O break é usado para quebrar o loop, ou seja, para parar a execução do loop.

Quando o algoritmo encontrar o "break", ele para o loop e continua com a sequência de instruções após o loop.
"""

for i in range(1, 1524):
    print(i)

    if i == 5:
        break

"""# Atividades

# Exercício 1
Você está criando um aplicativo para auxiliar pessoas na hora de fazer compras no mercado.
Neste aplicativo a pessoa pode inserir o número de produtos que está comprando e depois o nome de cada produto e o valor.

No final, apresente para a pessoa a soma total da compra.
"""

qtde_produtos = 0

qtde_produtos = int(input('Quantidade de produtos comprados: '))
for i in range(1, qtde_produtos+1):
   nome_produto = input('Nome do produto: ')
   valor_produto = float(input('Valor do produto: '))

total = qtde_produtos * valor_produto
print(f'O total da compra é: {total}.')

"""# Exercício 3

Crie um algoritmo que possui um laço for em um range de 1 a 16, mas que pare sua execução se o valor da iteração ( i ) for maior que 10 e par.
"""

for numero in range(1, 16):
  print(numero)
  if numero > 10 and numero % 2 == 0:
    break

"""# Exercício 3

Ainda pensando no aplicativo, crie um algoritmo em Python em que a pessoa não precisa inserir o número de produtos que está comprando. Considere que o algoritmo consegue armazenar no máximo 1000 produtos.
"""

max_produtos = 1000
total = 0

for _ in range(max_produtos):
    nome_produto = input('Nome do produto: ')
    valor_produto = float(input('Valor do produto: '))
    total += valor_produto
    compra = input('Você quer continuar a compra? (sim/não): ').lower()
    if compra == 'não':
        break
    elif compra != 'sim':
        print('Opção inválida')
        break

print(f'O total da compra é: R${total}')

"""#Exercício 4

Escreva um algoritmo para ler 2 valores e se o segundo valor informado for ZERO, deve ser lido um novo valor, ou seja, para o segundo valor não pode ser aceito o valor zero. Por fim, imprima o resultado da divisão do primeiro valor lido pelo segundo valor lido.
"""

valor1 = float(input('Informe um valor: '))
valor2 = float(input('Informe outro valor: '))
if valor2 == 0:
  valor2 = float(input('Inofrme outro valor: '))

total_div = valor1 / valor2
print(total_div)

"""#Exercício 5

Escreva um algoritmo no qual a pessoa possa inserir o seu usuário e senha.

Faça a verificação da senha com uma senha já salva no código e caso essa senha não seja correta, peça novamente uma outra senha.
"""

senha_definida = '123321m'
usuario = input('Usuário: ')

for i in range(3):
  senha = input('Senha: ')
  if senha == senha_definida:
        print('Senha correta.')
        break
  elif senha != senha_definida:
        print('Senha incorreta.')
  else:
    print('Você excedeu o número máximo de tentativas.')