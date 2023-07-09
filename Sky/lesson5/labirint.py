
# найти книги по слову Python
# собрать все карточки товаров
# вывести в консоль инфо: название + автор + цена

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

# зайти на лабиринт
driver.get("https://www.labirint.ru")

sleep(5)