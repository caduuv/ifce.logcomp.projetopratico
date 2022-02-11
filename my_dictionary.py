def create_dictionary(rules_num, file):
    max_size = ( 3* (len(file[0])-2) + 3 * (len(file[0]) - 1)*(rules_num - 1)) + 3
    num_attr = (len(file[0])) - 1
    dict = {}
    for rule in range(0, rules_num):
        for attr in range(0, num_attr):
            dict[((3*attr)  +     ((3*num_attr)*(rule))) + 1] = str('X_' + str(file[0][attr]) + '_' + str(rule+1) + '_p')
            dict[((3*attr)  +     ((3*num_attr)*(rule))) + 2] = str('X_' + str(file[0][attr]) + '_' + str(rule+1) + '_n')
            dict[((3*attr)  +     ((3*num_attr)*(rule))) + 3] = str('X_' + str(file[0][attr]) + '_' + str(rule+1) + '_s')
    for rule in range(0, rules_num):
        for patient in range(1, len(file)):
            for attr in range(0, num_attr):
                if file[patient][num_attr] == "1":
                    dict[(max_size + (rules_num)*(rule) + patient)] = str('C_' + str(rule+1) + '_' + str(patient))
    return(dict)

def print_solution_translated(dict, solved):
    resolution = []
    for literal in solved:
        if literal > 0:
            resolution.append("(" + dict[literal] + ", T)")
        else:
            resolution.append("(" + dict[literal*-1]+ ", F)")
    print(resolution)


