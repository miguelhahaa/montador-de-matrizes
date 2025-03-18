import os 
matriz=[]
coluna=[]
infor={
    'colunas':0,
    'linhas':0,
}
vazio="x"
os.system('clear')
while True:
    print(coluna)
    termo=input("Digite o termo: ")
    if termo=="":
        matriz.append(coluna.copy())
        infor['colunas']=len(coluna)
        coluna.clear()
        break
    if termo != "":
        coluna.append(int(termo))
    os.system('clear')

while True:
    os.system('clear')
    for x in range (0,len(matriz[0])-len(coluna)):
        coluna.append(vazio)
    for x in matriz:
        print(x)
    print(coluna)
    for x in range (0,coluna.count("x")):
        coluna.pop()
    termo=input("Digite o termo: ")
    if len(coluna)==0:
        if termo=="":
            os.system('clear')
            break
    if len(coluna)<infor['colunas']:
        coluna.append(int(termo))
    if len(coluna)==infor['colunas']:
        matriz.append(coluna.copy())
        coluna.clear()
infor['linhas']=len(matriz)

for x in matriz:
    print(x)
print(f'linhas:{infor['linhas']},colunas:{infor['colunas']}')