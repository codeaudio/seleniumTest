from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)
    num1 = browser.find_element_by_id("num1")
    x = num1.text

    num2 = browser.find_element_by_id("num2")
    y = num2.text
    int(x)
    int(y)
    z = int()+int(y)
    
    print(z)
   
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(z))
    button = browser.find_element_by_tag_name("button")
    button.click()
    
finally:
    
    time.sleep(31)

    browser.quit()