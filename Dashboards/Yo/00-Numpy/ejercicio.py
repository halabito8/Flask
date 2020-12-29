import numpy as np
import pandas as pd

np.random.seed(101)

arr = np.random.randint(1,101,(100,5))

print(arr)

df = pd.DataFrame(arr, columns=['f1','f2','f3','f4','label'])

print(df)

arr = np.random.randint(1,101,(50,4))

col = ['A','B','C','D']

pd.Dataframe(arr, columns=col)