def write_txt(file, file_name, variables, clauses, rules_num, format):
    with open('CNF/' + file_name + '-' + str(rules_num) + 'rules' + format, 'w') as arquivo:
        arquivo.write('c' + '     ' + file_name + '\n')
        arquivo.write('c' + '     ' + '---------EQUIPE--------' + '\n')
        arquivo.write('c' + '     ' + 'Carlos Eduardo Freitas' + '\n')
        arquivo.write('c' + '     ' + 'Lucas de Carvalho' + '\n')
        arquivo.write('c' + '     ' + '--------DISCPLINA------' + '\n')
        arquivo.write('c' + '     ' + 'Logica Para Computacao' + '\n')
        arquivo.write('c' + '     ' + 'Professor Thiago Alves' + '\n')
        arquivo.write('c' + '     ' + '2021.2' + '\n')
        arquivo.write('c' + '     ' + '----------------------' + '\n')
        arquivo.write('p cnf ' + str(variables) + ' ' +  str(clauses) + '\n')
        for clause in file:
            for atom in clause:
                arquivo.write(str(atom))
                arquivo.write(' ')
            arquivo.write('0\n')