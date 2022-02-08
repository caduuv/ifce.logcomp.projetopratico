from csv_manipulations import *
from restrictions_cnf import *
from semantics import *
import sys

my_file = open_csv(sys.argv[1])
rules_num = int(sys.argv[2])

print(my_file)

restriction1(rules_num, my_file[0])
