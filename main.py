from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as expect
import time

# Data declaration here:
username = ""  # put your username here
password = ""  # put your password here
working_time = "8"  # for working time
hour_rate_to_fill = "1x - Normal working days"  # for Hour Rate dropdown, modify your exact rate in the dropdown
activity_to_fill = "Code"  # for Activity dropdown, modify your exact activity in the dropdown
project_to_fill = "TooGood ODC"  # for normal working day, modify your exact project in the dropdown
# End data declaration

driver = webdriver.Chrome(executable_path="./chromedriver.exe")

driver.get("https://insider.saigontechnology.vn/dashboard")

# Login page
username_element = WebDriverWait(driver, 120, 1).until(expect.visibility_of_element_located((By.ID, "Username")))
username_element.send_keys(username)
driver.find_element_by_id("Password").send_keys(password)
driver.find_element_by_class_name("btn-login").click()

# dashboard page
today_element = WebDriverWait(driver, 120, 1).until(expect.visibility_of_element_located((By.CLASS_NAME, "fc-today")))
ActionChains(driver).move_to_element(today_element).click().perform()

# Log time pop-up
hour_element = WebDriverWait(driver, 120, 1).until(expect.visibility_of_element_located((By.ID, "hour")))
hour_element.send_keys(working_time)

selects = driver.find_elements_by_css_selector("input[placeholder='Type something']")

hour_rate = selects[0]
hour_rate.click()
time.sleep(1)
rate_option = WebDriverWait(driver, 120, 1)\
    .until(expect.visibility_of_element_located((By.XPATH, "//*[text()=' " + hour_rate_to_fill + " ']")))
rate_option.click()

activity = selects[1]
activity.click()
activity_option = WebDriverWait(driver, 120, 1)\
    .until(expect.visibility_of_element_located((By.XPATH, "//*[text()=' " + activity_to_fill + " ']")))
activity_option.click()

project = selects[2]
project.click()
project_option = WebDriverWait(driver, 120, 1)\
    .until(expect.visibility_of_element_located((By.XPATH, "//*[text()=' " + project_to_fill + " ']")))
project_option.click()

save_close_btn = driver.find_element_by_xpath("//*[text()=' Save & Close ']")
save_close_btn.click()

driver.close()
