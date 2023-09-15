# Loop irá parar apenas quando o numero 0 for digitado
cont=0
nr=1
while(nr !=0):
  nr=int(input("Digite o número: "))
  cont=cont+1

print("Você digitou", cont - 1,"numeros")


#Loop irá parar quando o 1º numero for maior que o 2º
nr=0
nr2=2
while(nr < nr2):
  print("")
  nr=int(input("Digite o 1º Numero: "))
  print("")
  nr2=int(input("Digite o 2º Numero: "))

print("")
print("1º numero maior que o 2º")

#Calculo de juros no banco
cont=0
valor = int(input("Quanto você quer juntar: "))
inicio = int(input("Quantidade Inicial: "))
juros = float(input("Quantidade de Juros: "))
depo = int(input("Valor deposio mensal: "))
subtotal=0
total= inicio
while(total <= valor):
  subtotal = total*(juros/100)
  total = total + subtotal + depo
  print(total)
  cont=cont+1
print("Levou", cont,"meses para juntar", valor,"ou", cont/12,"anos")
