print(float(0.1))

print(float('0.25'))


aa = format(0.1,'.20f')

print(aa)

x = .1 +.1 + .1
y= .3



print(x == y)

a = 1.0
while a!= format(0.1,'.1f'):
    print(a)
    a = a - format(0.1,'.1f')
print('fin')


def error(x,y):

    """
    Recibe dos números x e y y calcula el error de aproximar x usando y en float64
    
    """

def error_relativo(x,y):
    """
    recibe dos números x e y y calcula el error relativo de aproximar x usando y en float64
    """

def matricesIguales(A,B):
    """
    Devuelve True si ambas matrices son iguales y False en otro caso.
    Considerar que las matrices pueden tener distintas dimensiones, ademas de distintos valores
    """