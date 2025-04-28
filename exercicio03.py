notas = [""]*5
soma=0
cont=0
for i in range(len(notas)):
    notas[i]= float(input("Digite a nota: "))
for x in range(len(notas)):
    soma+=notas[x]
media=soma/len(notas)
for y in range(len(notas)):
    if notas[i]>media:
        cont+=1
print(cont)