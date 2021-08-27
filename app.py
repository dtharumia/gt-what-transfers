from selenium import webdriver
import numpy as np
import pandas as pd
import time

DRIVER_PATH = './chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

df = pd.DataFrame(columns=['School', 'T_class',
                  'T_title', 'GT_class', 'GT_title'])

driver.get('https://oscar.gatech.edu/pls/bprod/wwsktrna.P_find_location')

# school in US
driver.find_element_by_xpath("//input[@value='Yes']").click()

# goes through all states
for count_state in range(1, len(driver.find_elements_by_xpath('//option')) + 1):
    state = driver.find_element_by_xpath('//option[' + str(count_state) + ']')
    state.click()
    driver.find_element_by_xpath('//input[@value="Get State"]').click()
    time.sleep(3)

    # goes through all schools
    for count_school in range(1, len(driver.find_elements_by_xpath('//option')) + 1):
        school = driver.find_element_by_xpath(
            '//option[' + str(count_school) + ']')
        school.click()
        driver.find_element_by_xpath('//input[@value="Get School"]').click()
        time.sleep(3)

        # goes through all subjects
        for count_subject in range(1, len(driver.find_elements_by_xpath('//option')) + 1):
            subject = driver.find_element_by_xpath(
                '//option[' + str(count_subject) + ']')
            subject.click()
            driver.find_element_by_xpath('//option[@value="US"]').click()
            driver.find_element_by_xpath('//option[@value="202108"]').click()
            driver.find_element_by_xpath(
                '//input[@value="Get Courses"]').click()
            time.sleep(3)

            try:
                df.loc[(len(df.index))] = [school.text, 0, 0, 0, 0]
                print(df)
                driver.find_element_by_xpath(
                    '//input[@value="Search Another Subject/Level/Term"]').click()
                time.sleep(3)
            except:
                driver.find_element_by_xpath(
                    '//input[@value="Search Another School"]').click()
                time.sleep(3)
                break

    driver.find_element_by_xpath(
        '//input[@value="Search Another State"]').click()
