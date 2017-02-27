#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 20:03:33 2017

@author: andrew
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 22:23:40 2016

@author: andrew
"""

from pandas_datareader import data
from dateutil.relativedelta import relativedelta
import datetime
from config import tickers
import pandas as pd

def plt_data(ticker):
    """returns pd series object, its start and end dates.

    Arguments:
    ticker -- the ticker of the stock
    """
    plotdata = data.get_data_yahoo(ticker, datetime.date.today() - relativedelta(months = 12))['Adj Close'] # create pandas time series object
    start_date = plotdata.index[0].date() # get the first entry timestamp (pands format) and turn in into datetime date
    end_date = plotdata.index[plotdata.count()-1].date() # get the last entry timestamp (pands format) and turn in into datetime date
    return plotdata, start_date, end_date
    
def data_extr(pd_series):
    """returns maximum and minimum values and dates in pd data series

    Arguments:
    pd_series -- pandas data series
    """
    
    min_price_date = pd_series.idxmin(axis = 1) # return date of min value
    min_price = pd_series.loc[min_price_date] # return min value   
    max_price_date = pd_series.idxmax(axis = 1) # return date of max value
    max_price = pd_series.loc[max_price_date] # return max value

    
    return min_price_date, min_price, max_price_date, max_price
    
def get_lims(ax):
    """returns y axis limits, tick value stays the same

    Arguments:
    ax - matplotlib ax object
    """
    y_ax_ticks = ax.get_yticks().tolist() #tuple of y axis limits
    y_ax_value = y_ax_ticks[1]-y_ax_ticks[0] #value of an interval of the y axis
    min_val = ax.yaxis.get_data_interval()[0]  
    max_val = ax.yaxis.get_data_interval()[1]
    
    #create new limits to maintain constant "space" for all charts
    ymin_new = min_val - y_ax_value/2. 
    ymax_new = max_val + y_ax_value/2. 
    
    return ymin_new, ymax_new
    
def align_lbls(data, extr_date):
    """returns horizontal offset value for minimum and maximum labels

    Arguments:
    data - pd series frame with stock prices
    extr_date - date (timestamp) of max or min price
    """
    
    #derive x axis limits from dataframe
    start_date = data.index[0].date()
    end_date = data.index[len(data)-1].date()
    #get date of max or min price and the length of label
    date_extr = extr_date.date()
    lbl_len = len(str(round(data.loc[date_extr],1)))

    #offset label if it is too close to one of the axis:
    #it takes into account to which side of x axis the label is too close
    #and the label's length
    if (date_extr - start_date).days <= 12:
        if lbl_len == 3:
            offset_val = 10
        elif lbl_len == 4:
            offset_val = 15
        elif lbl_len == 5:
            offset_val = 20
        else:
            offset_val = 25
    elif (end_date - date_extr).days <= 12:
        if lbl_len == 3:
            offset_val = -10
        elif lbl_len == 4:
            offset_val = -15
        elif lbl_len == 5:
            offset_val = -20
        else:
            offset_val = -25
    else:
        offset_val = 0
        
    return offset_val

        
def getcompany(ticker):
    """Returns the full name of the company 
    that corresponds with the provided ticker
    Args:
        ticker(string): initial query from bot
    """

    
    #create pandas object
    ref = pd.read_csv(tickers, sep = ";", header = 0)
    
    #get company name
    try:
        company = ref.loc[ref['Ticker'] == ticker]
        company_n = company['Name']
        companyname = company_n.iloc[0]
    except:
        companyname = ticker
    return companyname

def getcurrency(ticker):
    """Returns currency in which the symbol is traded 
    Args:
        ticker(string): initial query from bot
    """

    
    #create pandas object
    ref = pd.read_csv(tickers, sep = ";", header = 0)
    
    #get currency
    try:
        currency = ref.loc[ref['Ticker'] == ticker]
        currency_n = currency['Currency']
        currency_n = ', ' + currency_n.iloc[0]
    except:
        currency_n = ''
    return currency_n

def checkticker(ticker):
    """Checks if ticker exists in db.  
    Args:
        ticker(string): initial query from bot
    """

    #used in bot module
    
    #create pandas object
    ref = pd.read_csv(tickers, sep = ";", header = 0)
    
    #check if df is not empty
    check = ref.loc[ref['Ticker'] == ticker]
    if check.empty:
        bCheck = False 
    else:
       bCheck = True

    return bCheck