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

# собрать все карточки товаров

book_locator = "div.product"
books = driver.find_elements(By.CSS_SELECTOR, book_locator)

# print(len(books))

# вывести в консоль инфо: название + автор + цена

for book in books:
    title = book.find_element(By.CSS_SELECTOR, 'span.product-title').text
    price = book.find_element(By.CSS_SELECTOR, 'span.price-val').text

    author = ''
    try:
         author = book.find_element(By.CSS_SELECTOR, 'div.product-author').text
    except:
         author = "Автор не указан"

    print(author + "\t" + title + "\t" + price)

sleep(5)