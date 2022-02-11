from csv_manipulations import *
from restrictions_cnf import *
from semantics import *
import sys
from txt_manipulations import write_txt
from my_dictionary import create_dictionary, print_solution_translated

my_file = open_csv(sys.argv[1])
rules_num = int(sys.argv[2])

withPatologyCounter = 0
for patient in my_file:
    if(patient[len(patient)-1]) == "1":
        withPatologyCounter+=1

attributes = my_file[0]
max_size = ( 3* (len(my_file[0])-2) + 3 * (len(my_file[0]) - 1)*(rules_num - 1)) + 3 + withPatologyCounter * rules_num

all_restrictions = restriction1(rules_num, attributes) + restriction2(rules_num, attributes) + restriction3(rules_num, my_file) + restriction4(rules_num, my_file) + restriction5(rules_num, my_file)
write_txt(all_restrictions, sys.argv[1], max_size, len(all_restrictions), rules_num, '.cnf')

dict = create_dictionary(rules_num, my_file)

"""for clause in restriction5(rules_num, my_file):
    for literal in clause:
        if literal > 0:
            print(dict[literal])
        else:
            print("~" + dict[literal*-1])
    print("AND")"""



