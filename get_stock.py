from datetime import datetime
import pandas as pd
import argparse

"""Fetch apple stock

    count the article character length
"""

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description='Fetch all daringfireball articles since 2002'
    )

    parser.add_argument('output')
    args = parser.parse_args()

    df = pd.DataFrame(
        columns=(
            'date',
            'close',
        )
    )

    from yahoo_finance import Share

    apple_stock = Share('AAPL')
    stock_data = apple_stock.get_historical('2002-01-01', '2017-01-01')

    for entry in stock_data:
        # get native time object
        date = datetime.strptime(entry['Date'], "%Y-%m-%d")
        s = pd.Series({
            'date': date,
            'close': float(entry['Close'])
        })

        df = df.append(s, ignore_index=True)

    df = df.set_index('date')
    df.to_pickle(args.output)
