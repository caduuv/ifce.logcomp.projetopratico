from csv_manipulations import *
from restrictions_cnf import *
from semantics import *
import sys
from txt_manipulations import write_txt

my_file = open_csv(sys.argv[1])
rules_num = int(sys.argv[2])

res_len = len(restriction1(rules_num, my_file[0]))

attributes = my_file[0]
max_size = ( 3* (len(attributes)-2) + 3 * (len(attributes) - 1) ) + 3

write_txt(restriction1(rules_num, attributes), sys.argv[1], max_size, res_len)
 
