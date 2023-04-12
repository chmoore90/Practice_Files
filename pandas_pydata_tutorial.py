# intro pandas tutorial found at: https://pandas.pydata.org/docs/user_guide/10min.html#min

import numpy as np
import pandas as pd

### OBJECT CREATION - SERIES

# pass in a list of values, pandas creates a default integer index
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

### OBJECT CREATION - DATAFRAMES

# pass in NumPy array, with datetime index (using date_range()) and labeled columns
dates = pd.date_range("20130101", periods=6)
print(dates)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
print(df)

# pass in dictionary, to be converted to series-like structure
df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp(20130102),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)
print(df2)
print(df2.dtypes)  # internal datatypes can be different

### VIEWING DATA

print(df.head()) # returns top n rows of data
print(df.tail(3)) # returns bottom n rows of data

print(df.index) # display the index
print(df.columns) # display the columns

# converting to NumPy arrays
# NB: NumPy arrays have one dtype for the array, pandas DataFrames have one type per column.
print(df.to_numpy()) # all floats, so runs quickly
print(df2.to_numpy())
