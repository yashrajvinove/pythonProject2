from selenium import webdriver
import time
import pytest

driver = webdriver.Chrome(executable_path='../drivers/chromedriver.exe')

driver.get('https://propftxdevadmin.iworklab.com/login')
driver.maximize_window()
time.sleep(2)

'admin email'
login_email = driver.find_element_by_xpath("//input[@name='loginEmail']").send_keys("rahul.agarwal@mail.vinove.com")
'admin password'
login_pass = driver.find_element_by_xpath("//input[@placeholder='············']").send_keys("Admin@123")
'submit button'
click_submit = driver.find_element_by_xpath("//button[normalize-space()='Sign in']").click()
time.sleep(4)

click_dashboard = driver.find_element_by_xpath("//*[@id='root']/div[1]/div[1]/div[1]").click()
click_usermanagement = driver.find_element_by_xpath("//span[normalize-space()='User Management']").click()
time.sleep(2)
click_list = driver.find_element_by_xpath("//*[@id='root']/div[1]/div[1]/div[3]/ul/li[2]/ul/div/li[1]/a").click()
driver.back()
driver.forward()
driver.refresh()
time.sleep(8)

driver.close()