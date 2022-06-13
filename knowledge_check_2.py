import pandas as pd
import seaborn as sns

df = pd.read_csv('./assets/songs_normalize.csv')

sns.scatterplot(x=df['tempo'],
                y=df['danceability'])
