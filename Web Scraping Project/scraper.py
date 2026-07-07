from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("https://www.bookswagon.com/search-books/python")

time.sleep(8)

books = driver.find_elements(By.CLASS_NAME, "product-card")

print("Books Found:", len(books))

data = []

for book in books:

    try:
        title = book.find_element(By.CLASS_NAME, "book-title").text
    except:
        title = ""

    try:
        author = book.find_element(By.CLASS_NAME, "book-author").text
    except:
        author = ""

    try:
        price = book.find_element(By.CLASS_NAME, "current-price").text
    except:
        price = ""

    try:
        old_price = book.find_element(By.CLASS_NAME, "original-price").text
    except:
        old_price = ""

    try:
        rating = book.find_element(By.CLASS_NAME, "rating-num").text
    except:
        rating = ""

    try:
        reviews = book.find_element(By.CLASS_NAME, "reviews-count").text
    except:
        reviews = ""

    try:
        image = book.find_element(By.CLASS_NAME, "book-cover").get_attribute("src")
    except:
        image = ""

    try:
        link = book.find_element(By.TAG_NAME, "a").get_attribute("href")
    except:
        link = ""

    data.append({
        "Title": title,
        "Author": author,
        "Price": price,
        "Original Price": old_price,
        "Rating": rating,
        "Reviews": reviews,
        "Image": image,
        "Link": link
    })

driver.quit()

df = pd.DataFrame(data)

print(df.head())

df.to_csv("bookswagon_books.csv", index=False, encoding="utf-8-sig")

print("Saved", len(df), "books!")