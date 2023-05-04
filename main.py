quantidade= int(input('Digite um numero inteiro:'))
if quantidade <=0:
    print('número inválido')
else:
    contador=0
    i=2
    while contador < quantidade:
        for x in range(2, i):
            if i % x ==0:
                break
            else:
                print(i)
                contador+=1
            i+=1
