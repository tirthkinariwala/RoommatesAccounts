import selenium
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://hollyburn.laundroworks.com/")

time.sleep(2)

search = driver.find_element_by_name("cardNumber")

search.send_keys("2122020272")

search.send_keys(Keys.RETURN)

time.sleep(2)

tables = driver.find_elements_by_id("availabilityTable")

vals = []

for table in tables:
    tablebody = table.find_elements_by_tag_name("tbody")

# iterate over all the rows
    for row in tablebody:
         # get the text from all the td's from each row
         tds = row.find_elements_by_tag_name('td')
         for td in tds:
             vals.append(td.text)

W1 = vals[1]
W2 = vals[4]
W3 = vals[7]
W4 = vals[10]
D1 = vals[13]
D2 = vals[16]
D3 = vals[19]
D4 = vals[22]


print(W1)
print(W2)
print(W3)
print(W4)
print(D1)
print(D2)
print(D3)
print(D4)