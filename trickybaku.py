import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=service)


try:
    driver.get("https://www.youtube.com/")

    time.sleep(3)

    search_bar = driver.find_element(By.NAME, "search_query")
    search_bar.send_keys("suxumski maxo")
    search_bar.send_keys(Keys.RETURN)

    time.sleep(3)

    first_video = driver.find_elements(By.CSS_SELECTOR, "#video-title")[0]
    first_video.click()

    time.sleep(5)

finally:
    driver.quit()
