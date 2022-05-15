import sys
import utils
if __name__ == "__main__":

    args = sys.argv[1:]

    for code in args:
        conv = utils.currency_rates(code)
        if conv:
            cur, date = conv
            date = date.strftime("%d-%m-%Y")
            print(f"{cur}, {date}")