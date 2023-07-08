from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://ya.ru")

sleep(5)

driver.fullscreen_window()

sleep(5)

driver.save_screenshot('./ya.png')

# driver.back()
# driver.forward()
# driver.refresh()

# driver.set_window_size(640, 460)



sleep(5)