import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Test case ID:TC_PIM_01
# Reset password link send sucessfully 

driver = webdriver.Chrome();
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
wait = WebDriverWait(driver,10)
forgot_element = wait.until(EC.presence_of_element_located((By.XPATH,'//p[contains(@class,"oxd-text oxd-text--p orangehrm-login-forgot-header")]')))
forgot_element.click()
#driver.find_element(By.XPATH,'//p[contains(@class,"oxd-text oxd-text--p orangehrm-login-forgot-header")]').clear()
Element = wait.until(EC.presence_of_element_located((By.XPATH,'//input[contains(@class,"oxd-input oxd-input--active")]')))
Element.send_keys("krithik")
driver.find_element(By.XPATH,'//button[contains(@type,"submit")]').click()
time.sleep(10)
driver.close()
