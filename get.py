import urllib2
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
import argparse

"""Fetch all daringfireball articles since 2002

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
            'text',
            'chars',
            'title',
            'url',
        )
    )

    for year in range(2002, 2017):
        print str(year)
        soup = BeautifulSoup(
            urllib2.urlopen("http://daringfireball.net/" + str(year)).read(),
            "html.parser"
        )

        archive = soup.find("div", class_="archive")
        p = archive.find_all("p")
        for item in p:
            link = item.find("a", href=True)

            # look for url in soup
            url = link['href']

            # look for title in soup
            title = link.string.encode('ascii', 'ignore')

            # look for date in soup
            date = item.find("small")

            # get native time object
            date = datetime.strptime(
                date.string.encode('ascii', 'ignore'), "%d%b%Y"
            )

            artcl_soup = BeautifulSoup(
                urllib2.urlopen(url).read(),
                "html.parser"
            )

            text = artcl_soup.find("div", class_="article")

            text_sans_quotes = []

            for p in text.find_all("p"):
                # add ascii text if not a quote
                if p.parent.name != 'blockquote':
                    text_sans_quotes.append(
                        p.getText().encode('ascii', 'ignore')
                    )

            print "Number of Characters: %d" % len(text_sans_quotes)
            print date
            print url
            print title

            s = pd.Series({
                'date': date,
                'text': text_sans_quotes,
                'chars': len(text_sans_quotes),
                'title': title,
                'url': url,
            })

            df = df.append(s, ignore_index=True)

    # make date object the index
    df = df.set_index('date')
    df.to_pickle(args.output)
