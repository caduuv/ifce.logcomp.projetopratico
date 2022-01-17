from csv_manipulations import *
from restrictions import *
from semantics import *
import sys

my_file = open_csv(sys.argv[1])
rules_num = int(sys.argv[2])

print(my_file)

final_formula = And(
    first_restriction(rules_num, my_file[0]),
    And(
        second_restriction(rules_num, my_file[0]),
        And(
            third_restriction(rules_num, my_file),
            And(fourth_restriction(rules_num, my_file),
                fifth_restriction(rules_num, my_file)
            )
        )
    )
)
satisfiability_brute_force(final_formula)
