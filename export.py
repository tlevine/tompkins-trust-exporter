#!/usr/bin/env python2
import os
import json
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep

def _driver_setup():
    desired_capabilities = webdriver.DesiredCapabilities.FIREFOX
    desired_capabilities['name'] = 'Tompkins Trust'
    driver = webdriver.Remote(desired_capabilities=desired_capabilities,command_executor="http://localhost:4444/wd/hub")
    return driver

def _settings():
    settings_file = open(os.path.expanduser(os.path.join('~', '.tompkins-trust.json')))
    settings = json.loads(settings_file.read())
    settings_file.close()
    return settings

d = _driver_setup()
settings = _settings()

# Username
d.get('https://www.tompkinstrust.com/accountlogin6x.html')
d.find_element_by_id('username').send_keys(settings['username'])

# Password
d.find_element_by_xpath('//input[@type="image"]').click()

# Checks
if settings['login-phrase'] not in d.page_source:
    raise AssertionError('Your login phrase is not shown on the page.')

# Let the page load.
sleep(2)

# Impute password
d.find_element_by_id('login_form:password').send_keys(settings['password'])

# Log in
d.find_element_by_id('login_form:login').click() 

# Click on "Export History
d.find_element_by_partial_link_text('Export History').click()

# OFX format
d.find_element_by_xpath('//input[@name="export_history:export_format"][@value="2"]').click()

# Dates: Today and one fortnight ago
def enter_date(input_id, thedate):
    date_element = d.find_element_by_id(input_id)
    date_element.clear()
    date_element.send_keys(thedate.strftime('%m/%d/%Y'))

today = datetime.date.today()
enter_date('export_history:startDate', today - datetime.timedelta(days=14))
enter_date('export_history:endDate', today)

# Go
d.find_element_by_id('export_history:submit_history').click()
sleep(2)
d.find_element_by_id('export_history_instructions:submit_button').click()
