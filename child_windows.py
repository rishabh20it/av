from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
driver.implicitly_wait(15)
#time.sleep(10)


driver.find_element(By.LINK_TEXT , "Click Here").click()
windows_opened=driver.window_handles

driver.switch_to.window(windows_opened[1])
text= print(driver.find_element(By.TAG_NAME , "h3").text)


driver.switch_to.window(windows_opened[0])
text_2= print(driver.find_element(By.TAG_NAME , "h3").text)

