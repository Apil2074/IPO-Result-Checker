import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


boids = ['1301610000548341','1301610000725387','1301650000616574']
names = ['Apil','Rajendra','Ajit']


this = input("Enter the begnnings of Company: ")
# webdriver.Chrome(executable_path=r'C:\webdriver\chromedriver.exe')

for boid in boids:
    driver = webdriver.Chrome(executable_path=r'C:\webdriver\chromedriver.exe')
    driver.minimize_window()  
    driver.get('https://iporesult.cdsc.com.np')


    searchbox = driver.find_element_by_name('companyShare')
    searchbox.send_keys(this)
    searchselect = Select(searchbox)
    boidenter = driver.find_element_by_xpath('//*[@id="boid"]')
    boidenter.send_keys(boid)
    check = driver.find_element_by_xpath("/html/body/app-root/app-allotment-result/div/div/div/div/form/button")
    check.click()
    time.sleep(2)

    if boid == '1301610000548341':
        name = names[0]
    if boid == '1301610000725387':
        name = names[1]     
    if boid == '1301650000616574':
        name = names[2]  
    # print(name)   
    print(name+driver.find_element_by_xpath("/html/body/app-root/app-allotment-result/div/div/div/div/form/p[2]").get_attribute('innerHTML'))# ALLOTTED
    print(name+driver.find_element_by_xpath("/html/body/app-root/app-allotment-result/div/div/div/div/form/p[1]").get_attribute('innerHTML')) #NOT ALLOTTED
    driver.close()

    # result = 
# sresult = Select(result)
# print(sresult)

# result = driver.find_element_by_xpath('/html/body/app-root/app-allotment-result/div/div/div/div/form/p[2]')


# checkres = result.get_attribute('innerHTML')

# print(checkres);
# /html/body/app-root/app-allotment-result/div/div/div/div/form/p[2]