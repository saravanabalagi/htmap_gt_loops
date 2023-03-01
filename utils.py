## Utility functions
import itertools
import pandas as pd


# minify a long list of indices
# eg: [1,2,3,4,5,10,11,12] -> "1:5;10:12"
def list_minify(l: list, range_sep=':', list_sep=";"):
    list_of_lists = (list(x) for _, x in itertools.groupby(l, lambda x, c=itertools.count(): next(c)-x))
    return list_sep.join(range_sep.join(map(str, [l[0], l[-1]][:len(l)])) for l in list_of_lists)


# expand string to list
# eg: flatten true: "1:5;10:12" -> [1,2,3,4,5,10,11,12]
# eg: flatten false: "1:5;10:12" -> [[1,2,3,4,5], [10,11,12]]
def list_unminify(txt: str, flatten=False):
    l = []
    if pd.isna(txt): return l
    for r in txt.split(';'):
        e = [int(e) for e in r.split(':')]
        l_row = list(range(e[0], e[-1]+1))
        if flatten: 
            l.extend(l_row)
        else: 
            l.append(l_row)
    return l


# read loops csv file
# loops_file: path to csv file
def read_loops_csv(loops_file):
    loops_gt = pd.read_csv(loops_file, comment='#')
    loops_gt.loops = loops_gt.loops.apply(lambda x: list_unminify(x, flatten=True))
    return loops_gt
