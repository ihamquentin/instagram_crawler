from selenium import webdriver
from bs4 import BeautifulSoup   
import pandas as pd
import datetime
import time

import sys, csv
from bs4 import BeautifulSoup, SoupStrainer
from urllib.request import urlopen
import re
from selenium.webdriver.common.by import By



#this bot is to access my instagram then attempt to
#follow accounts based on a certain tag, also leave
#comments on latest posts in those tags
insta_handle = str(input('ig handle goes in here: '))
insta_password = str(input('ig password goes in here: ')) 


driver = webdriver.Firefox(executable_path=r'C:\webdrivers\geckodriver.exe')

driver.get ("https://www.instagram.com/accounts/login")
time.sleep(7)
driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(insta_handle)
driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(insta_password)
driver.find_element_by_xpath("//button[@type=\"submit\"]").click()

time.sleep(2)
driver.find_element_by_xpath("//button[text()=\"Not Now\"]").click()
commands = {"on": "Turn On" , "off": "Not Now"}
# Formalize input  
command =  {"on": "turn On" , "off": "not Now"}
# If command is neither "on" or "off", return None
time.sleep(3)
driver.find_element_by_xpath("//button[text()=\"Not Now\"]").click()
#if command not in commands:
    #print("Wrong argument please input \"ON\" or \"OFF\" as argument")              
# Click button corresponding to the command 
#try:
    #driver.find_element_by_xpath("//button[text()=\"" + commands.get(command) + "\"]").click()
#except NoSuchElementException:
    #print("Couldn't find " + commands.get(command) + " button.")

driver.find_element_by_xpath("//a[@href=\"/explore/\"]").click()
time.sleep(6) # Adding a wait time to allow the page to load entirely
#driver.find_element_by_xpath("//a[@href=\"/people/\"]").click()
#time.sleep(2) # Adding a wait time to allow the page to load entirely
#soup = BeautifulSoup(driver.page_source,"html")



    
