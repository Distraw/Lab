import pandas as pd
import numpy as np


index = ["first", "second", "third"]
data = [1, 2, 3]
series = pd.Series(data, index = index)
print(series)

index = ["first", "second", "third"]
data = np.zeros(3)
series = pd.Series(data, index = index)
print(series)

index = ["first", "second", "third"]
data = ["first", 3, 2.05]
series = pd.Series(data, index = index)
print(series)

index = ["first", "second", "third"]
data = {"first" : 3, "second" : 2, "third" : 1}
series = pd.Series(data, index = index)
print(series)

index = ["first", "second", "third"]
data = ["1", "2", "3"]
series = pd.Series(data, index = index)
print(series)

###########################################################

print(series.loc["first"])
print(series.iloc[0])

series = pd.Series([1, 2, 3, 4, 5, 5], index = ["first", "second", "third", "fourth", "fifth", "sixth"])
even_series = series[series % 2 == 0]
print(even_series)

even_series = series.drop("second")
print(even_series)
print(series.value_counts())