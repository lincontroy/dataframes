import numpy as np
import pandas as pd

# df = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('CS56'))



# Create a DataFrame object
df = pd.DataFrame(np.random.randint(30,100,size=(3, 11)),
                  index=['CS 5000', 'CS 5110', 'CS 5600'],
                  columns=['Alice', 'Mark', 'Bill', 'Tony', 'Jason', 'Ravi','Sandeep','Mounika','John','Curtis','Denis'])



df['average'] = df.mean(axis=1)



print(df)
