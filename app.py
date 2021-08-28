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
                  't_title', 't_level', 't_mingrade', 'gt_class', 'gt_title', 'gt_ch'])

driver.get('https://oscar.gatech.edu/pls/bprod/wwsktrna.P_find_location')

# school in US
driver.find_element_by_xpath("//input[@value='Yes']").click()

school_name = ""
t_class = ""
t_title = ""
t_level = ""
t_mingrade = ""
gt_class = ""
gt_title = ""
gt_ch = ""

# goes through all states
for count_state in range(
        1, len(driver.find_elements_by_xpath('//option')) + 1):
    state = driver.find_element_by_xpath('//option[' + str(count_state) + ']')
    state.click()
    driver.find_element_by_xpath('//input[@value="Get State"]').click()

    for count_school in range(
            1, len(driver.find_elements_by_xpath('//option')) + 1):
        school = driver.find_element_by_xpath(
            '//option[' + str(count_school) + ']')
        school_name = school.text

        school.click()
        driver.find_element_by_xpath('//input[@value="Get School"]').click()

        for count_subject in range(1, len(driver.find_elements_by_xpath("//select[@name='sel_subj']//option")) + 1):
            subject = driver.find_element_by_xpath(
                '//select[@name="sel_subj"]//option[' + str(count_subject) + ']')
            subject.click()
            try:
                driver.find_element_by_xpath('//option[@value="US"]').click()
                driver.find_element_by_xpath(
                    '//option[@value="202108"]').click()
            except:
                continue
            driver.find_element_by_xpath(
                '//input[@value="Get Courses"]').click()

            for row in range(3, len(driver.find_elements_by_xpath('//table[@class="datadisplaytable"]//tr')) + 1):
                try:
                    t_class = driver.find_element_by_xpath(
                        '//table[@class="datadisplaytable"]//tr[' + str(row) + ']//td[1]').text
                    t_title = driver.find_element_by_xpath(
                        '//table[@class="datadisplaytable"]//tr[' + str(row) + ']//td[2]').text
                    t_level = driver.find_element_by_xpath(
                        '//table[@class="datadisplaytable"]//tr[' + str(row) + ']//td[3]').text
                    t_mingrade = driver.find_element_by_xpath(
                        '//table[@class="datadisplaytable"]//tr[' + str(row) + ']//td[5]').text
                    gt_class = driver.find_element_by_xpath(
                        '//table[@class="datadisplaytable"]//tr[' + str(row) + ']//td[8]').text
                    gt_title = driver.find_element_by_xpath(
                        '//table[@class="datadisplaytable"]//tr[' + str(row) + ']//td[9]').text
                    gt_ch = driver.find_element_by_xpath(
                        '//table[@class="datadisplaytable"]//tr[' + str(row) + ']//td[10]').text
                    df.loc[(len(df.index))] = [school_name,
                                               t_class, t_title, t_level, t_mingrade, gt_class, gt_title, gt_ch]
                except:
                    print('ERROR')
                    df.loc[(len(df.index))] = [
                        school_name, 0, 0, 0, 0, 0, 0, 0]
                finally:
                    df.to_csv('data.csv')
                    print(df)
            driver.find_element_by_xpath(
                '//input[@value="Search Another Subject/Level/Term"]').click()
        driver.find_element_by_xpath(
                '//input[@value="Search Another School"]').click()
            

    driver.find_element_by_xpath(
        '//input[@value="Search Another State"]').click()
