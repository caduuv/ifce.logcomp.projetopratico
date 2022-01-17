from operator import and_
from formula import *

def and_all(list_formulas):
    """Realiza um And com a lista de fórmulas"""
    first_formula = list_formulas[0]
    del list_formulas[0]
    for formula in list_formulas:
        first_formula = And(first_formula, formula)
    return first_formula

def or_all(list_formulas):
    """Realiza um And com a lista de fórmulas"""
    first_formula = list_formulas[0]
    del list_formulas[0]
    for formula in list_formulas:
        first_formula = Or(first_formula, formula)
    return first_formula

def first_restriction(rules_num, attributes):

    """Para cada atributo e cada regra, temos exatamente uma das três possibilidades: o atributo aparece
positivamente na regra, o atributo aparece negativamente na regra ou o atributo n ̃ao aparece na regra."""

    formulas = []
    for rule in range(1, rules_num+1):
        three_possibilities_list = []

        for attr in range(len(attributes)-1):
            three_possibilities_list.append(
                Or(
                    Or(
                        And(
                            And(Atom('X_' + str(attributes[attr]) + '_' + str(rule) + '_p'), Not(Atom('X_' + str(attributes[attr]) + '_' + str(rule) + '_n'))),
                            Not(Atom('X_' + str(attributes[attr]) + '_' + str(rule) + '_s'))
                        ),
                        And(
                            And(Not(Atom('X_' + str(attributes[attr]) + '_' + str(rule) + '_p')), Atom('X_' + str(attributes[attr]) + '_' + str(rule) + '_n')),
                            Not(Atom('X_' + str(attributes[attr]) + '_' + str(rule) + '_s'))
                        )
                    ),
                    And(
                            And(Not(Atom('X_' + str(attributes[attr]) + '_' + str(rule) + '_p')), Not(Atom('X_' + str(attributes[attr]) + '_' + str(rule) + '_n'))),
                            Atom('X_' + str(attributes[attr]) + '_' + str(rule) + '_s')
                    )
                )
            )
        tpl_and = and_all(three_possibilities_list)
        """tpl -> three possibilities list"""
        formulas.append(tpl_and)
    

    return and_all(formulas)

def second_restriction(rules_num, attributes):
    inner_list = []
    for rule in range(1, rules_num + 1):
        variable_formula = 0
        for attr in range(len(attributes) - 2):
            if attr == 0:
                variable_formula = Not(Atom('X_' + str(attributes[0]) + '_' + str(rule) + '_s'))
            variable_formula = Or(variable_formula, Not(Atom('X_' + str(attributes[attr+1]) + '_' + str(rule) + '_s')))
        inner_list.append(variable_formula)
    return(and_all(inner_list))

def third_restriction(rules_num, file):
    p_index = len(file[0]) - 1
    patients_restrictions = []
    for rule in range(1, rules_num + 1):
        singular_patient_restriction = []
        for patient in range(1, len(file)):
            if file[patient][p_index] == '0':
                for index in range(p_index):
                    if file[patient][index] == '1':
                        singular_patient_restriction.append(Atom('X_' + str(file[0][index]) + '_' + str(rule) + '_n'))
                    elif file[patient][index] == '0':
                        singular_patient_restriction.append(Atom('X_' + str(file[0][index]) + '_' + str(rule) + '_p'))
        patients_restrictions.append(or_all(singular_patient_restriction))
    return and_all(patients_restrictions)
    
def fourth_restriction(rules_num, file):
    p_index = len(file[0]) - 1
    restriction_list = []
    for rule in range(1, rules_num + 1):
        inner_list = []
        for patient in range(1, len(file)):
            if file[patient][p_index] == '1':
                implications_list = []
                for index in range(p_index):
                    if file[patient][index] =='1':
                        implications_list.append(
                            Implies(
                                Atom('X_' + str(file[0][index]) + '_' + str(rule) + '_n'),
                                Not(Atom('C_' + str(rule) + '_' + str(patient)))
                                )
                        )
                    elif file[patient][index] =='0':
                        implications_list.append(
                            Implies(
                                Atom('X_' + str(file[0][index]) + '_' + str(rule) + '_p'),
                                Not(Atom('C_' + str(rule) + '_' + str(patient)))
                                )
                        )
                inner_list.append(and_all(implications_list))
        restriction_list.append(and_all(inner_list))

    return and_all(restriction_list)

def fifth_restriction(rules_num, file):
    p_index = len(file[0]) - 1
    inner_list = []
    for patient in range(1, len(file)):
        patient_or_list = []
        if file[patient][p_index] == '1':
            for rule in range(1, rules_num + 1):
                patient_or_list.append(Atom('C_' + str(rule) + '_' + str(patient)))
            inner_list.append(or_all(patient_or_list))
    return(and_all(inner_list))
                