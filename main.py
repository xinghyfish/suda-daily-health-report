# -*- coding:utf-8 -*-
import json
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""
@author: Xosmos
@email: hyxing@stu.suda.edu.cn
"""
"""0. Prepare and config basic information"""
chromedriverUrl = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
driver = webdriver.Chrome(chromedriverUrl)   # initialize driver version
# turn information json into a dict
load_dict = {}
with open("info.json", encoding="utf-8") as load_f:
    load_dict = json.load(load_f)
temperature = "36"
account = load_dict["account"]
passwd = load_dict["passwd"]
current_location = load_dict["current_location"]
town_and_community = load_dict["town_and_community"]
# location cast
location_dict = {
    "在校": 1,
    "在苏州": 2,
    "江苏省其他地区": 3,
    "在境外、在中高风险地区": 4,
    "在中高风险地区所在城市": 5,
    "在其他地区": 6
}
# target url, redirect to: "https://my.suda.edu.cn/portal/_s2/anonymous_sy/main.psp"
suda_url = "https://my.suda.edu.cn"
MAX_WAIT_SEC = 10

"""1. log in"""
driver.get(suda_url)
driver.maximize_window()
# Store iframe web element
try:
    iframe = WebDriverWait(driver, MAX_WAIT_SEC).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".unLoginSd_application_iframe > iframe"))
    )
except TimeoutException:
    print("LOAD ERROR!")
    driver.close()
else: # switch to selected iframe, else won't find button
    driver.switch_to.frame(iframe)
# Now click on button to enter log in page
button = driver.find_element(by=By.CLASS_NAME, value="button")
button.click()

"""2. log in by username and password"""
# clear and input username
username_input = driver.find_element(by=By.ID, value="username")
username_input.clear()
username_input.send_keys(account)
# clear and input password
password_input = driver.find_element(by=By.ID, value="password")
password_input.clear()
password_input.send_keys(passwd)
# click log in button
button = driver.find_element(by=By.CLASS_NAME, value="login-btn")
button.click()

"""3. enter navigate list and find health info page entrance"""
nav_list = driver.find_elements(by=By.CLASS_NAME, value="nav_list")
nav_list[1].click() # enter app list
try:
    iframe = WebDriverWait(driver, MAX_WAIT_SEC).until(
        EC.presence_of_element_located((By.ID, "frameServer"))
    )
except TimeoutException:
    print("LOAD ERROR")
    driver.close()
else:
    driver.switch_to.frame(iframe)   # IMPORTANT, else don't work

try:
    service = WebDriverWait(driver, MAX_WAIT_SEC).until(
        EC.presence_of_element_located((By.ID, "1929"))
    )   # find health app
except TimeoutException:
    print("LOAD ERROR")
    driver.close()
else:
    service.click() # then a new page jumps out

"""4. switch to health-app and fill form"""
windows = driver.window_handles
driver.switch_to.window(windows[1]) # switch to new web to go on
# fill in body temperature, default 36
try:
    morning_temp = WebDriverWait(driver, MAX_WAIT_SEC).until(
        EC.presence_of_element_located((By.ID, "input_swtw"))
    )
    morning_temp.send_keys(temperature)
except TimeoutException:
    print("LOAD ERROR!")
    driver.close()


driver.find_element(by=By.ID, value="input_xwtw").send_keys(temperature)
# roll page down
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
choices = driver.find_elements(by=By.CLASS_NAME, value="iCheck-helper")
choices[2].click()
# select current area
selector = driver.find_element(by=By.XPATH, value="//*[@id=\"form\"]/div[3]/div[5]/div/div/div[2]/div/span/span[1]/span")
selector.click()
for i in range(location_dict[current_location]):
    selector.send_keys(Keys.DOWN)
selector.send_keys(Keys.ENTER)
# fill in specific location
location_input = driver.find_element(by=By.ID, value="input_jtdz")
location_input.clear()
location_input.send_keys(town_and_community)
# tick rest boxes
for i in range(15, 28, 2):
    choices[i].click()
# post the form and stop
driver.find_element(by=By.ID, value="tpost").click()

try:
    submit = WebDriverWait(driver, MAX_WAIT_SEC).until(
        EC.presence_of_element_located((By.CLASS_NAME, "layui-layer-btn0"))
    )
    submit.click()
except TimeoutException:
    print("LOAD ERROR!")
finally:
    driver.close()


if __name__ == '__main__':
    pass    # thank you for watching! :)