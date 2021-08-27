from selenium import webdriver
import csv
DRIVER_PATH = './chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://oscar.gatech.edu/pls/bprod/wwsktrna.P_find_location')

# school in US
driver.find_element_by_xpath("//input[@value='Yes']").click()

# what state
# print(len(driver.find_elements_by_xpath('//option')))

state = driver.find_element_by_xpath('//option[10]')  # change manual
state.click()
driver.find_element_by_xpath('//input[@value="Get State"]').click()

# what school
# for count in range(0, len(driver.find_elements_by_xpath('//option'))):
    # print(count)
    # print('//option[' + str(count) + ']')
school = driver.find_element_by_xpath('//option[' + str(1) + ']')  # change manual
school.click()
driver.find_element_by_xpath('//input[@value="Get School"]').click()

# subject, level, term
subject = driver.find_element_by_xpath('//option[10]')  # change manual
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



