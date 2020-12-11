import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
Tirth_Test_Date = datetime(2020, 11, 17)
Saurav_Test_Date = datetime(2020, 11, 20)
Tirth_email = "tirth20000@gmail.com"
Saurav_email = "sauravchoudhury007@gmail.com"

Driving_Test_Date = [Tirth_Test_Date, Tirth_Test_Date]
emails = [Tirth_email, Saurav_email]
Potential_Tests = []



PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://onlinebusiness.icbc.com/webdeas-ui/login;type=driver")
time.sleep(2)
search = driver.find_element_by_id("mat-input-0")
search.send_keys("Kinariwala")
search = driver.find_element_by_id("mat-input-1")
search.send_keys("0201784")
search = driver.find_element_by_id("mat-input-2")
search.send_keys("shilpa")
search = driver.find_element_by_id("mat-checkbox-1-input")
search.send_keys(Keys.SPACE)
time.sleep(1)
actions = ActionChains(driver)
actions.send_keys(Keys.TAB)
actions.send_keys(Keys.TAB)
actions.send_keys(Keys.TAB)
actions.send_keys(Keys.TAB)
actions.send_keys(Keys.TAB)
actions.send_keys(Keys.RETURN)
actions.perform()
time.sleep(5)
search = driver.find_elements_by_class_name("mat-button-wrapper")
search[3].click()
time.sleep(1)
search = driver.find_elements_by_class_name("mat-button-wrapper")
search[7].click()
time.sleep(5)
search=driver.find_element_by_id("mat-input-3")
search.send_keys("vancouver ")
time.sleep(3)
actions2 = ActionChains(driver)
actions2.send_keys(Keys.DOWN)
actions2.send_keys(Keys.RETURN)
actions2.perform()
time.sleep(3)
search = driver.find_elements_by_class_name("mat-button-wrapper")
search[3].click()
time.sleep(10)
search1 = driver.find_elements_by_class_name("department-title")
search2 = driver.find_elements_by_class_name("department-appointment")
d1 = datetime.today()

for val in range(len(search1)):
    txt = search2[val].text
    x = txt.splitlines()
    x[3] = x[3][:-2]
    x[3] = x[3] + " 2020"
    d2 = datetime.strptime(x[3], "%B %d %Y")
    if d1 > d2:
        x[3] = x[3][:-4]
        x[3] = x[3] + " 2021"
    d2 = datetime.strptime(x[3], "%B %d %Y")
    if d2 < Driving_Test_Date:
        Potential_Tests = search1[val].text+"              "+x[3]
    print(search1[val].text+"              "+x[3])
    print("------------------------------------")
print(d1)
print("Potential Test Dates Are")
print(Potential_Tests)

# search = driver.find_elements_by_class_name("department-container ng-star-inserted")
# for val in search:
#     print(val.text)
#     print("------------------------------------")


