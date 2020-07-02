from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox()
browser.implicitly_wait(5)

browser.get('https://www.you_web_site/')

sleep(3)

username_input = browser.find_element_by_css_selector("input[name='username']")
password_input = browser.find_element_by_css_selector("input[name='password']")

username_input.send_keys("you_login")
password_input.send_keys("you_pass")

login_button = browser.find_element_by_xpath("//button[@type='submit']")
login_button.click()

sleep(15)

browser.close()
