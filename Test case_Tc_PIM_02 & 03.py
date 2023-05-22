import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Test case ID:TC_PIM_02
# User Management

driver = webdriver.Chrome();
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(10)
driver.find_element(By.XPATH,'//input[contains(@name,"username")]').send_keys("Admin")
driver.find_element(By.XPATH,'//input[contains(@type,"password")]').send_keys("admin123")
driver.find_element(By.XPATH,'//button[contains(@class,"oxd-button oxd-button--medium oxd-button--main orangehrm-login-button")]').click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,'//a[contains(@class,"oxd-main-menu-item")]').click()
time.sleep(10)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button').click()
time.sleep(5)
driver.find_element(By.XPATH,'//i[contains(@class,"oxd-icon bi-caret-down-fill oxd-select-text--arrow")][1]').click()
driver.find_element(By.XPATH,'//div[@role="option"]/span[text()="Admin"]').click()
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div/div[2]/i').click()
driver.find_element(By.XPATH,'//div[@role="option"]/span[text()="Enabled"]').click()
driver.find_element(By.XPATH,'//input[contains(@placeholder,"Type for hints...")]').send_keys("Alice  Duval")
driver.find_element(By.XPATH,'//input[contains(@autocomplete,"off")][1]').send_keys("krith@123")
driver.find_element(By.XPATH,'//input[contains(@type,"password")][1]').send_keys("Password@123")
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input').send_keys("Password@123")
driver.find_element(By.XPATH,'//button[contains(@type,"submit")]').click()
time.sleep(5)

# Job
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]').click()
driver.find_element(By.XPATH,'//a[contains(@class,"oxd-topbar-body-nav-tab-link")][1]').click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,'//button[contains(@class,"oxd-button oxd-button--medium oxd-button--secondary")]').click()
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/input').send_keys("tester")
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/textarea').send_keys("Testing website")
driver.find_element(By.XPATH,'//button[contains(@type,"submit")]').click()
time.sleep(10)

# Organistation
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/span').click()
driver.find_element(By.XPATH,'//a[contains(@class,"oxd-topbar-body-nav-tab-link")][1]').click()
driver.implicitly_wait(5)
driver.find_element(By.XPATH,'//span[contains(@class,"oxd-switch-input oxd-switch-input--active --label-left")]').click()
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input').send_keys("123456")
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input').send_keys("5456")
driver.find_element(By.XPATH,'//input[contains(@modelmodifiers,"[object Object]")]').send_keys("9876543210")
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[2]/div/div[2]/input').send_keys("32110")
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[4]/div/div[2]/div/div[2]/input').send_keys("538/103 Teal Plaza")
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[5]/div/div[2]/div/div[2]/input').send_keys("600066")
driver.find_element(By.XPATH,'//i[contains(@class,"oxd-icon bi-caret-down-fill oxd-select-text--arrow")]').click()
driver.find_element(By.XPATH,'//div[@role="option"]/span[text()="India"]').click()
driver.find_element(By.XPATH,'//button[contains(@type,"submit")]').click()

# qulification
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]').click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,'//a[contains(@role,"menuitem")][1]').click()
driver.implicitly_wait(5)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[1]/div/button').click()
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/input').send_keys("krithik")
driver.find_element(By.XPATH,'//textarea[contains(@placeholder,"Type description here")]').send_keys("Best tester")
driver.find_element(By.XPATH,'//button[contains(@type,"submit")]').click()
time.sleep(10)

# Nationalty
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[5]').click()
driver.implicitly_wait(5)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[1]/div/button').click()
time.sleep(10)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/input').send_keys("India")
driver.find_element(By.XPATH,'//button[contains(@type,"submit")]').click()
driver.implicitly_wait(5)

# corporate Banking

driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[6]/a').click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div').click()
action = ActionChains(driver)
action.click_and_hold(driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div[2]/input[1]')).move_by_offset(100,0).perform()
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/div/div').click()
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/div/div[2]/input[2]').send_keys("#412929")
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div/div/div/label/span').click()
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[4]/div/button[3]').click()
driver.implicitly_wait(15)

# Configureation
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[7]/span').click()
driver.find_element(By.XPATH,"//a[contains(@role,'menuitem')][1]").click()
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[2]/div/label/span').click()
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input').send_keys("jhk")
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input').send_keys("mnop")
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div/div/div[2]/div[2]/div[2]/div/label/span').click()
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[4]/div/div/div/div/label/span').click()
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[6]/div/div/div/div/label/span').click()
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[7]/div/div/div/div[2]/input').send_keys("krith@gmail.com")

#driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div/div/div/label/span').click()
driver.find_element(By.XPATH,'//button[contains(@class,"oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space")]').click()


# TEST CASEE ID : TC_PIM_03

driver.find_element(By.XPATH,'//button[contains(@type,"button")][1]').click()
time.sleep(5)
driver.find_element(By.XPATH,'//button[contains(@type,"button")][1]').click()
driver.find_element(By.XPATH,'//a[contains(@class,"oxd-main-menu-item active")]').click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a').click()
driver.implicitly_wait(15)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a').click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a').click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a').click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a/span').click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a').click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a/span').click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a/span').click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[9]/a').click()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[10]/a/span').click()
driver.implicitly_wait(10)
wait = WebDriverWait(driver,10)
password = wait.until(EC.presence_of_element_located((By.XPATH,"//input[contains(@type,'password')]")))
password.send_keys("admin123")
#driver.find_element(By.XPATH,"").send_keys("admin123")
driver.find_element(By.XPATH,"//button[contains(@type,'submit')]").click()
driver.implicitly_wait(15)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[11]/a/span').click()
driver.implicitly_wait(15)
driver.quit()
