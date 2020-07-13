from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Firefox()
browser.implicitly_wait(3)

browser.get('https://www.fl.ru/login/')
sleep(3)

username_input = browser.find_element_by_css_selector("input[name='login']")
password_input = browser.find_element_by_css_selector("input[name='passwd']")

username_input.send_keys("email")
<<<<<<< HEAD
password_input.send_keys("password")
=======
password_input.send_keys("pass")
>>>>>>> 4df8d367a1194fb85a1cc042edc1e3d93480b7e3

login_button = browser.find_element_by_xpath("//button[@type='submit']")
login_button.click()
sleep(10)

filter_button = browser.find_element_by_css_selector("button.b-button.b-button_flat.b-button_flat_green")
filter_button.click()
sleep(50)

while 1:
	filter_button = browser.find_element_by_css_selector("button.b-button.b-button_flat.b-button_flat_green")
	filter_button.click()
	sleep(180)

#browser.close()
