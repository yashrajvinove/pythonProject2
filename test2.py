import time
from idlelib import browser

from selenium import webdriver
import time
import pytest

driver = webdriver.Chrome(executable_path='../drivers/chromedriver.exe')


driver.get('https://propftxdev.iworklab.com/')
'''
signup1 = driver.find_element_by_class_name("login-btn").click()
signup2 = driver.find_element_by_link_text("Signup").click()
signup_name = driver.find_element_by_xpath("//input[@placeholder='Enter Your Full Name']").send_keys("yasshh")
signup_number = driver.find_element_by_xpath("//input[@id='phone']").send_keys("9548779463")
signup_otp = driver.find_element_by_xpath("//button[normalize-space()='Get OTP']").click()'''

login1 = driver.find_element_by_xpath("//a[normalize-space()='Login']").click()
enterph = driver.find_element_by_xpath("//input[@id='phone']").send_keys("9548779463")
getotp_btn = driver.find_element_by_xpath("//button[normalize-space()='Get OTP']").click()
time.sleep(15)
verifyotp_btn = driver.find_element_by_xpath("//button[normalize-space()='Verify OTP']").click()
time.sleep(15)




driver.quit()