import numpy as np

def numpy_to_latex(arr: np.ndarray) -> str:
    if arr.ndim != 2:
        raise ValueError(f'arr has to be a 2 dimensional array, but has {arr.ndim} dimensions instead.')
    res = ''
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            res += '\\num{' + f'{arr[i, j]}' + '} & '
        res += '\\\\ \n'
    return res