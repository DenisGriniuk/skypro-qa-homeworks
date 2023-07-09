

# собрать все карточки товаров
# вывести в консоль инфо: название + автор + цена


from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

# зайти на лабиринт
driver.get("https://www.labirint.ru")

# найти книги по слову Python
search_locator = "#search-field"
search_input = driver.find_element(By.CSS_SELECTOR, search_locator)
# search_input.send_keys("Python")
# search_input.send_keys(Keys.RETURN)
search_input.send_keys("Python", Keys.RETURN)


sleep(5)