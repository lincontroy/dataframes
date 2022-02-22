import numpy as np
import pandas as pd

import random

random.seed(123456)

# Create a DataFrame object
df = pd.DataFrame(np.random.randint(30,100,size=(3, 1)),
                  index=['CS 5000', 'CS 5110', 'CS 5600'],
                  columns=[''])


print(df)