from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.FirefoxOptions()
#options.add_argument("--headless")

driver = webdriver.Firefox(options=options)

driver.get('https://ortus.rtu.lv/')

nameInput = driver.find_element(By.ID, "IDToken1")
passwordInput = driver.find_element(By.ID, "IDToken2")
loginBtn = driver.find_element(By.NAME, "Login.Submit")

nameInput.send_keys(input("Ortus lietotajvards: "))
passwordInput.send_keys(input("Ortus parole: "))
loginBtn.click()
