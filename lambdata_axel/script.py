import pandas as pd
from lambdata_axel.ds_tools import DSDataFrame

data = {'numbers': [0, 1, 2, 3, 4, 5, 6, 7],
        "alphabet": ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']}
df = DSDataFrame(data)

df.check_nulls()

train, val, test = df.train_val_test_split(random_state=24)
print(train)
print(val)
print(test)
