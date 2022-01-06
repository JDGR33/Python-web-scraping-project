# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 13:57:22 2021

@author: Julio
"""
#Importing the Web Screaping Libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup
#Importing date library
import datetime
#Import DataBase libraries
#import  ibm_db

#Import librery for Schedule events
import sched, time

schedule = sched.scheduler(time.time, time.sleep)


#Retturns the exchange rate and the date-time of the extraction
def get_conversion_bcv():

    #Url of the Central Bank of Venezuela
    html = urlopen('http://www.bcv.org.ve/')
    
    #Web Screpaing the Converation Rate of $ to BS
    bs = BeautifulSoup(html.read(),'html.parser')
    dolarBox = bs.find(id="dolar").find ('div',{'class':"col-sm-6 col-xs-6 centrado"})
    
    #Transforming the text base converation rate to a floar number
    dolarText = dolarBox.get_text().replace(",",".")
    exchangeRate = float(dolarText)
    
    #Formating the date and time of the data point
    extractionDate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    print("The convertarion Rate on ",extractionDate," was ", exchangeRate)
    
    return(exchangeRate,extractionDate)


#Schedule the reading of data
def do_something(delay=1): 
    print("Doing stuff...")
    #Prints the date and exchange Rate
    get_conversion_bcv()
    #this begins the loop again
    schedule.enter(delay, 1, do_something,argument=(delay,))
    


delay = 60# Delay of the reading
#Beginings the loop
schedule.enter(delay, 1, do_something,argument=(delay,))

schedule.run() #Runs the Schdule events
#Prints the date and converation rate
rate,date = get_conversion_bcv()
