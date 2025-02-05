#calculadora de média by Luigi 5168 2B
from statistics import mean
print("\n\n________________________________________________\n\n_Calculadora de média trimestral de 3 elementos_\n________________________________________________\n")
#input das matérias
while True:
    try:
        mate = int(input("Quantas matérias serão calculadas?"))
        break;
    except ValueError:
        print("Valor Inválido \n")
mediasfinais = []
e = 0
for b in range(mate): #laço para a quantidade de matérias
    n = {}
    x = 0
    k = 2
    y = 1
    print("\n________________________________________________\nMatéria {}:".format((b+1)))
    print("\nTrimestre 1\n")
    while x < 9 : #input das notas
        while True:
            try:
                n[x] = float(input("N{}: ".format((y))))
                break;
            except ValueError:
                print("\nValor Inválido! ")
        x=x+1
        y=y+1
        if x % 3 == 0 and x<9: 
            print("\nTrimestre {}".format(k))
            k=k+1
            y=y-3
    #calculo das médias
    m1 = (n[0]+n[2]+n[1])/3
    m2 = (n[4]+n[5]+n[3])/3
    m3 = (n[7]+n[6]+n[8])/3
    mf = ((2*m1)+(2*m2)+(3*m3))/7
    medias = [m1,m2,m3]
    for i in range(3): #avaliação das médias
        print("\nMédia Trimeste {0}: {1:2.3}".format((i+1),medias[i]))
        if medias[i] < 6:
            rec = 12 - medias[i]
            print("Nota necessária na recuperação:{0:2.3}".format(rec))
    print("\nMédia final:{0:2.3}".format(mf))
    if mf < 6:
        print("Voce está de exame!")
        e = e+1
    else:
        print("Matéria aprovada!")
    b +=1 #avaliação das médias gerais
    mediasfinais.append(mf)
    mff = mean(mediasfinais)
print("\n________________________________________________\n")
if b >1: 
    print("\n A média das matérias é:{0:2.3}".format(mff))
if e > 3:
    print("\nVoce foi reprovado!\nMatérias reprovadas:",e)
elif 1<=e<=3:
    print("\nVoce esta de exame em {} matéria(s)".format(e))
elif e==0:
    print("\nParabéns passou direto!")