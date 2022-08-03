import numpy as np
import math

# Variaveis
# cpf = [0]*11
Controle = [0]*2
digito = [0]*2
soma = 0
soma2 = 0
resto = 0
resto2 = 0
x = 10
y = 11


#COLOCAR O CPF
cpf = str(input("Digite os 9 primeiros digitos do CPF:"))
lista_CPF = [int(d) for d in str(cpf)]
nova_lista = np.zeros(9)
Controle = str(input("Digite o ultimos dois digitos de controle:"))

#SOMA DOS CADA DIGITO DO CPF
for i in range(9):
    soma = soma + (lista_CPF[i] * x)
    x-=1

print(f"A soma pro 1 digito: {soma}")
resto = soma % 11
#TESTE DO PRIMEIRO DIGITO DE CONTROLE
if(resto >= 2):
    digito1 = 11 - resto
else:
    digito1 = 0

lista_CPF.append(int(digito1))

#TESTE DO 2 DIGITO
for i in range(10):
    soma2 = soma2 + (lista_CPF[i] * y)
    y-=1

print(f"A soma pro 2 Digito: {soma2}")
resto2 = soma2 % 11

if(resto2 >= 2):
    digito2 = 11 - resto2
else:
    digito2 = 0
   
lista_CPF.append(int(digito2))

CPF_total = ''
DC_correto = ''

for i in range(11):
  CPF_total += str(lista_CPF[i])

##Recebe os dígitos de validação
DC_correto += str(int(digito1))
DC_correto += str(int(digito2))
#VERIFICANDO SE É VALIDO
if(Controle == DC_correto):
    print("CPF é valido")
    print(f"O CPF:{CPF_total}")
else:
    print("CPF invalido")
    print(f"O digito controlador certo é:{DC_correto}")
    print(f"O CPF correto é: {CPF_total}")