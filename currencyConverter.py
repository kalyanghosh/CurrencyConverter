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
baseURL="https://v3.exchangerate-api.com/bulk"
yourAPIKey="a829f18d02e0e79bb9342658"
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

URL=baseURL+"/"+yourAPIKey+"/"+(input_curr_type.upper())


#2. Getting real-time rates 
def getRealTimeRates(URL):
    
    # Making our request
    response = requests.get(URL)
    data = response.json()
    return data

def parseJSON(data):
    TIMESTAMP=data["timestamp"]
    FROM=data["from"]
    RESULT=data["result"]
    RATES=(data["rates"])
    for curr_type in output_curr_types:
        for r in RATES:
            if(r==curr_type):
                conversion_rate=float(RATES[r])
                print (conversion_rate*input_curr_val)
            
    
    

data=getRealTimeRates(URL)
parseJSON(data)
