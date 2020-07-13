from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class bot:
	
	def __init__(self):
		
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(5)
		self.auth_inst() 
		#self.auth_fb()

	def auth_inst(self):
		self.browser.get('https://www.instagram.com/')
		sleep(3)

		self.username_input = self.browser.find_element_by_css_selector("input[name='username']").send_keys("usermane")
		self.password_input = self.browser.find_element_by_css_selector("input[name='password']").send_keys("password")

		self.login_button = self.browser.find_element_by_xpath("//button[@type='submit']")
		self.login_button.click()
		sleep(3)

    self.not_now = self.browser.find_element_by_css_selector('button.sqdOP:nth-child(1)').click()
		self.not_now2 = self.browser.find_element_by_css_selector('button.aOOlW:nth-child(2)').click()
		sleep(15)

	def auth_fb(self):
		self.browser.execute_script("window.open('https://www.facebook.com','_blank');")
		sleep(3)
		self.browser.find_element_by_css_selector('input#email.inputtext.login_form_input_box').send_keys("email")
		self.browser.find_element_by_css_selector("input#pass.inputtext.login_form_input_box").send_keys("pass")
		self.browser.find_element_by_css_selector("input#u_0_4[@type='submit']").click()

#browser.close()

def main():
	b = bot()

if __name__ == '__main__':
	main()
