'''
Will be tested with year between 1913 and 2013.
You might find the reader() function of the csv module useful,
but you can also use the split() method of the str class.
'''
import csv
from collections import defaultdict

def f(year):
    '''
    >>> f(1914)
    In 1914, maximum inflation was: 2.0
    It was achieved in the following months: Aug
    >>> f(1922)
    In 1922, maximum inflation was: 0.6
    It was achieved in the following months: Jul, Oct, Nov, Dec
    >>> f(1995)
    In 1995, maximum inflation was: 0.4
    It was achieved in the following months: Jan, Feb
    >>> f(2013)
    In 2013, maximum inflation was: 0.82
    It was achieved in the following months: Feb
    '''
    months = 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    # Insert your code here
    # csv.DictReader
    results = defaultdict(set)
    following_months = None
    with open("cpiai.csv") as file:
        lines = file.readlines()
        max_inflation = 0.0
        for line in lines[1:]:
            if line.startswith(str(year)):
                following_month = months[int(line.strip().split()[0].split("-")[1]) - 1]
                max_inflation = max(max_inflation,float(line.strip().split()[2]))
                results[max_inflation].add(following_month)

        following_months = results[max_inflation]
        result_months = [month for month in months if month in following_months]

        print(f"In {year}, maximum inflation was: {max_inflation}")
        print(f"It was achieved in the following months: {result_months}")


if __name__ == '__main__':
    import doctest
    doctest.testmod()
