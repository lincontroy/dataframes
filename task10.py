import numpy as np
import pandas as pd

# df = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('CS56'))



# Create a DataFrame object
df = pd.DataFrame(np.random.randint(30,100,size=(10, 3)),
                  columns=['CS 5000', 'CS 5110', 'CS 5600'],
                  index=['Alice', 'Mark', 'Bill', 'Tony', 'Jason', 'Ravi','Sandeep','Mounika','John','Curtis'])

df2 = pd.DataFrame(np.random.randint(30,100,size=(1, 3)),
                  columns=['CS 5000', 'CS 5110', 'CS 5600'],
                  index=['Denis'])


df=pd.concat([df,df2])

df['Average'] = df.mean(axis=1)



print(df)