import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/redirect_accept.html")

button1 = browser.find_element(By.TAG_NAME, "button")
button1.click()

browser.switch_to.window(browser.window_handles[1])

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = x_element.text
y = calc(x)

text_box = browser.find_element(By.ID, "answer")
text_box.send_keys(y)

submit_button = browser.find_element(By.TAG_NAME, "button")
submit_button.click()

time.sleep(10)

browser.quit()