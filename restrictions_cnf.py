from xml.dom.minidom import Attr

def restriction1(rules_num, attributes):

    and_list = []
    for rule in range(0, rules_num):
        lista_somentes = []
        for attr in range(0, len(attributes)-1):
            """
            (A∧¬B∧¬C) ∨ (¬A∧B∧¬C) ∨ (¬A∧¬B∧C) in CNF is: 
            (¬A ∨ ¬B) ∧ (¬A ∨ ¬C) ∧ (B ∨ ¬C ∨ ¬A) ∧ (¬C ∨ A ∨ ¬B) ∧ (¬C ∨ ¬B) ∧ (B ∨ A ∨ C)

            3*Res + 3*TAM_Res*Reg + 1 - p
            3*Res + Reg + 2 - p
            3*Res + Reg + 3 - p

            """
            somente_um_interno = []
            somente_um_interno.append(int(-1*( (3*attr)  +     (3*(len(attributes)-1)*rule)    +   1    )))
            somente_um_interno.append(-1*( (3*attr)  +     (3*(len(attributes)-1)*rule)    +   2    ))
            lista_somentes.append(somente_um_interno)
            somente_um_interno = []
            somente_um_interno.append(-1*( (3*attr)  +     (3*(len(attributes)-1)*rule)    +   1    ))
            somente_um_interno.append(-1*( (3*attr)  +     (3*(len(attributes)-1)*rule)    +   3    ))
            lista_somentes.append(somente_um_interno)
            somente_um_interno = []
            somente_um_interno.append(-1*( (3*attr)  +     (3*(len(attributes)-1)*rule)    +   1    )) 
            somente_um_interno.append(( (3*attr)  +     (3*(len(attributes)-1)*rule)    +   2    ))
            somente_um_interno.append(-1*( (3*attr)  +     (3*(len(attributes)-1)*rule)    +   3   ))
            lista_somentes.append(somente_um_interno)
            somente_um_interno = []
            somente_um_interno.append(( (3*attr)  +     (3*(len(attributes)-1)*rule)    +   1    )) 
            somente_um_interno.append(-1*( (3*attr)  +     (3*(len(attributes)-1)*rule)    +   2    ))
            somente_um_interno.append(-1*( (3*attr)  +     (3*(len(attributes)-1)*rule)    +   3    ))
            lista_somentes.append(somente_um_interno)
            somente_um_interno = []
            somente_um_interno.append(-1*( (3*attr)  +     (3*(len(attributes)-1)*rule)    +   2    ))
            somente_um_interno.append(-1*( (3*attr)  +     (3*(len(attributes)-1)*rule)    +   3    ))
            lista_somentes.append(somente_um_interno)
            somente_um_interno = []
            somente_um_interno.append(( (3*attr)  +     (3*(len(attributes)-1)*rule)    +   1    ))
            somente_um_interno.append(( (3*attr)  +     (3*(len(attributes)-1)*rule)    +   2    ))
            somente_um_interno.append(( (3*attr)  +     (3*(len(attributes)-1)*rule)    +   3    ))
            lista_somentes.append(somente_um_interno)

        and_list = and_list+lista_somentes
    return(and_list)

def restriction2(rules_num, attributes):
    list_clauses = []
    for rule in range(0, rules_num):
        list_ors = []
        for attr in range(0, len(attributes) - 1):
            list_ors.append(-1* ( (3*attr)  +     (3*(len(attributes)-1)*rule)    +   3  ))
        list_clauses.append(list_ors)
    return(list_clauses)

def restriction3(rules_num, file):
    p_index = len(file[0]) - 1
    clauses_list = []
    for rule in range(0, rules_num):
        for patient in range(1, len(file)):
            patient_list = []
            if file[patient][p_index] == "0":
                for attr in range(p_index):
                    if file[patient][attr] == '1':
                        patient_list.append((3*attr)  +     ((3*p_index)*rule)    +   2  )
                    elif file[patient][attr] == '0':
                        patient_list.append((3*attr)  +    ((3*p_index)*rule)    +   1  )
                clauses_list.append(patient_list)
    return(clauses_list)

def restriction4(rules_num, file):
    max_size = ( 3* (len(file[0])-2) + 3 * (len(file[0]) - 1)*(rules_num) ) + 3
    p_index = len(file[0]) - 1
    clauses_list = []
    for rule in range(0, rules_num):
        for patient in range(1, len(file)):
            attr_list_of_patient = []
            if file[patient][p_index] == '1':  
                for attr in range(p_index):
                    for_each_attr = []
                    if file[patient][attr] =='1':
                        for_each_attr.append(-1*( (3*attr)  +     ( (3*p_index) *rule)    +   2))
                        for_each_attr.append(-1*(max_size + (rules_num)*rule + patient))
                    elif file[patient][attr] =='0':
                        for_each_attr.append(-1*((3*attr)  +     ((3*p_index)*rule)    +   1))
                        for_each_attr.append(-1*(max_size + (rules_num)*rule + patient))     
                    attr_list_of_patient.append(for_each_attr)
            clauses_list = clauses_list + attr_list_of_patient
    return(clauses_list)  

def restriction5(rules_num, file):
    max_size = ( 3* (len(file[0])-2) + 3 * (len(file[0]) - 1)*rules_num ) + 3
    p_index = len(file[0]) - 1
    clauses = []
    for patient in range(1, len(file)):
        for_patient = []
        if file[patient][p_index] == '1':
            for rule in range(0, rules_num):
                for_patient.append((max_size + (rules_num)*rule + patient))
            clauses.append(for_patient)
    return(clauses)
        