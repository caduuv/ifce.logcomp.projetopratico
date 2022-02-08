def restriction1(rules_num, attributes):
    and_list = []
    for rule in range(1, rules_num+1):
        lista_somentes = []
        for attr in range(len(attributes)-1):
            somente_um_interno = []
            somente_um_interno.append('~X_' + str(attributes[attr]) + '_' + str(rule) + '_p')
            somente_um_interno.append('~X_' + str(attributes[attr]) + '_' + str(rule) + '_n')
            lista_somentes.append(somente_um_interno)
            somente_um_interno = []
            somente_um_interno.append('~X_' + str(attributes[attr]) + '_' + str(rule) + '_p')
            somente_um_interno.append('~X_' + str(attributes[attr]) + '_' + str(rule) + '_s')
            lista_somentes.append(somente_um_interno)
            somente_um_interno = []
            somente_um_interno.append('~X_' + str(attributes[attr]) + '_' + str(rule) + '_p') 
            somente_um_interno.append('X_' + str(attributes[attr]) + '_' + str(rule) + '_n')
            somente_um_interno.append('~X_' + str(attributes[attr]) + '_' + str(rule) + '_s')
            lista_somentes.append(somente_um_interno)
            somente_um_interno = []
            somente_um_interno.append('X_' + str(attributes[attr]) + '_' + str(rule) + '_p') 
            somente_um_interno.append('~X_' + str(attributes[attr]) + '_' + str(rule) + '_n')
            somente_um_interno.append('~X_' + str(attributes[attr]) + '_' + str(rule) + '_s')
            lista_somentes.append(somente_um_interno)
            somente_um_interno = []
            somente_um_interno.append('~X_' + str(attributes[attr]) + '_' + str(rule) + '_n')
            somente_um_interno.append('~X_' + str(attributes[attr]) + '_' + str(rule) + '_s')
            lista_somentes.append(somente_um_interno)
            somente_um_interno = []
            somente_um_interno.append('X_' + str(attributes[attr]) + '_' + str(rule) + '_p')
            somente_um_interno.append('X_' + str(attributes[attr]) + '_' + str(rule) + '_n')
            somente_um_interno.append('X_' + str(attributes[attr]) + '_' + str(rule) + '_s')
            lista_somentes.append(somente_um_interno)
        and_list = and_list+lista_somentes
    print(and_list)
