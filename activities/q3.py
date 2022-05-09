import numpy as np
import math

def bissecao(f, a, b, ATOL):
    n = np.ceil(np.log2((a+b)/(2*ATOL)))
    a_alg = a
    b_alg = b
    
    for _ in range(int(n)):
        p = (a_alg + b_alg) / 2
        fp = f(p)
        
        if f(a_alg) * fp < 0: b_alg = p
        else: a_alg = p   
    
    return p


def f(x):
    return( 2.0*math.sin(2.0*x) - x**3 + 3.0)

def false_position():
    l = 0.000001
    tol = 0.000001
    Ni = 100
    cont = 0
    a = float(input("Entre com o valor de 'a' do intervalo [a;b]: "))
    b = float(input("Entre com o valor de 'b' do intervalo [a;b]: "))
    c = b - a
    x0 = (a*f(b) - b*f(a))/(f(b) - f(a))

    while(c > l or math.fabs(f(x0)) > tol):
        if(f(a)*f(x0) < 0.0):
            b = x0
        if(f(a)*f(x0) > 0.0):
            a = x0
        c = b - a
        x0 = (a*f(b) - b*f(a))/(f(b) - f(a))
        cont = cont + 1
        if(cont >= Ni):
            break

    print("\n\nRaíz: %f\nIterações: %i\nf(%f) = %g" %(x0,cont,x0,f(x0)))


def secante(f,xat,xant,*args):
    """
    Primeiro argumento livre é o contador e o segundo é a tolerância. Se não for preenchido, tolerância é de 10⁻5
    e o contador máximo é 200
    """
    if not args:
        tol = 1e-5
        contador = 200
    elif len(args) == 1:
        tol = 1e-5
        contador = args[0]
    else:
        tol = args[1]
        contador = args[0]
    cont = 0
    tol = 1e-5
    while True:
        xsuc = xat - ((xat - xant)/(f(xat) - f(xant)))*f(xat)
        erro = abs((xsuc - xat)/xsuc)
        xant = xat
        xat = xsuc
        cont += 1
        if cont>contador:
            break
        if erro<tol:
            break
    return float('%.2f'%xat)