"""The goal in this module is to define functions associated with the semantics of formulas in propositional logic. """


from formula import *
from functions import atoms


def truth_value(formula, interpretation):
    """Determines the truth value of a formula in an interpretation (valuation).
    An interpretation may be defined as dictionary. For example, {'p': True, 'q': False}.
    """
    pass
    if isinstance(formula, Atom):
        if interpretation.get(formula) == True:
            return True
    if isinstance(formula, Not):
        return not truth_value(formula.inner, interpretation.copy())
    if isinstance(formula, Or):
        return truth_value(formula.left, interpretation.copy()) or truth_value(formula.right, interpretation.copy())
    if isinstance(formula, And):
        return truth_value(formula.left, interpretation.copy()) and truth_value(formula.right, interpretation.copy())
    if isinstance(formula, Implies):
        return (not truth_value(formula.left, interpretation.copy())) or truth_value(formula.right, interpretation.copy())


def is_logical_consequence(premises, conclusion):  # function TT-Entails? in the book AIMA.
    """Returns True if the conclusion is a logical consequence of the set of premises. Otherwise, it returns False."""
    pass
    # ======== YOUR CODE HERE ========


def is_logical_equivalence(formula1, formula2):
    """Checks whether formula1 and formula2 are logically equivalent."""
    pass
    # ======== YOUR CODE HERE ========


def is_valid(formula):
    """Returns True if formula is a logically valid (tautology). Otherwise, it returns False"""
    pass
    # ======== YOUR CODE HERE ========

def sat(formula, atoms, interpretation):
    if (len(atoms) == 0):
        if truth_value(formula, interpretation):
            for x in interpretation:
                print(str(x) + ': ' + str(interpretation[x]))
            return interpretation
        else:
            return False
    else:
        atom = atoms.pop()
        interpretation1 = interpretation.copy()
        interpretation2 = interpretation.copy()
        interpretation1[atom] = True
        interpretation2[atom] = False
        result = sat(formula, atoms.copy(), interpretation1.copy())
        if result != False:
            return result
        return sat(formula, atoms.copy(), interpretation2.copy())
        
def satisfiability_pre_processing_and(formula, interpretation, list_atoms):
    if isinstance(formula.left, Atom):
            interpretation[formula.left] = True
            list_atoms.remove(formula.left)
    elif isinstance(formula.left, Not) and isinstance(formula.left.inner, Atom):
            interpretation[formula.left.inner] = False
            list_atoms.remove(formula.left.inner)
    if isinstance(formula.right, Atom):
            interpretation[formula.right] = True
            list_atoms.remove(formula.right)
    elif isinstance(formula.right, Not) and isinstance(formula.right.inner, Atom):
            interpretation[formula.right.inner] = False
            list_atoms.remove(formula.right.inner)
    if isinstance(formula.left, And):
        satisfiability_pre_processing_and(formula.left, interpretation, list_atoms)
    if isinstance(formula.right, And):
        satisfiability_pre_processing_and(formula.right, interpretation, list_atoms)

def satisfiability_pre_processing(formula, interpretation, list_atoms):
    if isinstance(formula, And):
        satisfiability_pre_processing_and(formula, interpretation, list_atoms)

def satisfiability_brute_force(formula):
    """Checks whether formula is satisfiable.
    In other words, if the input formula is satisfiable, it returns an interpretation that assigns true to the formula.
    Otherwise, it returns False."""
    pass 
    list_atoms = atoms(formula)
    interpretation = {}
    satisfiability_pre_processing(formula, interpretation, list_atoms)
    return sat(formula, list_atoms, interpretation)


    

