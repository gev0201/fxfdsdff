from selenium import webdriver
from selenium.webdriver.common.by import By


def test_mc():
    driver = webdriver.Chrome()
    driver.implicitly_wait(50)
    driver.get("https://www.list.am/")

    driver.find_element(By.ID, "idSearchBox").send_keys("mercedes")
    # driver.find_element(By.XPATH, "//button[@aria-label='Որոնում']")
    driver.find_element(By.CSS_SELECTOR, "button[aria-label='Որոնում']").click()
    auto = driver.find_elements(By.XPATH, "//*[@id='tp']/div/a")
    for a in auto:
        if "Mercedes G500 պռակատ" in a.text.lower():
            a.click()
