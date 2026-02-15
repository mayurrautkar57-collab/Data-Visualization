import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set()
ticker =pd.read_csv('test.csv')
ticker.head()
ticker.info()
sns.distplot(ticker['High'])