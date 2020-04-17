from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
import time

url = input("Enter the URL : ")

driver = webdriver.Firefox()
print("Firefox is opened successfully..")

driver.get(url)
print("Url is successfully prased.")
time.sleep(2)

name = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[1]/div/div[2]/div/div[1]/div/div[1]/input').send_keys("Akash Saini")

college = driver.find_element_by_xpath('docssharedWizToggleLabeledLabelText exportLabel freebirdFormviewerViewItemsRadioLabel').click()

time.sleep(3)
driver.execute_script("window.scrollTo(0, 700);")
time.sleep(3)

stream = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[3]/div/div[2]/div[1]/div/label/div/div[1]/div[3]').click()

phone = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[4]/div/div[2]/div/div[1]/div/div[1]/input').send_keys("9779889819")

email = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[5]/div/div[2]/div/div[1]/div/div[1]/input').send_keys('akashsaini0797@gmail.com')

note = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[6]/div/div[2]/div[1]/div[2]/textarea').send_keys("")
