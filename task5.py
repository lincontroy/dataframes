import numpy as np
import pandas as pd

# df = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('CS56'))



# Create a DataFrame object
df = pd.DataFrame(np.random.randint(30,100,size=(10, 3)),
                  columns=['CS5000', 'CS5110', 'CS5600'],
                  index=['Alice', 'Mark', 'Bill', 'Tony', 'Jason', 'Ravi','Sandeep','Mounika','John','Curtis'])

df2 = pd.DataFrame(np.random.randint(30,100,size=(1, 3)),
                  columns=['CS5000', 'CS5110', 'CS5600'],
                  index=['Denis'])


df=pd.concat([df,df2])

# df=df[['CS 5000']].sort_values(['CS 5000'], ascending=False).head(3)

values_1=[80,100]

values_2=[30,60]


filtered_df = df[df.CS5000.isin(values_1)&~df.CS5110.isin(values_2)]


print(filtered_df)






