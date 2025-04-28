usuarios=["joao", "carlos", "mario", "maria", "josefa"]
senhas=[1234, 3432, 5432, 3333, 6666]
user=input("Digite seu Usuarios: ")
passw=int(input("Digite sua senha: "))
for i in range(5):
    if usuarios[i]!=user and senhas[i]!=passw:
        print("Login falhou")
    else:
        print("Login efetuado com sucesso!")