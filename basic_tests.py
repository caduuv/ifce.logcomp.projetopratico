from functions import *
from formula import *
from semantics import *

my_formula = Implies(Atom('p'), Or(Atom('p'), Atom('s')))
for atom in atoms(my_formula):
        print(atom)

interpretation = {}
atom = "Teste"
interpretation1 = interpretation.copy()
interpretation1[atom] = True

print(interpretation)
print(interpretation1)

formula = Or(Atom('p'), And(Atom('q'), Not(Atom('r'))))
print(satisfiability_brute_force(formula))

    