from fractions import gcd
from fractions import Fraction

def get_markov_form(m):
    for i in range(len(m)):
        row_sum = sum(m[i])
        if row_sum == 0:
            m[i][i] = 1
        else:
            for j in range(len(m[i])):
                m[i][j] = Fraction(m[i][j], row_sum)

def submatrix(m, rows, cols):
    sub_m = []
    for row in rows:
        tmp = []
        for col in cols:
            tmp.append(m[row][col])
        sub_m.append(tmp)
    return sub_m

def maketrix(rows, cols):
    m = []
    for row in range(rows):
        m += [[0] * cols]
    return m
    
def multiply(a, b):
    rows = len(a)
    cols = len(b[0])
    matrix_mult = maketrix(rows, cols)
    for row in range(rows):
        for col in range(cols):
            product = Fraction(0, 1)
            for i in range(len(a[0])):
                product += a[row][i]*b[i][col]
            matrix_mult[row][col] = product
    return matrix_mult

def multiply_row(m, row, k):
    n = len(m)
    a = identity(n)
    a[row][row] = k
    return multiply(a, m)
    
def add_row(m, src_row, target_row, k):
    n = len(m)
    a = identity(n)
    a[target_row][src_row] = k
    return multiply(a, m)
    
def invert(m):
    n = len(m)
    m_inverse = identity(n)
    for i in range(n):
        k = Fraction(1, m[i][i])
        m = multiply_row(m, i ,k)
        m_inverse = multiply_row(m_inverse, i ,k)
        for j in range(n):
            if i != j:
                k = -m[j][i]
                m = add_row(m, i, j, k)
                m_inverse = add_row(m_inverse, i, j, k)
    return m_inverse

def subtract(a, b):
    final = []
    for i in range(len(a)):
        tmp = []
        for j in range(len(a[0])):
            tmp.append(a[i][j] - b[i][j])
        final.append(tmp)
    return final

def identity(n):
    m = maketrix(n, n)
    for i in range(n):
        m[i][i] = Fraction(1, 1)
    return m

def lcm(l):
    initial = l[0]
    for digit in l:
        initial = initial * digit / gcd(initial, digit)
    return initial

def solution(m):
    terminal_states = []
    reg_states = []
    
    for i in range(len(m)):
        if sum(m[i]) == 0:
            terminal_states.append(i)
        else:
            reg_states.append(i)

    if len(terminal_states) == 1:
        return [1, 1]

    transform_matrix(m)

    q = submatrix(m, reg_states, reg_states)
    r = submatrix(m, reg_states, terminal_states)

    fr = multiply(invert(subtract(identity(len(q)), q)), r)

    denominator = lcm([fraction.denominator for fraction in fr[0]])

    fr = [fraction.numerator * denominator / fraction.denominator for fraction in fr[0]]

    fr.append(denominator)
    
    return fr
