DESCRIPTION:
This project is a part of my telegram bot that creates a stock plot for the last 12 months of a given ticker.

The project consists of 4 files:

1) plot_main.py - function that creates the plot that is lated sent by the bot (just replace plt.show() with fig.savefig with dpi = 120).

2) plot_functions.py - a set of support functions that generate data and format the plot: adjust Y axis, offset minimum and maximum labels. Company and currency lookup by ticker is also performed by these functions.

3) config.py - file with the bot’s unique token and a path to the .csv file with tickers, company names and currency

4) tickers.csv - database of traded stocks on major exchanges. Sources: 
www.nyse.com/
www.eoddata.com
www.moex.com

HOW TO LAUNCH THE CODE:
1) Place files 1-3 in the same folder
2) In file 3 set the ticker variable to the path of the file 4 like this:
tickers = '/Users/usrname/Desktop/Bot/db/tickers.csv'
3) Launch the function in file 1
4) call example: plot_LTM(‘C’)

