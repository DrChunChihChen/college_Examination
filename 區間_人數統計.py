import numpy as np
import pandas as pd


df = pd.read_excel("化學系化學生物組(B組).xlsx")

bins = np.arange(0,400,3)
bins2 = np.arange(3.01,400,3)
bins3 = np.insert(bins2,0,0)

bins4 = np.concatenate((bins, bins3))

list1 = bins.tolist()
list2 = bins3.tolist()
result = [None]*(len(list1)+len(list2))
result[::2] = list1
result[1::2] = list2
result
del result[0]

bin_final = np.array(result)
labels = ['-'.join(map(str,(x,y))) for x, y in zip(bin_final[:-1], bin_final[1:])]
df['bins'] = pd.cut(df['總分'], bins = bin_final, labels=labels)

pd.crosstab(index=df['bins'], columns='count')