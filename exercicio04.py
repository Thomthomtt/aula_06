a=[0]*5
mult=[0]*5
for i in range(len(a)):
    a[i]=int(input("Digite um numero: "))
M=int(input("Digite um número para multiplicar: "))
for i in range(len(a)):
    mult[i]=a[i]*M
print(mult)