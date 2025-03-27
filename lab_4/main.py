import pandas as pd
import numpy as np
import time

def do_test(count: int):
    df1 = pd.DataFrame({'weight': np.random.random(count)})

    start_time = time.perf_counter()

    max_id = df1['weight'].idxmax()

    end_time = time.perf_counter()
    internal_func_time = end_time - start_time

    start_time = time.perf_counter()

    max_arg_id = 0
    row = df1['weight']
    for i in range(1, len(row)):
        if row[i] > row[max_arg_id]:
            max_arg_id = i

    end_time = time.perf_counter()
    external_func_time = end_time - start_time

    print('Вбудована функція на ', count, ' кількості: ', internal_func_time)
    print('Наша функція на ', count, ' кількості: ', external_func_time)


do_test(100)
do_test(1_000_000)