
driver = webdriver.Chrome()

def site_login():
driver.get (“login.html”)
driver.find_element_by_id(“fname”).send_keys(“abc”)
driver.find_element_by_id(“email”).send_keys(“abc@example.com”)
driver.find_element_by_id (“password”).send_keys(“abc1234”)
driver.find_element_by_id(“login”).click()

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait WebDriverWait(driver, 10).until(EC.title_contains("home"))