# autoweb.py

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from datetime import datetime
import csv


def write(data=['SS-1001','30.45','50.44','2022-08-06 15:05:05']):
	with open('result.csv','a',newline='',encoding='utf-8') as file:
		fw = csv.writer(file)
		fw.writerow(data)


path = r'C:\Users\Uncle Engineer\Desktop\Basic Python\Automated Website\chromedriver_win32\chromedriver.exe'
service = Service(path)

options = webdriver.ChromeOptions()
options.headless = True # Don't launch Chrome

driver = webdriver.Chrome(service=service,options=options)

url = 'http://www.uncle-machine.com/login/'

driver.get(url)



username  = driver.find_element(By.ID, "username")
username.clear()
username.send_keys('USERNAME')

password  = driver.find_element(By.ID, "password")
password.send_keys('PASSWORD')

password.send_keys(Keys.RETURN) #press 'enter'

sensor_url = 'http://www.uncle-machine.com/sensor/'
driver.get(sensor_url)


search = driver.find_element(By.ID,'sid')

sensorid = 'SS-1001'
search.send_keys(sensorid)
search.send_keys(Keys.RETURN)

time.sleep(1)

temperature = driver.find_element(By.CLASS_NAME,'temp')
humid = driver.find_element(By.CLASS_NAME,'humid')

t = temperature.text.split(' ')[1]
h = humid.text.split(' ')[1]
stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
data = [sensorid, t, h, stamp]
write(data)

time.sleep(3)
driver.quit()