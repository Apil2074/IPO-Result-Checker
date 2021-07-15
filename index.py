import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

boid1 = "XXXXXXXXXXXXXXXX"
boid2 = "XXXXXXXXXXXXXXXX"


this = input("Enter the begnnings of Company: ")

# select = Select(driver.find_element_by_name('name'))
driver = webdriver.Chrome()
driver.maximize_window()  



driver.get('https://iporesult.cdsc.com.np')

searchbox = driver.find_element_by_name('companyShare')
searchbox.send_keys(this)
searchselect = Select(searchbox)
boidenter = driver.find_element_by_xpath('//*[@id="boid"]')
boidenter.send_keys(boid1)
check = driver.find_element_by_xpath("/html/body/app-root/app-allotment-result/div/div/div/div/form/button")
check.click()
time.sleep(1)
driver.close()
driver = webdriver.Chrome()
driver.maximize_window()  

driver.get('https://iporesult.cdsc.com.np')

searchbox2 = driver.find_element_by_name('companyShare')
searchbox2.send_keys(this)
searchselect = Select(searchbox2)
boidenter2 = driver.find_element_by_xpath('//*[@id="boid"]')
boidenter2.send_keys(boid2)
check2 = driver.find_element_by_xpath("/html/body/app-root/app-allotment-result/div/div/div/div/form/button")
check2.click()
time.sleep(1)
driver.close()

# result = driver.find_element_by_xpath('/html/body/app-root/app-allotment-result/div/div/div/div/form/p[2]')
# sresult = Select(result)
# print(sresult)




