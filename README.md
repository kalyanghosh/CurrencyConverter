# CurrencyConverter

# TITLE: 
1. This is an application written by me to convert between different currency types.
2. This application uses real-time currency conversion provided by the API of the website http://apilayer.net/

# PREREQUISITE STEPS BEFORE RUNNING THE APPLICATION:
1. Navigate to website http://apilayer.net/
2. Click on the "currencylayer API" tab below which provides a real time currency conversion JSON API
3. Sign up for the Free version. Note: For the Free version you can only get <b>1000</b> hits for currency conversion.
4. After signing in, you will be given a unique API key for use.

   4.1 Copy that API key

   4.2 Open the <b>currencyConverter.py</b> file in an editor

   4.3 Paste the key in the variable named <b>yourAPIKey</b> inside the <b>currencyConverter.py</b> file.

   4.4 Save and close the python file

# ASSUMPTIONS:
1. The user must provide the currency type in UPPER CASE and in ISO 4217 Three Letter Currency Codes

     i.e USD for United States Dollars 
2. For this application the i/p currency type is always United States Dollars i.e USD


# INPUT ARGUMENTS FORMAT:

1. Format of input params of performConversion() method :

   Enter Input Currency Code,Enter a space,Enter amount
   
   eg: USD 100
2. Format of input params of retrieveHistory() method :

   Enter 1st Output Currency Code,Enter a space,Enter 2nd Currency Code,...continue entering currency codes
   
   eg: INR AUD EUR
   
3. While retrieving the number of historical transactions, the user should enter a number which is less than or equal to the maximum number of transaction history maintained

# HOW TO RUN:

1. Open a terminal

2. Make sure you have python installed in your system 

3. Make sure your python installation path is properly updated so that the application should find python from whichever location it is run

4. Run the currencyConverter.py file by the below command in the terminal:

<b>python currencyConverter.py</b>
