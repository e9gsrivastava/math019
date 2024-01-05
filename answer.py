'''this is find the num of Sundays'''

from datetime import date
from solver import solver

def answer():
    """
    Counts the number of Sundays that fall on the first of the month from 1901 to 2000
    """

    return solver(date(1901, 1, 1), date(2000, 12, 31))


if __name__ == "__main__":
    print(answer())
