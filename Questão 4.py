separarPalavra = []
vogais = []
vogais2 = []
vogais3 = []
vogais4 = []
vogais5 = []
n = 0
palavra = str(input("")).lower()
while n < 1:
    for i in palavra:
        separarPalavra.append(i)
        if i in "aáã":
            vogais.append(i)
            separarPalavra.remove(i)
        elif i in "eéê":
            vogais2.append(i)
            separarPalavra.remove(i)
        elif i in "ií":
            vogais3.append(i)
            separarPalavra.remove(i)
        elif i in "oó":
            vogais4.append(i)
            separarPalavra.remove(i)
        elif i in "uú":
            vogais5.append(i)
            separarPalavra.remove(i)
    n = n + 1    
    print("A: {}" .format(len(vogais)))
    print("E: {}" .format(len(vogais2)))
    print("I: {}" .format(len(vogais3)))
    print("O: {}" .format(len(vogais4)))
    print("U: {}" .format(len(vogais5)))
    
    separarPalavra.clear()
    vogais.clear()   
