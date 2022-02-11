from formula import *
def DPLL(S):
    return DPLL_Check(S,[])

def DPLL_Check(S,interpretation):
    S,interpretation = unit_propagation(S,interpretation)
    if S == []:
        return interpretation
    if [] in S:
        return False
    atomic = S[0][0]
    S1 = S.copy()
    S2 = S.copy()
    S1.append([atomic])
    atomic = atomic*(-1)
    S2.append([atomic])
    result = DPLL_Check(S1,interpretation)
    if result != False:
        return result
    return DPLL_Check(S2,interpretation)


def unit_propagation(S,interpretation):
    while has_unit_clause(S):
        l = literal_unit(S)
        interpretation = interpretation + [l]
        S = remove_clauses_literal(S,l)
        S = remove_complements(S,l)
    return S,interpretation

def has_unit_clause(S):
    for clausula in S:
        cont = 0
        for elemento in clausula:
            cont = cont + 1
        if cont == 1:
            return True
    return False

def literal_unit(S):
    for clausula in S:
        cont = 0
        for elemento in clausula:
            cont = cont + 1
        if cont == 1:
            return elemento
        
def remove_clauses_literal(S,l):
    cont = 0
    t = 0
    for c in S:
        t = t+1
    while(cont < t):
        v = 0
        for elemento in S[cont]:
            if elemento == l:
                v = v + 1
        if v > 0:
            del(S[cont])
        else:
            cont = cont + 1
        t = 0
        for c in S:
            t = t+1
    return S

def remove_complements(S,l):
    t = 0
    l = l*(-1)
    for clausula in S:
        t = 0
        for elemento in clausula:
            if elemento == l:
                del(clausula[t])
            t = t+1
    return S
