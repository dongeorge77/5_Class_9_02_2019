import time

from selenium import webdriver

browser='chrome'
if browser=='chrome':
    driver=webdriver.Chrome(executable_path="C:/Users/ADMIN/PycharmProjects/S_Class/drivers/chromedriver.exe")
elif browser=='firefox':
    driver=webdriver.Firefox(executable_path="C:/Users/ADMIN/PycharmProjects/S_Class/drivers/geckodriver.exe")
elif browser=='ie':
    driver=webdriver.Ie(executable_path="C:/Users/ADMIN/PycharmProjects/S_Class/drivers/IEDriverServer.exe")
else:
    print("Provide appropriate browser name")


driver.get("http://makemytrip.com")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element_by_id("header_tab_hotels").click()
driver.find_element_by_id("header_tab_holidays").click()
driver.back()
driver.forward()
driver.refresh()