
import pandas as pd
import sys


def evaluate(reader, dates):

    months = reader["Date"].count()
    sum = reader["Profit/Losses"].sum()
    changeSum = reader["Profit/Losses"].diff()

    print(f"The total number of months: {months}")
    print(f"Total : ${sum}")
    print(f"Average Change : ${'{:.2f}'.format(changeSum.mean())}")
    print(f"Greatest Increase in profits was on {dates.loc[changeSum == changeSum.max()]['Date'].   values[0]}: ${'{:.0f}'.format(changeSum.max())}")
    print(f"Greatest Decrease in profits was on {dates.loc[changeSum == changeSum.min()]['Date'].values[0]}: ${'{:.0f}'.format(changeSum.min())}")


if __name__ == "__main__":
    reader = pd.read_csv(r'../PyBank/Resources/budget_data.csv', parse_dates=True)
    dates = pd.DataFrame(reader)
    evaluate(reader, dates)
    sys.stdout = open('output.txt', 'w')
    evaluate(reader, dates)
    sys.stdout.close()
