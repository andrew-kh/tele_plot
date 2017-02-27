#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 19:56:02 2017

@author: andrew
"""

import matplotlib
import matplotlib.style
matplotlib.style.use('ggplot')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from plot_functions import plt_data, data_extr, get_lims, align_lbls, getcompany, getcurrency

def plot_LTM(ticker):
    
    """creates a plot for the specified ticker (last 12 months of data from yahoo)
    
    Arguments:
    ticker -- the ticker of the stock
    """
    
    #create dataframe with stock prices and get necessary info  
    plotdata,s_date,e_date = plt_data(ticker) #get pd data series of ticker, its start and end dates
    min_price_date, min_price, max_price_date, max_price = data_extr(plotdata) #get maximum and minimum prices and their dates
    max_num = plotdata.index.get_loc(max_price_date)
    min_num = plotdata.index.get_loc(min_price_date)
    
    #create variables for x axis formatting
    # months = mdates.MonthLocator()  # every month
    ax_major_fmt = mdates.DateFormatter("%b'%y ")
    
    #create plot and add time series
    fig, ax = plt.subplots()
    fig.set_size_inches(8.33,6.25)
    
    ax.plot(plotdata.index, plotdata, lw = 2, marker = 'o', markevery = [max_num, min_num], zorder = 3) #plot stock price
    ax.axhline(max_price, color="#2B0756", linestyle='--', lw = 1.2, zorder = 1) #max dotted line
    ax.axhline(min_price, color="#2B0756", linestyle='--', lw = 1.2, zorder = 1) #min dotted line
    
    #format plot
    ax.xaxis.set_major_formatter(ax_major_fmt)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    
    max_offset = align_lbls(plotdata, max_price_date) #determine required offset if necessary 
    min_offset = align_lbls(plotdata, min_price_date) #determine required offset if necessary 
    
    lbl_max = ax.annotate(round(max_price,1), xy = (max_price_date, max_price),fontweight = 'bold', ha = 'center', xytext=(max_offset,5), textcoords="offset points") # add text label to max price
    lbl_min = ax.annotate(round(min_price,1), xy = (min_price_date, min_price),fontweight = 'bold', ha = 'center', xytext=(min_offset,-15), textcoords="offset points") # add text label to max price
    
    lbl_max.set_alpha(.5) #transparency
    lbl_min.set_alpha(.5)
    
    ymin, ymax = get_lims(ax)
    ax.set_ylim([ymin,ymax])
    
    datemin = s_date #can be killed
    datemax = e_date #can be killed
    ax.set_xlim(datemin, datemax) #can be killed
    
    c_name = getcompany(ticker)
               
    fig.autofmt_xdate(rotation = 30) 
    fig.suptitle(c_name)
    
    c_currency = getcurrency(ticker)
    
    plt.ylabel('Share Price'+c_currency)
    plt.show()
