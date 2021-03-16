import pandas as pd
import numpy as np
import glob
import os
import re

path = 'C://Users//abhis//Desktop//Reimplement-NLP4SE-1//data//pages'
os.chdir(path)

# data = pd.read_csv(path+'//ae.csv_1.csv_p.csv')
# print(data["Text_1"][1])
for file in list(glob.glob('*.csv')):
    data = pd.read_csv(file)
    result = []
    for row in data.itertuples():
        # Remove unnecessary spaces and lower case
        res = re.sub(" *{.*} *", ' ', str(row)).lower()
        res1 = re.sub(r" *\\+(n|t) *", ' ', res)  # Remove escape sequences
        res2 = re.sub(" *\\+ *", '', res1)  # Remove triple slash
        res3 = re.sub(" *===.*=== *", ' ', res2)  # Remove ==={}=== patterns
        result.append(res3)
        print(result)
    data["Text_1"] = result
    print(file+' text processing done.')
    data.to_csv(file+'_p.csv', index=False)

# Perform tokenization
