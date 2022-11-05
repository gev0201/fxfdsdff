import time

from selenium import webdriver
from selenium.webdriver.common.by import By  # inport By class for selector choose



driver = webdriver.Chrome()
driver.implicitly_wait(50)
driver.get("https://amazon.com")

driver.find_element(By.ID, "twotabsearchtextbox").send_keys("iphone")
search_button = driver.find_element(By.ID, "nav-search-submit-button")
search_button.click()
items = driver.find_elements(By.CSS_SELECTOR, "span[class $= 'a-text-normal']")
for item in items:
    if "valod" in item.text.lower():
        assert True
    else:
        assert False
