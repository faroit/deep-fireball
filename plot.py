import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


sns.set_style("dark")
sns.set_context("talk", font_scale=1.2)

df = pd.read_pickle('2002-2016.pandas')
stock = pd.read_pickle('apple_stock.pandas')

# Resamplte time index to business quarts
df = df.resample('BQ').count()
stock = stock.resample('BQ').mean()

fig, ax = plt.subplots(1)
ax.plot(df.index, df.chars, 'k')

ax2 = ax.twinx()
ax2.plot(stock.index, stock.close, 'b')
ax2.set_ylabel('Apple Stock in USD', color='b')
for tl in ax2.get_yticklabels():
    tl.set_color('b')

ax.set_title('Number of Articles on Daring Fireball')
ax.set_xlabel('Quarter')
ax.set_ylabel('Total Number of Articles')
plt.show()

# ax.get_yaxis().set_major_formatter(
#     ticker.FuncFormatter(lambda x, p: x/1000)
# )
