from os import listdir
from os.path import isfile, join
from csv_manipulations import *
import signal
from contextlib import contextmanager
from restrictions import bf_create_restrictions
from my_dictionary import create_dictionary, print_solution_translated
from restrictions_cnf import *
from semantics import *

from pysat.solvers import Glucose3
from pysat.formula import CNF

from DPLL import DPLL
import matplotlib as plt
import sys
import time

class TimeoutException(Exception): pass

@contextmanager
def time_limit(seconds):
    def signal_handler(signum, frame):
        raise TimeoutException("Timed out!")
    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)

inputs = []
dpll_runtimes = []
bf_runtimes = []
pysat_runtimes = []

path = '/content/drive/MyDrive/LogComp/pacientes'
files = [f for f in listdir(path) if isfile(join(path, f))]

for p in files:
    file_name = p.replace(".csv", "")
    inputs.append(file_name.replace("column_bin_", ""))
    my_file = open_csv(file_name)
    rules_num = 2

    restrictions_in_cnf = cnf_create_restrictions(file_name, my_file, rules_num)
    restrictions_to_bf = bf_create_restrictions(my_file, rules_num)

    init = time.time()
    dpll_solved = DPLL(restrictions_in_cnf)
    end = time.time()
    dpll_runtimes.append(end-init)

    init = time.time()
    try:
        with time_limit(300):
            satisfiability_brute_force(restrictions_to_bf)
    except TimeoutException as e:
        print("Timed out!")
    end = time.time()
    bf_runtimes.append(end-init)

    formula = CNF(from_file = str("/content/drive/MyDrive/LogComp/CNF/" + file_name + "-2rules.cnf"))
    g = Glucose3()
    g.append_formula(formula)
    g.solve()

    init = time.time()
    pysat_solved = g.get_model()
    end = time.time()
    pysat_runtimes.append(end-init)

