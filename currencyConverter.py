# -*- coding: utf-8 -*-
"""
Created on Sat Jun 04 09:48:19 2018

@author: Kalyan
"""

###############################################################################

##################  REAL TIME CURRENCY CONVERTOR ##############################

###############################################################################

#Import Necessary libraries
from __future__ import print_function
import requests
import cgi
import os
import urllib
import json
import sys
from collections import namedtuple
import time

#Set Global Variables and Keys
baseURL="http://apilayer.net/api/"
yourAPIKey="9481be930c0a6e0c5129c1c03b632cd3"
baseCurrency=""
history=[] 


# This is the method which presents the menu to the user 
def menu():
    menu = {}
    print ("***************************************************\n")
    print ("------WELCOME TO THE CURRENCY CONVERTER APP------- \n")
    print ("***************************************************\n")
    print ("------ENTER YOUR CHOICE------\n")
    menu['1']="ENTER 1 TO PERFORM CONVERSION : " 
    menu['2']="ENTER 2 TO RETRIEVE HISTORY : "
    menu['3']="ENTER 3 TO GET HELP : "
    menu['4']="ENTER 4 TO EXIT THE APPLICATION : "
    while True: 
        options=menu.keys()
        options.sort()
        for entry in options: 
            print (menu[entry])
        selection=raw_input("PLEASE SELECT YOUR OPTION: \n") 
        if selection =='1': 
            performConversion()     
        elif selection == '2': 
           retrieveHistory()
        elif selection == '3':
           seekHelp() 
        elif selection == '4': 
           sys.exit("EXITING APPLICATION..")
        else: 
           print ("UNKNOWN OPTION SELECTED !! TRY AGAIN..")


# This is the method to perform conversions of transactions 
def performConversion():
    # The user provides the currency type in ISO 4217 Three Letter Currency Codes
    # i.e USD for United States Dollars
    # For this application i/p currency type is always United States Dollars i.e USD
    
    print ("ENTER THE INPUT CURRENCY TYPE IN CAPS & AMOUNT SEPARATED BY SPACES:")
    input_args=raw_input()
    input_values=input_args.split(" ")
    input_curr_type=str(input_values[0])
    input_curr_val=float(input_values[1])
    print ("ENTER THE DESIRED OUTPUT CURRENCY TYPES IN CAPS SEPARATED BY SPACES:");
    output_args=raw_input()
    output_curr_types=output_args.split(" ")     
    liveRatesURL=baseURL+'live' 
    currencies= ','.join(output_curr_types) 
    params={'access_key': yourAPIKey, 'currencies': currencies, 'format': 1}
    r = requests.get(liveRatesURL, params = params)
    livequote=r.json()  
    SOURCE=livequote["source"]
    STATUS=livequote["success"]
    TIMESTAMP=livequote["timestamp"]
    LASTCHANGED=time.ctime(TIMESTAMP)
    CURRENTTIME=time.ctime(time.time())
    QUOTES=livequote["quotes"] 
    print ("*************************************")
    print("TRANSACTION DETAILS ARE AS FOLLOWS : \n")
    for r in QUOTES:
        transactions=[]
        source_target=str(r)
        rate=QUOTES[r]
        amount=input_curr_val*rate
        str1="SOURCE_TARGET_CURRENCIES: "+source_target
        str2="RATE: "+str(rate)
        str3="INPUT_AMOUNT: "+str(input_curr_val)
        str4="OUTPUT_AMOUNT: "+str(amount)
        str5="LAST_CHANGED: "+str(LASTCHANGED)
        str6="DATE: "+str(CURRENTTIME)
        transactions.append(str1)
        transactions.append(str2)
        transactions.append(str3)
        transactions.append(str4)
        transactions.append(str5)
        transactions.append(str6)
        history.append(transactions)
        
        print("SOURCE & TARGET CURRENCIES = ",source_target)
        print("RATE = ",str(rate))
        print("INPUT_AMOUNT =",str(input_curr_val))
        print("OUTPUT_AMOUNT = ",str(amount))
        print("RATE_LAST_CHANGED = ",str(LASTCHANGED))
        print("DATE = ",str(CURRENTTIME))
        print ("*************************************")
    
    
    
    
# This is the method to retrieve history of transactions
def retrieveHistory():
    
    maxHistory=len(history)
    print ("%d TOTAL HISTORICAL TRANSACTIONS ARE STORED IN DATABASE"%(maxHistory))
    print ("ENTER THE NUMBER OF HISTORICAL TRANSACTIONS YOU WANT TO RETRIEVE: ")
    hist=int(raw_input())
    
    print ("PRINTING THE HISTORY OF TRANSACTIONS : ")
    print("*************************************")
    for h in range(0,hist):
        details=history[h]
        
        print(details[0])
        print(details[1])
        print(details[2])
        print(details[3])
        print(details[4])
        print(details[5])
        print("*************************************")
    
# This is the HELP method
def seekHelp():
    
    print("*************************************")
    print("THIS IS THE DETAILED HELP METHOD : ")
    print("*************************************")
    print('Format of input params of performConversion() method : ')
    print('Enter Input Currency Code,Enter a space,Enter amount  ')
    print('Format of input params of retrieveHistory() method : ')
    print('Enter 1st Output Currency Code,Enter a space,Enter 2nd Currency Code,...continue entering currency codes  ')
    print('Press 3 anytime for HELP : ')
    print('Press 4 to EXIT the application : ')
    print("*************************************")

#This is the main method
if __name__ == "__main__":    
    menu()




