#!/usr/bin/env python
# coding: utf-8

# In[14]:



from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")
#driver = webdriver.Chrome(executable_path="./chromedriver", options=chrome_options)
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
url = "http://192.168.1.135:8090/ON"
driver.get(url)

