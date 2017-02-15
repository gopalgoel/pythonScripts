from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

driver = None

def wait(web_opening_time=3):
	time.sleep(web_opening_time)

def load_driver():
	global driver
	driver = webdriver.Chrome()
def quit():
	driver.quit()

def whatsapp_login():
	driver.get('https://web.whatsapp.com/');
	wait(10)

def send_message(msg='Hi!'):
	obj = driver.find_element_by_xpath("//div[@contenteditable='true']")
	obj.send_keys(msg)
	obj.send_keys(Keys.RETURN)


if __name__ == "__main__":
	load_driver()
	whatsapp_login()
	wait()
	while 1==1:
		try:
			friend = str(input("Friend's name?\n"))
			number_of_times = int(input("How many times?\n"))
			message = str(input("Message?\n"))
			web_obj = driver.find_element_by_xpath("//span[@title='" + friend + "']")
			web_obj.click()
		except NoSuchElementException:
			print("No such name exists\n")
			continue
		else:
			for i in range(number_of_times):
				send_message(message)
			print("Process complete successfully")
	wait()
	quit()