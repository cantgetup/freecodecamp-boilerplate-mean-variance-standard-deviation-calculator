import numpy as np

def calculate(list_num):
    
    if len(list_num) != 9:
        raise ValueError('List must contain nine numbers.')
    
    a = np.reshape(list_num, (3,3))

    calculations = {}

    calculations['mean'] = [list(np.mean(a, axis=0)), list(np.mean(a, axis=1)), np.mean(a)]

    calculations['variance'] = [list(np.var(a, axis=0)), list(np.var(a, axis=1)), np.var(a)]

    calculations['standard deviation'] = [list(np.std(a, axis=0)), list(np.std(a, axis=1)), np.std(a)]

    calculations['max'] = [list(np.max(a, axis=0)), list(np.max(a, axis=1)), np.max(a)]

    calculations['min'] = [list(np.min(a, axis=0)), list(np.min(a, axis=1)), np.min(a)]

    calculations['sum'] = [list(np.sum(a, axis=0)), list(np.sum(a, axis=1)), np.sum(a)]

    return calculations
