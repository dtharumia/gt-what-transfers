from selenium import webdriver
import numpy as np
import pandas as pd
import time
from selenium.webdriver.chrome.options import Options
import os

DRIVER_PATH = './chromedriver'

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")

driver = webdriver.Chrome(executable_path=DRIVER_PATH)


df = pd.DataFrame(columns=['school_name', 't_class',
                  't_title', 'gt_class', 'gt_title'])

driver.get('https://oscar.gatech.edu/pls/bprod/wwsktrna.P_find_location')

# school in US
driver.find_element_by_xpath("//input[@value='Yes']").click()

school_name = ""
t_class = ""
t_title = ""
gt_class = ""
gt_title = ""

# goes through all states
for count_state in range(1, len(driver.find_elements_by_xpath('//option')) + 1):
    state = driver.find_element_by_xpath('//option[' + str(count_state) + ']')
    state.click()
    driver.find_element_by_xpath('//input[@value="Get State"]').click()
    # time.sleep(3)

    # goes through all schools
    for count_school in range(1, len(driver.find_elements_by_xpath('//option')) + 1):
        school = driver.find_element_by_xpath(
            '//option[' + str(count_school) + ']')
        school_name = school.text
        # df.loc[(len(df.index))] = [school.text, 0, 0, 0, 0]
        # print(df)
        # print(school_name)
        school.click()
        driver.find_element_by_xpath('//input[@value="Get School"]').click()
        # time.sleep(3)

        # goes through all subjects
        for count_subject in range(1, len(driver.find_elements_by_xpath('//option')) + 1):
            subject = driver.find_element_by_xpath(
                '//option[' + str(count_subject) + ']')
            subject.click()
            driver.find_element_by_xpath('//option[@value="US"]').click()
            driver.find_element_by_xpath('//option[@value="202108"]').click()
            driver.find_element_by_xpath(
                '//input[@value="Get Courses"]').click()
            # time.sleep(3)

            try:
                # df.loc[(len(df.index))] = [school_name, 0, 0, 0, 0]
                # print(df)
                start_row = driver.find_element_by_xpath(
                    '//table[@class="datadisplaytable"]//tr[3]')
                # print(start_table.text)
                # start_row = driver.find_elements_by_xpath('//')
                print(start_row.text)
                file1 = open("data.txt", "a")  # append mode
                file1.write(start_row.text)
                file1.close()
                # for count_course in range(3, len(start_table.find_elements_by_xpath('//tr')) + 1):
                #     course = start_table.find_element_by_xpath(
                #         '//tr[' + str(count_course) + ']')
                #     print(course.text)
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
