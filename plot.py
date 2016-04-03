import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


sns.set_style("darkgrid")
sns.set_context("talk", font_scale=1.2)
df = pd.read_pickle('2002-2016.pandas')

# Resamplte time index to business quarts
df = df.resample('BQ').sum()

get_quarterly_apple_stock(df.index.tolist())

fig, ax = plt.subplots(1)
ax.plot(df.index, df.chars, 'k')

ax.get_yaxis().set_major_formatter(
    ticker.FuncFormatter(lambda x, p: x/1000)
)

ax.set_title('DARING FIREBALL Quarterly Character Count')
ax.set_xlabel('Quarter')
ax.set_ylabel('Article Length in 1000 Characters')
plt.show()
