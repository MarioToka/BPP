def es_primo(n):
    primo = True
    for i in range(2,n):
        if(n%i == 0):
            primo = False
    return primo

aux = [3,4,8,5,5,22,13]
aux2 = list(filter(es_primo, aux))
print(aux2)