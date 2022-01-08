from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys
import time
from urllib.parse import urljoin
import requests

# primary_url = 'https://divar.ir/s/tehran/motorcycles/tvs/wego/110?brand_model=tvs%20wego&price=10000000-&post-type=offer&non-negotiable=true'
# base = 'https://divar.ir'
# driver = webdriver.Chrome()
#
# driver.get(primary_url)
# time.sleep(2)
#
# urls = []
# for i in range(35):
#     element = driver.find_element(By.TAG_NAME, 'body')
#     element.send_keys(keys.Keys.PAGE_DOWN)
#     time.sleep(1.5)
#     soup = BeautifulSoup(driver.page_source, 'html.parser')
#     data = soup.find_all(class_='post-card-item kt-col-6 kt-col-xxl-4')
#     for parent in data:
#         a_tag = parent.find("a")
#         link = a_tag.attrs['href']
#         url = urljoin(base, link)
#         if url not in urls:
#             urls.append(url)
#
# driver.close()
# print(len(urls))

urls = ['https://divar.ir/v/موتور-وگو-ویگو-مدل-۹۵_موتورسیکلت-و-لوازم-جانبی_تهران_نیاوران_دیوار/QYZDNrB5']
for url in urls:
    data = requests.get(url)
    soup = BeautifulSoup(data.text, 'html.parser')
    brand = soup.find('p', class_='kt-unexpandable-row__value')
    price = soup.find('p', class_='kt-unexpandable-row__value')
