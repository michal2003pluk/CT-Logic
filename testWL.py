from vsdc48 import dpll_sat_solve, check_truth_assignment
import timeit
import sys

def load_dimacs(filepath):
    # Open file and read lines
    file = open(filepath, 'r')
    lines = file.readlines()
    
    clauses = []
    for line in lines:
        if line[0] == '%':
            break
        if line[0] not in ('c', 'p'):
            clauses.append([int(literal) for literal in line.split() if literal != '0'])
    return clauses

def uf20():
    print("uf20")
    for fileCount in range(1, 1001):
        fileName = f'sat_instances/uf20/uf20-0{fileCount}.cnf'
        # print(fileCount)
        sat_instance = load_dimacs(fileName)
        result = dpll_sat_solve(sat_instance)
        if not result:
            print(fileName)
            sys.exit()

def uuf50_218():
    print("uuf50-218")
    for fileCount in range(1, 1001):
        fileName = f'sat_instances/uuf50-218/uuf50-0{fileCount}.cnf'
        sat_instance = load_dimacs(fileName)
        result = dpll_sat_solve(sat_instance)
        if result:
            print(fileName)
            sys.exit()

def flat50():
    print("flat50")
    for fileCount in range(1, 1000):
        if fileCount != 73:
            fileName = f'sat_instances/flat50/flat50-{fileCount}.cnf'
            # print(fileCount)
            sat_instance = load_dimacs(fileName)
            result = dpll_sat_solve(sat_instance)
            if not result:
                print(fileName)
                sys.exit()

def CBS():
    print("CBS")
    for clauseCount in [403]:
        for backboneSize in [10, 30, 50, 70, 90]:
            print('bs', backboneSize)
            mainFileName = f'CBS_k3_n100_m{clauseCount}_b{backboneSize}'
            for (fileCount) in range(0, 1000):
                # print(fileCount)
                fileName = f'sat_instances/{mainFileName}/{mainFileName}_{fileCount}.cnf'
                sat_instance = load_dimacs(fileName)
                result = dpll_sat_solve(sat_instance)
                if not result:
                    print(fileName)
                    sys.exit()

def sw100():
    print("sw100")
    for p in range(0,2):
        mainFileName = f'sat_instances/sw100-8-lp{p}-c5/SW100-8-{p}/sw100'
        for (fileCount) in range(1, 101):
            if fileCount != 16:
                # print(fileCount)
                fileName = f'{mainFileName}-{fileCount}.cnf'
                sat_instance = load_dimacs(fileName)
                result = dpll_sat_solve(sat_instance)
                if not result:
                    print(fileName)
                    sys.exit()

from os import listdir

def testAll():
    fp = 'sat_instances/'
    for dir in ['blocksworld', 'ais', 'QG', 'logistics', 'f' 'flat200-479', 'gcp-large', 'bmc']:
        print(dir)
        for file in listdir(fp + dir):
            if file in ('qg1-08.cnf', 'qg2-08.cnf'):
                continue
            print(file)
            filePath = fp + dir + '/' + file
            sat_instance = load_dimacs(filePath)
            result = dpll_sat_solve(sat_instance)
            print(result)
            if result:
                print(check_truth_assignment(sat_instance, result))

# uf20()
# uuf50_218()
# flat50()
# CBS()
# sw100()

testAll()
