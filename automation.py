from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

driver = webdriver.Firefox()
driver.get("https://docs.google.com/forms/d/e/1FAIpQLScDCQdVDnrt5i3j0T9YJgP65Aev_7STwc3EgBT-aO1lgnwQ-A/viewform?usp=sf_link")

uname = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[1]/div/div[2]/div/div[1]/div/div[1]/input')
uname.send_keys("Akash")

cname = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/input')
cname.send_keys("Globallogic.com")

driver.find_element(By.CSS_SELECTOR, ".freebirdFormviewerViewItemsRadioOptionContainer:nth-child(1) .docssharedWizToggleLabeledLabelText").click() 

time.sleep(3)
driver.execute_script("window.scrollTo(0, 900);")
time.sleep(3)
#driver.find_element(By.CSS_SELECTOR, ".isSelected > .quantumWizMenuPaperselectContent").click()

driver.find_element(By.CSS_SELECTOR, ".isSelected").click()
# 4 | click | css=.exportSelectPopup > .isSelected > .quantumWizMenuPaperselectContent |  | 
driver.find_element(By.CSS_SELECTOR, ".exportSelectPopup > .isSelected > .quantumWizMenuPaperselectContent").click()

'''
se_ne = driver.find_element_by_class_name("quantumWizMenuPaperselectOption").click()
time.sleep(3)
print("option opened")
#network = driver.find_element_by_xpath("//span[text()='4 G']").click()
network = driver.find_element_by_tag_name("4 G").click()
'''

driver.find_element(By.NAME, "entry.211057078").send_keys("mastermindvishu97@gmail.com")
