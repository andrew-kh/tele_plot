# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 21:51:24 2017

@author: andrew
"""

import matplotlib
import matplotlib.style
matplotlib.style.use('ggplot')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from plot_functions import plt_data, data_extr, get_lims, align_lbls

def plot_LTM(ticker):
    
    #create dataframe to plot and other necessary 
    
    plotdata,s_date,e_date = plt_data(ticker) #get pd data series of ticker, its start and end dates
    min_price_date, min_price, max_price_date, max_price = data_extr(plotdata)
    max_num = plotdata.index.get_loc(max_price_date)
    min_num = plotdata.index.get_loc(min_price_date)
    
    #locators that are later used to format the date axis
    years = mdates.YearLocator()   # every year
    months = mdates.MonthLocator()  # every month
    ax_major_fmt = mdates.DateFormatter("%b'%y ")
    
    fig, ax = plt.subplots()
    
    ax.axhline(max_price, color="#2B0756", linestyle='--', lw = 1.2) #max dotted line
    ax.axhline(min_price, color="#2B0756", linestyle='--', lw = 1.2) #min dotted line
    ax.plot(plotdata.index, plotdata, lw = 2, marker = 'o', markevery = [max_num, min_num]) #plot stock price
    
    ax.xaxis.set_major_locator(months)
    ax.xaxis.set_major_formatter(ax_major_fmt)
    
    max_offset = align_lbls(plotdata, max_price_date)
    min_offset = align_lbls(plotdata, min_price_date)
    
    lbl_max = ax.annotate(round(max_price,1), xy = (max_price_date, max_price),fontweight = 'bold', ha = 'center', xytext=(max_offset,5), textcoords="offset points")
    lbl_min = ax.annotate(round(min_price,1), xy = (min_price_date, min_price),fontweight = 'bold', ha = 'center', xytext=(min_offset,-15), textcoords="offset points")
    
    lbl_max.set_alpha(.5)
    lbl_min.set_alpha(.5)
    
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    
    datemin = s_date
    datemax = e_date
    ax.set_xlim(datemin, datemax)
    
    fig.autofmt_xdate(rotation = 30)
    fig.suptitle(ticker)
    
    plt.ylabel('Share Price')
    
    ymin, ymax = get_lims(ax)
    
    ax.set_ylim([ymin,ymax])
    
    plt.show()