from selenium import webdriver
import csv
import time

DRIVER_PATH = './chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://oscar.gatech.edu/pls/bprod/wwsktrna.P_find_location')

# school in US
driver.find_element_by_xpath("//input[@value='Yes']").click()

# what state



# what school

for count_state in range(1, len(driver.find_elements_by_xpath('//option'))):
    state = driver.find_element_by_xpath('//option[' + str(count_state) + ']')
    state.click()
    driver.find_element_by_xpath('//input[@value="Get State"]').click()
    for count_school in range(1, len(driver.find_elements_by_xpath('//option'))):
        school = driver.find_element_by_xpath('//option[' + str(count_school) + ']')
        school.click()
        driver.find_element_by_xpath('//input[@value="Get School"]').click()

        # subject, level, term
        subject = driver.find_element_by_xpath('//option[2]')  # change manual
        subject.click()
        driver.find_element_by_xpath('//option[@value="US"]').click()
        driver.find_element_by_xpath('//option[@value="202108"]').click()
        driver.find_element_by_xpath('//input[@value="Get Courses"]').click()

        # data file
        # data = open("data.txt", "a")
        # data.write(driver.find_element_by_class_name('datadisplaytable').text)
        # data.close()

        # search another school
        driver.find_element_by_xpath('//input[@value="Search Another School"]').click()
        time.sleep(3)
    driver.find_element_by_xpath('//input[@value="Search Another State"]').click()



