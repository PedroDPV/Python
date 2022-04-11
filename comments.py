from instascrape import Profile 
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.instagram.com/')

time.sleep(5)
username=driver.find_element_by_css_selector("input[name='username']")
password=driver.find_element_by_css_selector("input[name='password']")
username.clear()
password.clear()
username.send_keys("sirdatadummy")
password.send_keys("Sauter@2022")
login = driver.find_element_by_css_selector("button[type='submit']").click()

time.sleep(5) 
notnow = driver.find_element_by_xpath("//button[contains(text(), 'Agora não')]").click() 
time.sleep(5)
notnow2 = driver.find_element_by_xpath("//button[contains(text(), 'Agora não')]").click() 

time.sleep(5) 
searchbox=driver.find_element_by_css_selector("input[placeholder='Pesquisar']") 
searchbox.clear() 
searchbox.send_keys("cea_brasil") 
time.sleep(5) 
searchbox.send_keys( Keys.ENTER) 
time.sleep(5) 
searchbox.send_keys(Keys.ENTER)
cea = Profile('cea_brasil')
cea.scrape()