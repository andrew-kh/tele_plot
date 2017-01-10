# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 22:23:40 2016

@author: andrew
"""

from pandas_datareader import data
from dateutil.relativedelta import relativedelta
import datetime


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
    y_ax_ticks = ax.get_yticks().tolist()
    y_ax_value = y_ax_ticks[1]-y_ax_ticks[0]
    min_val = ax.yaxis.get_data_interval()[0]
    max_val = ax.yaxis.get_data_interval()[1]
    
    ymin_new = min_val - y_ax_value/2.
    ymax_new = max_val + y_ax_value/2. 
    
    return ymin_new, ymax_new
    
def align_lbls(data, lbl_date):
    """returns horizontal offset value for minimum and maximum labels

    Arguments:
    data - pd series frame with stock prices
    lbl - label
    """
    start_date = data.index[0].date()
    end_date = data.index[len(data)-1].date()
    lbl_date = lbl_date.date()
    lbl_len = len(str(round(data.loc[lbl_date],1)))

    if (lbl_date - start_date).days <= 12:
        if lbl_len == 3:
            offset_val = 10
        elif lbl_len == 4:
            offset_val = 15
        elif lbl_len == 5:
            offset_val = 20
        else:
            offset_val = 25
    elif (end_date - lbl_date).days <= 12:
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
    
