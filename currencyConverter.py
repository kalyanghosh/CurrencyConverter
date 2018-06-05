# -*- coding: utf-8 -*-
"""
Created on Sat Jun 02 09:48:19 2018

@author: Kalyan
"""

###############################################################################

##################  REAL TIME CURRENCY CONVERTOR ##############################

###############################################################################


import requests
import cgi
import os
import urllib
import json
from collections import namedtuple
import time
baseURL="http://apilayer.net/api/"
yourAPIKey="9481be930c0a6e0c5129c1c03b632cd3"
baseCurrency=""



#1. Getting inputs from the user
#2. Assumptions:
#2.1 Input Base Currency is United States Dollars (USD)
#2.2 The user provides the currency type in ISO 4217 Three Letter Currency Codes
#    i.e USD for United States Dollars  

print ("WELCOME TO THE CURRENCY CONVERTER APP \n");
print ("ENTER THE INPUT CURRENCY TYPE AND AMOUNT SEPARATED BY SPACES: \n");
input_args=raw_input();
input_values=input_args.split(" ");
input_curr_type=str(input_values[0]);
input_curr_val=float(input_values[1]);
print ("ENTER THE DESIRED OUTPUT CURRENCY TYPES SEPARATED BY SPACES: \n");
output_args=raw_input();
output_curr_types=output_args.split(" ");
maxHistory=4
history=[]



#2. Getting real-time rates 
def getLiveRates():
    liveRatesURL=baseURL+'live' 
    currencies= ','.join(output_curr_types) 
    params={'access_key': yourAPIKey, 'currencies': currencies, 'format': 1}
    r = requests.get(liveRatesURL, params = params)
    livequote=r.json()  
    SOURCE=livequote["source"]
    STATUS=livequote["success"]
    TIMESTAMP=livequote["timestamp"]
    LASTCHANGED=time.ctime(TIMESTAMP)
    QUOTES=livequote["quotes"]
    
    for r in QUOTES:
        transactions=[]
        source_target=str(r)
        rate=QUOTES[r]
        amount=input_curr_val*rate
        str1="SourceTarget: "+source_target
        str2="Rate: "+str(rate)
        str3="InputAmount: "+str(input_curr_val)
        str4="OutputAmount: "+str(amount)
        str5="LastChanged: "+str(LASTCHANGED)
        transactions.append(str1)
        transactions.append(str2)
        transactions.append(str3)
        transactions.append(str4)
        transactions.append(str5)
        history.append(transactions)
    
    print (history)
    
    
    
    
    
def getHistorical():
    
    for h in range(0,maxHistory):
        print ("*"*32)
        print (history[h])
    
    
    '''
    historicalURL=baseURL+'historical'
    currentdate='2018-06-03'
    currencies= ','.join(output_curr_types) 
    params={'access_key': yourAPIKey, 'date': currentdate, 'currencies': currencies, 'format': 1}
    r = requests.get(historicalURL, params = params)
    historicalquote=r.json()
    TIMESTAMP=historicalquote["timestamp"]
    LASTCHANGED=time.ctime(TIMESTAMP)
    FROM=historicalquote["source"]
    RESULT=historicalquote["quotes"]
    '''
  
    
    
    

getLiveRates()
getHistorical()




