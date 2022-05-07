# <center> Sistemas Lineares

- Operações elementares
    1. Trocar linhas
    2. Multiplicar uma linha por uma constate $\neq 0$
    3. Somar uma linha, multiplicada por uma constante, à outra

- Determinante:
    1. Transformar matriz em triangular
    2. DET = Multiplicação dos elementos da diagonal principal

### Resolução de Sistemas Lienares
#### Métodos iterativos
$\rightarrow$ Começa com uma aproximação inicial $X^{0}$ e, a partir dela, gera uma sequência de outras aproximações que convergem para a solução.

$\rightarrow x = F \cdot x + d$ - `Há varias formas`

- Ex: $Ax = b \rightarrow Ax + Ix - Ix = b \newline \rightarrow Ax + Ix - b = Ix \newline \rightarrow x = (A+I)x - b$

#### Método de Jacobi

$a_{11}x_1 + a_{12}x_2 + ... + a_{1N}x_N = b_1$
.
.
.
$a_{N1}x_1 + a_{N2}x_2 + ... + a_{NN}x_N = b_N$

$ \rightarrow $  
$x_1 = \dfrac{b_1 - (a_{12}x_2 + a_{13}x_3 + ... + a_{1N}x_n)}{a_{11}}$
.
.
.
$x_n = \dfrac{b_n - (a_{n1}x_1 + ... + a_{NN}x_{n-1})}{a_{NN}}$

__Obs:__ Se $a_{ii} = 0 \text{ para algum i} \rightarrow$ Trocar linhas ou colunas.

$\rightarrow$

$x = [{x_1} ... x_n]$ , $d = []$, $f = [0 | \dfrac{-a_{12}}{a_{11}}|\dfrac{-a_{13}}{a_{11}} ... \dfrac{-a_{1N}}{a_{11}}]$ (Estruturar em coluna, ambos)

- Procedimento
    a)


### Teorema : É condiçãõ suficente para que  $ x = Fx + d $ convirja, que $F$ satisfaça:

$  $