from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=es")

driver.find_element(By.XPATH, ".//button[@class='auth-form__button']").click()

driver.quit()
