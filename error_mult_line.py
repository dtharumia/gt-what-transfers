from selenium import webdriver
import numpy as np
import pandas as pd
import time
from selenium.webdriver.chrome.options import Options
import os

# DRIVER_PATH = './chromedriver'

# driver = webdriver.Chrome(executable_path=DRIVER_PATH)

# df = pd.DataFrame(columns=['state_entry', 'term', 'school_name', 't_class',
#                   't_title', 't_level', 't_mingrade', 'gt_class', 'gt_title', 'gt_ch'])

# driver.get('https://oscar.gatech.edu/pls/bprod/wwsktrna.P_find_location')

# school in US
# driver.find_element_by_xpath("//input[@value='Yes']").click()

# state_entry = ""
# term = ""
# school_name = ""
# t_class = ""
# t_title = ""
# t_level = ""
# t_mingrade = ""
# gt_class = ""
# gt_title = ""
# gt_ch = ""

df = pd.read_csv('data.csv')
# print(df)

print(len(df['school_name'].unique()))

# df = df[df['t_class'] == '0']

# print('\nResult dataframe :\n', df)

# df = df.drop_duplicates(subset=['school_name'])

# df.to_csv('error.csv')
# print(df)