user=[""]*5
passw=[0]*5
for i in range(len(user)):
    user[i]=input("Digite o usuario: ")
    passw[i]=int(input("Digite a senha: "))
for x in range(len(user)):
    print(f"Aqui está a lista dos usuarios: nome: {user[x]}, senha: {passw[x]} posição: {[x]}")