# Contando de 1 a 10
for x in range(1,11,1):
  print(x)

# Contando de 2 em 2 de 1 a 50
for x in range(1,51,2):
  print(x)

# Contando quantos numeros são par nos digitados
cont=0
for x in range(4):
  nr = int(input("Numero: "))
  if(nr%2 == 0):
    cont = cont+1
print("O total de números pares na lista é",cont)

# Somando todos números digitados
cont=0
for x in range(6):
  nr = int(input("Numero: "))
  cont=cont+nr
print("A soma de todos os números é",cont)
