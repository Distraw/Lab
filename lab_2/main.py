from warnings import catch_warnings

import numpy_operations as npo

while True:
    try:
        arr = npo.inputarray()
        break
    except ValueError:
        print(ValueError)

occuredXtoNTimes = npo.get_elements_occuring_in_range_from_n_to_x_times(arr, 1, 5)
print(occuredXtoNTimes)