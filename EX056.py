soma = 0
média = 0
nomevelho = ' '
maioridadehomem = 0
totmulher = 0
for p in range (1, 5):
    print("{}ª pessoa ->".format(p))
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip()
    soma += idade
    if p == 1 and sexo in "Mm":
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Mm" and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Ff" and idade < 20:
        totmulher += 1

media = soma / 4

print("A média de idade do grupo é de {} anos.".format(media))
print("O nome do homem mais velho do grupo é {} e ele tem {} anos.".format(nomevelho, marioridadehomem))
print("O grupo tem {} mulher(es) com menos de 20 anos.".format(totmulher))
