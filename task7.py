import numpy as np
import pandas as pd

# df = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('CS56'))



# Create a DataFrame object
df = pd.DataFrame(np.random.randint(30,100,size=(2, 2)),
                  columns=['CS 5000','CS 5600'],
                  index=[ 'Ravi','Mounika'])




# filtered_df=df[['CS 5000','CS 5110','CS 5600']].sort_values(['CS 5000','CS 5110'], ascending=[True,False])


print(df)
