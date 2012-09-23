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

settings_file = open(os.path.expanduser(os.path.join('~', '.tompkins-trust.json')))
settings = json.loads(settings_file.read())
settings_file.close()

d = _driver_setup()

# Username
d.get('https://www.tompkinstrust.com/accountlogin6x.html')
d.find_element_by_id('username').send_keys(settings['username'])

# Password
d.find_element_by_xpath('//input[@type="image"]').click()

# Checks
if settings['login-phrase'] not in d.page_source:
    raise AssertionError('Your login phrase is not shown on the page.')

#input_data = d.find_elements_by_css_selector('td.input_data')
#if input_data[0].text != settings['username']:
#    params = (input_data[0].text, settings['username'])
#    raise AssertionError('Page shows username as "%s" instead of "%s".' % params)
#if input_data[2].text != u'*':
#    params = (input_data[2].text, u'*')
#    raise AssertionError('Page shows star as "%s" instead of "%s".' % params)
#
#if input_data[3].text != u'':
#    params = (input_data[3].text, u'u')
#    raise AssertionError('Page shows answer as "%s" instead of nothing ("%s").' % params)

# Handle question
#question = input_data[1].text
#if not question in settings:
#    raise ValueError('Please add a value for questions["%s"] in ~/tompkins-trust.json' % question)

# Let the page load.
sleep(2)

# Impute
#d.find_element_by_css_selector('input[type="checkbox"]').click()
#d.find_element_by_css_selector('input[type="text"]').send_keys(settings['questions'][question]) 
d.find_element_by_id('login_form:password').send_keys(settings['password'])

# Submit
d.find_element_by_id('login_form:login').click() 
