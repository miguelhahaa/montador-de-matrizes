import os 
matriz=[]
linha=[]
infor={
    'colunas':0,
    'linhas':0,
}
vazio="x"
os.system('clear')
while True:
    print(linha)
    termo=input("Digite o termo: ")
    if termo=="":
        matriz.append(linha.copy())
        infor['colunas']=len(linha)
        linha.clear()
        break
    if termo != "":
        linha.append(int(termo))
    os.system('clear')

while True:
    os.system('clear')
    for x in range (0,len(matriz[0])-len(linha)):
        linha.append(vazio)
    for x in matriz:
        print(x)
    print(linha)
    for x in range (0,linha.count("x")):
        linha.pop()
    termo=input("Digite o termo: ")
    if len(linha)==0:
        if termo=="":
            os.system('clear')
            break
    if len(linha)<infor['colunas']:
        linha.append(int(termo))
    if len(linha)==infor['colunas']:
        matriz.append(linha.copy())
        linha.clear()
infor['linhas']=len(matriz)

for x in matriz:
    print(x)
print(f'colunas:{infor["colunas"]},linhas:{infor["linhas"]}')