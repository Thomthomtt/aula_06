#fiz do jeito mais porco possivel sono duca boy
# aluno = [input("Digite seu nome: "),input("Digite seu nome: "),input("Digite seu nome: "),input("Digite seu nome: "),input("Digite seu nome: ")]
# print(aluno)

###codigo do professor(segundo exercicio)

# alunos=[""]*5
# for i in range(len(alunos)):
#     alunos[i]=input("Digite seu nome: ")
# for x in range(len(alunos)):
#     print(f"{alunos[x]} está na posição {x}")

###codigo do terceiro exercicio

nomes=["Taynara", "Raynara", "Joao", "Lopes", "Felix"]
posicao=input("Digite um nome: ")
for x in range(len(nomes)):
    if posicao == nomes[x]:
     print(f"Ele está no nosso banco de dados! Aqui esta: {nomes[x]} está na posição {x}")