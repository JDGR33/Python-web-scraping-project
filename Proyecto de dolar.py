# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 13:57:22 2021

@author: Julio
"""
#Importing the Web Screaping Libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup
#Importing date library
from datetime import date
#Import DataBase libraries
import  ibm_db

#Url of the Central Bank of Venezuela
html = urlopen('http://www.bcv.org.ve/')

#Web Screpaing the Converation Rate of $ to BS
bs = BeautifulSoup(html.read(),'html.parser')
dolarBox = bs.find(id="dolar").find ('div',{'class':"col-sm-6 col-xs-6 centrado"})

#Transforming the text base converation rate to a floar number
dolarText = dolarBox.get_text().replace(",",".")
convertaionRate = float(dolarText)

#Formating the date of the data point
d1 = date.today().strftime("%d/%m/%Y")


#Prints the date and converation rate
print("The convertarion Rate on ",d1," was ", convertaionRate)